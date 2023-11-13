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
    convert_from_camel_case,
    lower_words,
    name_code,
    name_court,
    name_statute,
    titled_words,
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
