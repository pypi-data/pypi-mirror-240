from enum import Enum
from typing import Any, NamedTuple

from ._pattern import _re
from .digit import DigitLists, possible_provision_digits


def get_cased_value(v: str, cased: str | None = None):
    if cased:
        if cased == "lower":
            return v.lower()
        elif cased == "upper":
            return v.upper()
    return v


styled_case = (None, "lower", "upper")


class Def(NamedTuple):
    title: str
    abbv: str | None = None

    @property
    def dotted_abbv(self):
        bits = []
        if self.abbv:
            for style in styled_case:
                bits.append(get_cased_value(self.abbv, cased=style))
                bits.append(get_cased_value(self.abbv + ".", cased=style))
        return bits

    @property
    def options(self):
        bits = []
        for style in styled_case:
            bits.append(get_cased_value(self.title, cased=style))
        return bits + self.dotted_abbv


class Abbv(Enum):
    """Some common abbreviations used in Philippine legal text."""

    Adm = Def(title="Administrative", abbv="Adm")
    Admin = Def(title="Administrative", abbv="Admin")
    Pres = Def(title="Presidential", abbv="Pres")
    Dec = Def(title="Decree", abbv="Dec")
    Executive = Def(title="Executive", abbv="Exec")
    Blg = Def(title="Bilang", abbv="Blg")
    Number = Def(title="Number", abbv="No")
    Numbers = Def(title="Numbers", abbv="Nos")
    Const = Def(title="Constitution", abbv="Const")
    Company = Def(title="Company", abbv="Co")
    Corporation = Def(title="Corporation", abbv="Corp")
    Incorporated = Def(title="Incorporated", abbv="Inc")
    Phil1 = Def(title="Philippines", abbv="Phil")
    Phil2 = Def(title="Philippines", abbv="Phils")
    Limited = Def(title="Limited", abbv="Ltd")
    Association = Def(title="Association", abbv="Assoc")
    Assistant = Def(title="Assistant", abbv="Ass")
    Department = Def(title="Department", abbv="Dept")
    Nat1 = Def(title="National", abbv="Nat")
    Nat2 = Def(title="National", abbv="Natl")
    St = Def(title="Street", abbv="St")
    Road = Def(title="Road", abbv="Rd")
    Ave = Def(title="Avenue", abbv="Ave")
    Blk = Def(title="Block", abbv="Blk")
    Brgy = Def(title="Barangay", abbv="Brgy")
    Building = Def(title="Building", abbv="Bldg")
    Purok = Def(title="Purok", abbv="Prk")
    Subdivision = Def(title="Subdivision", abbv="Subd")
    Highway = Def(title="Highway", abbv="Hwy")
    Municipality = Def(title="Municipality", abbv="Mun")
    City = Def(title="City", abbv="Cty")
    Province = Def(title="Province", abbv="Prov")
    Governor = Def(title="Governor", abbv="Gov")
    Congressman = Def(title="Congressman", abbv="Cong")
    General = Def(title="General", abbv="Gen")
    Lieutenant = Def(title="Lieutenant", abbv="Lt")
    Sct = Def(title="Scout", abbv="Sct")
    Sta = Def(title="Santa", abbv="Sta")
    Sto = Def(title="Santo", abbv="Sto")
    Vda = Def(title="Viuda", abbv="Vda")
    Jr = Def(title="Junior", abbv="Jr")
    Sr = Def(title="Senior", abbv="Sr")
    Fr = Def(title="Father", abbv="Fr")
    Bro = Def(title="Brother", abbv="Bro")
    Dr = Def(title="Doctor", abbv="Dr")
    Dra = Def(title="Doctora", abbv="Dra")
    Maria = Def(title="Maria", abbv="Ma")
    Hon = Def(title="Honorable", abbv="Hon")
    Atty = Def(title="Attorney", abbv="Atty")
    Engr = Def(title="Engineer", abbv="Engr")
    Justice = Def(title="Justice", abbv="J")

    @classmethod
    def make_special_rules(cls) -> dict[str, list[dict[str, str]]]:
        """Used to create special rules for custom tokenizer."""
        rules = {}
        for style in styled_case:
            for bit in cls.set_abbvs(cased=style):
                rules[f"{bit}."] = [{"ORTH": f"{bit}."}]
        return rules

    @classmethod
    def set_abbvs(cls, cased: str | None = None):
        for member in cls:
            if v := member.value.abbv:
                yield get_cased_value(v, cased)

    @classmethod
    def set_fulls(cls, cased: str | None = None):
        for member in cls:
            yield get_cased_value(member.value.title, cased)


_re("(" + "|".join(DigitLists.generate_options()) + ")")


class Prov(Enum):
    """A provision of a statute may be abbreviated and the same may have different variations:
    e.g. titlecase, lowercase, and uppercase."""

    Title = Def(title="Title", abbv="Tit")
    SubT1 = Def(title="SubTitle")
    SubT2 = Def(title="Sub-Title")
    Book = Def(title="Book", abbv="Bk")
    Chapter = Def(title="Chapter", abbv="Ch")
    SubChap = Def(title="Sub-Chapter", abbv="Sub-Chap")
    Article = Def(title="Article", abbv="Art")
    SubArt1 = Def(title="SubArticle")
    SubArt2 = Def(title="Sub-Article")
    Section = Def(title="Section", abbv="Sec")
    SubSec1 = Def(title="SubSection")
    SubSec2 = Def(title="Sub-Section")
    Par = Def(title="Paragraph", abbv="Par")
    SubPar = Def(title="Sub-Paragraph", abbv="Sub-Par")
    Rule = Def(title="Rule")
    Canon = Def(title="Canon")

    @classmethod
    def make_special_rules(cls) -> dict[str, list[dict[str, str]]]:
        """Used to create special rules for custom tokenizer."""
        rules = {}
        for style in styled_case:
            for bit in cls.set_abbvs(cased=style):
                rules[f"{bit}."] = [{"ORTH": f"{bit}."}]
        return rules

    @classmethod
    def make_attr_rules(cls) -> list[dict[str, Any]]:
        """Used to create rules for the attribute ruler."""
        rules = []
        for member in cls:
            noun_rule = member.create_attribute_rules(
                attrs={"POS": "NOUN"},
                index=0,
            )
            digit_rule = member.create_attribute_rules(
                attrs={"POS": "NUM", "LIKE_NUM": True},
                index=1,
            )
            rules.extend([noun_rule, digit_rule])
        return rules

    def create_attribute_rules(
        self,
        attrs: dict[str, Any],
        digit_patterns: list[dict[str, Any]] = possible_provision_digits,
        index: int = 1,
    ):
        """Each member can contain explicit rules so that the `digit_patterns`
        are included in the list of patterns with the following formula:

        first node | second node
        :-- | --:
        The member option for Sec., Section, etc. | a "digit" pattern e.g. 1, 1(a)

        The list of patterns can then be applied as part of an attribute ruler
        https://spacy.io/usage/linguistic-features#mappings-exceptions so that
        the token in the second node, i.e. the digit, can be set with the attributes defined in
        `attributes_to_set`.
        """
        patterns = [
            [{"ORTH": opt}, v] for v in digit_patterns for opt in self.value.options
        ]
        return {"index": index, "patterns": patterns, "attrs": attrs}

    @classmethod
    def set_abbvs(cls, cased: str | None = None):
        for member in cls:
            if v := member.value.abbv:
                yield get_cased_value(v, cased)

    @classmethod
    def set_fulls(cls, cased: str | None = None):
        for member in cls:
            yield get_cased_value(member.value.title, cased)
