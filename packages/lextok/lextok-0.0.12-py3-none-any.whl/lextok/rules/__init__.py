from ._pattern import (
    CM,
    CODE,
    CONNECTOR,
    COURT,
    OF,
    OF_THE_PH_,
    PROV_DIGITS,
    TH,
    THE,
    VS,
    DigitLists,
    Label,
    Rule,
    _orth_in,
    _re,
    camel_case_pattern,
    lower_words,
    name_code,
    name_court,
    name_statute,
    titled_words,
    uncamel,
)
from .abbv import ENT_CASE_NAME, ENT_CUSTOM_DATE, Abbv, Prov
from .builder import Duo, Style
from .cites import (
    ENT_COURT_NAME,
    ENT_DOCKET_NUM,
    ENT_PROVISION_NUM,
    ENT_REPORTER_NUM,
    ENT_SERIAL_NUM,
    ENT_STATUTE_NUM,
    SPAN_CITE,
    SPAN_SER,
    SPAN_STAT,
    CourtName,
    DocketNum,
    ProvisionNum,
    ReporterNum,
    StatuteNum,
)
from .pretest import pretest_entities

BASIC_SPAN_RULES = [
    SPAN_SER,
    SPAN_CITE,
    SPAN_STAT,
]
BASIC_ENTITY_RULES = [
    ENT_CASE_NAME,
    ENT_COURT_NAME,
    ENT_CUSTOM_DATE,
    ENT_DOCKET_NUM,
    ENT_PROVISION_NUM,
    ENT_REPORTER_NUM,
    ENT_SERIAL_NUM,
    ENT_STATUTE_NUM,
]


LABELS_BUILT_IN = [
    Label.GPE,
    Label.ORG,
    Label.LAW,
]
LABELS_STATUTORY = [
    Label.ProvisionNum,
    Label.StatuteNamed,
    Label.StatuteNum,
]
LABELS_CITATION = [
    Label.CaseName,
    Label.DocketNum,
    Label.ReporterNum,
]
LABELS_GENERIC = [
    Label.SerialNum,
    Label.Personality,
    Label.Document,
]

EXT_ENTS = LABELS_BUILT_IN + LABELS_STATUTORY + LABELS_CITATION + LABELS_GENERIC
"""A collection of _entity-based_ labels that will be extended by the Detector component"""

EXT_SPANS = [
    Label.StatutoryProvision,
    Label.DecisionCitation,
    Label.SerialDocument,
]
"""A collection of _span-ruler-based_ labels that will be extended by the Detector component"""
