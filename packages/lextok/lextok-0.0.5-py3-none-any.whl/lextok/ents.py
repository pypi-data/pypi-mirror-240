import io
import itertools
import re
from collections.abc import Iterator
from enum import Enum
from pathlib import Path
from typing import Any

import jsonlines
import spacy
from pydantic import BaseModel, model_serializer

from .bits import (
    CM,
    CONNECTOR,
    COURT,
    OF,
    VS,
    Abbv,
    DigitLists,
    Prov,
    Style,
    _orth_in,
    _re,
    name_court,
    titled_words,
)

abbv_months = (
    Abbv.January,
    Abbv.February,
    Abbv.March,
    Abbv.April,
    Abbv.June,
    Abbv.July,
    Abbv.August,
    Abbv.Sept1,
    Abbv.Sept2,
    Abbv.October,
    Abbv.November,
    Abbv.December,
)
extras = " ".join(
    set(
        op
        for s in (
            Abbv.Phil1,
            Abbv.Phil2,
            Abbv.Company,
            Abbv.Corporation,
            Abbv.Limited,
            Abbv.Incorporated,
        )
        for op in s.value.options
    )
)
extras += " . , et al. et al the Jr Jr. Sr Sr. III IV Partnership Dev't"
misc = _orth_in(extras.split()) | {"OP": "*"}
opt_acronym = _re("\\([A-Z]+\\)") | {"OP": "?"}


camel_case_pattern = re.compile(
    r".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)"
)


def convert_from_camel_case(text: str) -> list[str]:
    """For text in camelCaseFormatting, convert into a list of strings."""
    return [m.group(0) for m in camel_case_pattern.finditer(text)]


class Rule(BaseModel):
    """`patterns` associated with a single `label` (optionally
    with an `id` as well that serve as the `ent_id_` in `spacy.tokens.Doc.ents`).

    This makes it possible to serialize pattern objects as a file, see generally:

    1. https://spacy.io/usage/rule-based-matching#entityruler-files
    2. https://spacy.io/usage/rule-based-matching#spanruler-files

    Use with: <Rule instance>.create_file() or <Rule instance>.model_dump() to
    simply get a list of patterns without file creation. See common usage in
    `set_entity_ruler()`
    """

    id: str | None = None
    label: str
    patterns: list[list[dict[str, Any]]]

    @property
    def ent_id(self):
        return self.id or "-".join(convert_from_camel_case(self.label)).lower()

    @model_serializer
    def ser_model(self) -> list[dict[str, Any]]:
        """Following the pydantic convention for .model_dump(); instead of a traditional
        `dict` return, the function results in a serialized list of patterns for consumption
        by either `create_file()` or the _entity_ruler_ spacy pipeline."""
        return [
            {"id": self.ent_id, "label": self.label, "pattern": pattern}
            for pattern in self.patterns
        ]

    def create_file(self, file: Path | None = None):
        """Will update the file, if it exists; will create a file, if it doesn't exist."""
        if not file:
            file = Path(__file__).parent.joinpath(f"{self.ent_id}.jsonl")
        fp = io.BytesIO()
        with jsonlines.Writer(fp) as writer:
            for ser_pattern in self.model_dump():
                writer.write(ser_pattern)
        file.unlink(missing_ok=True)
        file.write_bytes(fp.getbuffer())
        return file


def create_date_entities():
    def add_year(p: list[dict[str, Any]]) -> dict:
        opt_comma = CM | {"OP": "?"}
        p.insert(0, opt_comma)
        return {"id": "ent-date", "label": "DATE", "pattern": p + [_re("\\d{4}")]}

    # first output: the series pattern
    yield add_year([{"LOWER": {"IN": ["s.", "series"]}}, OF | {"OP": "?"}])
    # second output: loop over the months
    for month_data in abbv_months:
        for month in month_data.value.options:
            month_node = {"ORTH": month}
            day_node = _orth_in([f"{str(i)}" for i in range(1, 31)])
            yield add_year([month_node, day_node, CM])


