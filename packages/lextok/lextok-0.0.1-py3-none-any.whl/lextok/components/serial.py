from enum import Enum
from typing import Any, NamedTuple

from ._pattern import CONNECTOR, _orth_in, _re
from .duo import Duo


class Style(NamedTuple):
    v: list[str] = []
    let: str | None = None
    pre: list[str] = ["No", "Nos", "No.", "Nos."]
    r: str = "[\\w-]+"

    @property
    def title_pre(self) -> list[dict[str, Any]]:
        return [_orth_in(self.pre), _re(self.r)]

    @property
    def upper_pre(self) -> list[dict[str, Any]]:
        return [_orth_in([i.upper() for i in self.pre]), _re(self.r)]

    @property
    def token_parts(self):
        """The first pass is for indiscriminate words e.g. `bar matter`; the second, for
        dealing with periods, e.g. `adm. matter`. The first will generate the following as
        token parts ('bar','matter'); the second: ('adm.','matter'), ('adm','.','matter')
        """
        objs = set()
        for words in self.v:
            partial = []
            for word in words.split():
                partial.append(word)
            objs.add(tuple(partial))
        for words in self.v:
            partial = []
            for word in words.split():
                if word.endswith("."):
                    cleaned = word.removesuffix(".")
                    partial.append(cleaned)
                    partial.append(".")
                else:
                    partial.append(word)
            objs.add(tuple(partial))
        return objs

    @property
    def _title_num(self) -> list[list[dict[str, Any]]]:
        return [
            [{"ORTH": sub.title()} for sub in subtokens] + self.title_pre
            for subtokens in self.token_parts
        ]

    @property
    def _title_no_num(self) -> list[list[dict[str, Any]]]:
        return [
            [{"ORTH": sub.title()} for sub in subtokens] + [_re(self.r)]
            for subtokens in self.token_parts
        ]

    @property
    def _upper_num(self) -> list[list[dict[str, Any]]]:
        return [
            [{"ORTH": sub.upper()} for sub in subtokens] + self.upper_pre
            for subtokens in self.token_parts
        ]

    @property
    def _upper_no_num(self) -> list[list[dict[str, Any]]]:
        return [
            [{"ORTH": sub.upper()} for sub in subtokens] + [_re(self.r)]
            for subtokens in self.token_parts
        ]

    @property
    def initials(self):
        if not self.let:
            return None
        if len(self.let) != 2:
            return None
        return Duo(a=self.let[0], b=self.let[1])

    @property
    def word_patterns(self):
        patterns = []
        patterns.extend(self._title_num)
        patterns.extend(self._title_no_num)
        patterns.extend(self._upper_num)
        patterns.extend(self._upper_no_num)
        return patterns

    @property
    def letter_patterns(self):
        if not self.initials:
            return None

        items = []
        for b in self.initials.add_to_each_pattern(self.upper_pre):
            items.append(b)

        for b in self.initials.add_to_each_pattern(self.title_pre):
            items.append(b)

        for b in self.initials.add_to_each_pattern([_re(self.r)]):
            items.append(b)
        return items

    @property
    def patterns(self):
        words = self.word_patterns
        letters = self.letter_patterns
        p = words + letters if letters else words
        return p


class DocketNo(Enum):
    GR = Style(let="gr")
    AM = Style(let="am", v=["adm. matter"])
    AC = Style(let="ac", v=["adm. case"])
    BM = Style(let="bm", v=["bar matter"])

    @classmethod
    def get_patterns(cls):
        return [pattern for member in cls for pattern in member.value.patterns]

    def create_attribute_rules(self):
        return {"index": -1, "patterns": self.value.patterns, "attrs": {"POS": "NUM"}}

    @classmethod
    def make_attr_rules(cls) -> list[dict[str, Any]]:
        """Used to create rules for the attribute ruler."""
        rules = []
        for member in cls:
            rules.append(member.create_attribute_rules())
        return rules

    @classmethod
    def make_special_rules(cls):
        return {
            k: v
            for member in cls
            if member.value.initials
            for k, v in member.value.initials.as_token.items()
        }


class StatuteNo(Enum):
    RA = Style(let="ra", r="\\d{1,5}", v=["republic act", "rep. act"])
    CA = Style(let="ca", r="\\d{1,3}", v=["commonwealth act", "com. act"])
    BP = Style(let="bp", r="\\d{1,3}(-?(A|B))?", v=["batas pambansa"], pre=["Blg."])
    EO = Style(let="eo", r="\\d{1,4}(-?(A|B|C))?", v=["executive order", "exec. order"])
    PD = Style(
        let="pd",
        r="\\d{1,4}(-?(A|B))?",
        v=["presidential decree", "pres. decree", "pres. dec."],
    )
    ACT = Style(r="\\d{1,4}", v=["act"])

    @classmethod
    def get_patterns(cls):
        return [pattern for member in cls for pattern in member.value.patterns]

    @classmethod
    def make_special_rules(cls):
        return {
            k: v
            for member in cls
            if member.value.initials
            for k, v in member.value.initials.as_token.items()
        }

    def create_attribute_rules(self):
        return {"index": -1, "patterns": self.value.patterns, "attrs": {"POS": "NUM"}}

    @classmethod
    def make_attr_rules(cls) -> list[dict[str, Any]]:
        """Used to create rules for the attribute ruler."""
        rules = []
        for member in cls:
            rules.append(member.create_attribute_rules())
        return rules


class DocNumConstructor(Enum):
    uppercase = {"IS_UPPER": True, "OP": "+"}
    titlecase = {"IS_TITLE": True, "OP": "+"}
    cover = {"TEXT": {"REGEX": "\\(.*\\)"}, "OP": "?"}
    indicator = {"ORTH": "No."}
    v = {"POS": "NUM"}

    @classmethod
    def create_base(cls) -> list:
        return [cls.cover, cls.indicator, cls.v]

    @classmethod
    def use_upper(cls) -> list[dict]:
        return [b.value for b in [cls.uppercase] + cls.create_base()]

    @classmethod
    def use_title(cls) -> list[dict]:
        return [b.value for b in [cls.titlecase] + cls.create_base()]

    @classmethod
    def use_upper_title(cls) -> list[dict]:
        return [b.value for b in [cls.uppercase, cls.titlecase] + cls.create_base()]

    @classmethod
    def get_patterns(cls) -> list[list[dict]]:
        values = [cls.use_upper_title(), cls.use_title(), cls.use_upper()]
        for v in values:
            v.insert(0, CONNECTOR)
        return values
