from collections.abc import Iterator
from enum import Enum
from typing import Any

from ._pattern import (
    CM,
    CONNECTOR,
    COURT,
    OF,
    DigitLists,
    Label,
    Rule,
    _orth_in,
    _re,
    name_court,
    titled_words,
)
from .abbv import Prov
from .builder import Style


class ReporterNum(Enum):
    scra = ["SCRA"]
    phil = ["Phil.", "Phil"]
    og = ["OG", "O.G.", "Off. Gaz."]


ENT_REPORTER_NUM = Rule(
    label=Label.ReporterNum,
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


ENT_COURT_NAME = Rule(label=Label.CourtName, patterns=[mem.value for mem in CourtName])  # type: ignore


class DocketNum(Enum):
    GR = Style(let="gr")
    AM = Style(let="am", v=["adm. matter"])
    AC = Style(let="ac", v=["adm. case"])
    BM = Style(let="bm", v=["bar matter"])


ENT_DOCKET_NUM = Rule(
    label=Label.DocketNum, patterns=[p for mem in DocketNum for p in mem.value.patterns]
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


ENT_STATUTE_NUM = Rule(
    label=Label.StatuteNum,
    patterns=[p for mem in StatuteNum for p in mem.value.patterns],
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


ENT_PROVISION_NUM = Rule(
    label=Label.ProvisionNum, patterns=list(ProvisionNum.generate())
)

## Generic Serial Number


def serialize_pattern(nodes: list[dict[str, Any]]):
    return nodes + [
        {"TEXT": {"REGEX": "\\(.*\\)"}, "OP": "?"},
        _orth_in(["No", "Nos", "No.", "Nos."]),
        {"POS": "NUM"},
    ]


exc_dockets = [
    token
    for mem in DocketNum
    if mem.value.initials
    for token in mem.value.initials.exclude_tokens
]
exc_statutes = [
    token
    for mem in StatuteNum
    if mem.value.initials
    for token in mem.value.initials.exclude_tokens
]
exc = exc_dockets + exc_statutes
up = {"IS_UPPER": True, "OP": "+", "TEXT": {"NOT_IN": exc + ["ACT"]}}
tit = {"IS_TITLE": True, "OP": "+", "TEXT": {"NOT_IN": exc + ["Act"]}}
ENT_SERIAL_NUM = Rule(
    id="serial-doc",
    label=Label.SerialNum,
    patterns=[
        serialize_pattern([up]),
        serialize_pattern([tit]),
        serialize_pattern([up, tit]),
    ],
)

# SpanRuler Candidates

provs = {"ENT_TYPE": Label.ProvisionNum.name, "OP": "+"}
stat = {"ENT_TYPE": {"IN": [Label.StatuteNamed.name, Label.StatuteNum.name]}}
opt_comma = CM | {"OP": "?"}
opt_nums = {"POS": {"IN": ["NUM", "PUNCT"]}, "OP": "*"}


SPAN_STAT = Rule(
    label=Label.StatutoryProvision,
    patterns=[
        [provs, opt_comma, stat],
        [provs, OF, stat],
        [stat, opt_comma, provs],
    ],
)
SPAN_CITE = Rule(
    label=Label.DecisionCitation,
    patterns=[
        [
            Label.CaseName.opt,
            Label.DocketNum.node,
            opt_nums,
            Label.DATE.node,
            opt_comma,
            Label.ReporterNum.node,
        ],
        [
            Label.CaseName.opt,
            Label.DocketNum.node,
            opt_nums,
            Label.DATE.node,
        ],
        [
            Label.CaseName.node,
            Label.ReporterNum.node,
            opt_nums,
            opt_comma,
            Label.DATE.node,
        ],
    ],
)
SPAN_SER = Rule(
    label=Label.SerialDocument,
    patterns=[
        [
            Label.SerialNum.node,
            opt_nums,
            Label.DATE.node,
        ]
    ],
)