class CaseName(Enum):
    ent = {"ENT_TYPE": {"IN": ["ORG", "PERSON"]}, "OP": "+"}
    pos = {"POS": {"IN": ["PROPN", "ADP", "DET"]}, "OP": "+"}
    upper = {"IS_UPPER": True, "OP": "{1,6}"}
    title = {"IS_TITLE": True, "OP": "{1,6}"}

    @staticmethod
    def _vs(first: dict[str, Any], second: dict[str, Any]) -> list[dict[str, Any]]:
        return [first, opt_acronym, misc] + [VS] + [second, opt_acronym, misc]

    @classmethod
    def permute_patterns(cls) -> list[list[dict[str, Any]]]:
        pairs = itertools.permutations((m.value for m in cls), 2)
        return [cls._vs(a, b) for a, b in pairs]


CASE_NAME = Rule(label="CaseName", patterns=CaseName.permute_patterns())


class ReporterNum(Enum):
    scra = ["SCRA"]
    phil = ["Phil.", "Phil"]
    og = ["OG", "O.G.", "Off. Gaz."]


REPORTER_NUM = Rule(
    label="ReportNo",
    patterns=[
        [{"LIKE_NUM": True}, {"ORTH": style}, {"LIKE_NUM": True}]
        for member in ReporterNum
        for style in member.value
    ],
)


class CourtName(Enum):
    SC = [{"LOWER": "supreme", "IS_TITLE": True}, COURT]
    RTC = titled_words("regional trial court")
    CA = name_court("appeals")
    CFI = name_court("first instance")
    MeTC = titled_words("metropolitan trial court")
    MCTC = titled_words("municipal circuit court")
    MTC = titled_words("municipal trial court")
    MTCC = (
        titled_words("municipal trial court")
        + [{"LOWER": "in"}]
        + titled_words("the cities")
    )


COURT_NAME = Rule(label="CourtName", patterns=[mem.value for mem in CourtName])  # type: ignore


class DocketNo(Enum):
    GR = Style(let="gr")
    AM = Style(let="am", v=["adm. matter"])
    AC = Style(let="ac", v=["adm. case"])
    BM = Style(let="bm", v=["bar matter"])


DOCKET_NUM = Rule(
    label="DocketNo", patterns=[p for mem in DocketNo for p in mem.value.patterns]
)


class StatuteNum(Enum):
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


STATUTE_NUM = Rule(
    label="StatuteNum", patterns=[p for mem in StatuteNum for p in mem.value.patterns]
)


class ProvisionNum(Enum):
    """A statute's text is divided into (sometimes hierarchical) provisions.
    This structure combines both the adjective division, e.g. `Sec.`, `Section`, `Bk.`, etc.
    (which may have different casing and abbreviations) with presumed valid serial numbers,
    e.g. `1`, `1-b`, `III`, etc.
    """

    abbreviated_Sec1 = list(Prov.set_abbvs())
    abbreviated_sec1 = list(Prov.set_abbvs(cased="lower"))
    abbreviated_SEC1 = list(Prov.set_abbvs(cased="upper"))
    Section1 = list(Prov.set_fulls())
    section1 = list(Prov.set_fulls(cased="lower"))
    SECTION1 = list(Prov.set_fulls(cased="upper"))

    @classmethod
    def generate(cls) -> Iterator[list[dict[str, Any]]]:
        specific_digits = _re("(" + "|".join(DigitLists.generate_options()) + ")")
        for member in cls:
            for end in [{"POS": "NUM"}, specific_digits]:
                start = [CONNECTOR]  # start
                if member.name.startswith("abbreviated_"):
                    yield start + [_orth_in(member.value), {"ORTH": "."}, end]
                    yield start + [_orth_in([f"{v}." for v in member.value]), end]
                yield start + [_orth_in(member.value), end]


PROVISION_NUM = Rule(label="ProvisionNum", patterns=list(ProvisionNum.generate()))


def set_entity_ruler(nlp: spacy.language.Language):
    ruler = nlp.add_pipe(
        "entity_ruler",
        config={"overwrite_ents": True, "validate": True},
        validate=True,
    )

    ruler.add_patterns(DOCKET_NUM.model_dump())  # type: ignore
    ruler.add_patterns(STATUTE_NUM.model_dump())  # type: ignore
    ruler.add_patterns(CASE_NAME.model_dump())  # type: ignore
    ruler.add_patterns(REPORTER_NUM.model_dump())  # type: ignore
    ruler.add_patterns(COURT_NAME.model_dump())  # type: ignore
    ruler.add_patterns(PROVISION_NUM.model_dump())  # type: ignore
    ruler.add_patterns(list(create_date_entities()))  # type: ignore

    return nlp
