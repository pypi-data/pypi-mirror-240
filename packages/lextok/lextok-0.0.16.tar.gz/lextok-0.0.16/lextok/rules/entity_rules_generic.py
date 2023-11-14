from ._pattern import (
    CM,
    COURT,
    OF,
    OF_THE_PH_,
    TH,
    Label,
    Rule,
    _orth_in,
    _re,
    titled_words,
)
from .abbreviations import CaseName, abbv_months, org_options

ENT_CUSTOM_DATE = Rule(
    id="ent-date",
    label=Label.DATE,
    patterns=[
        [
            CM | {"OP": "?"},
            {"LOWER": {"IN": ["s.", "series"]}},
            OF | {"OP": "?"},
            _re("\\d{4}"),
        ]
    ]
    + [
        [
            CM | {"OP": "?"},
            {"ORTH": month},
            _orth_in([f"{str(i)}" for i in range(1, 31)]),
            CM | {"OP": "?"},
            _re("\\d{4}"),
        ]
        for month_data in abbv_months
        for month in month_data.value.options
    ],
)


ENT_CASE_NAME = Rule(
    label=Label.CaseName,
    patterns=CaseName.permute_patterns(),
)

ENT_GENERIC_PERSON_PREFIX = Rule(
    id="titled",
    label=Label.PERSON,
    patterns=[
        [
            _orth_in(["Atty.", "Hon.", "Engr.", "Dr.", "Dra."]),
            {"IS_TITLE": True, "OP": "+"},
        ],
        [
            _orth_in(["Atty.", "Hon.", "Engr.", "Dr.", "Dra."]),
            {"ENT_TYPE": Label.PERSON.name},
        ],
    ],
)


ENT_GENERIC_ESTATE = Rule(
    id="estate",
    label=Label.ORG,
    patterns=[
        [{"ORTH": "Estate"}, OF, {"IS_TITLE": True, "OP": "+"}],
        [{"ORTH": "Estate"}, OF, {"ENT_TYPE": Label.PERSON.name}],
    ],
)

ENT_GENERIC_ORG = Rule(
    id="incorporated",
    label=Label.ORG,
    patterns=[
        [
            {"IS_TITLE": True, "OP": "+"},
            {"ORTH": ",", "IS_PUNCT": True, "OP": "?"},
            {
                "LOWER": {"IN": list(set(o.lower() for o in org_options))},
                "IS_TITLE": True,
            },
        ]
    ],
)

ENT_GENERIC_LAWS = Rule(
    id="named-generic-laws",
    label=Label.StatuteNamed,
    patterns=[
        [
            TH,
            _orth_in(["1987", "1973", "1935"]) | {"OP": "?"},
            _orth_in(["CONSTITUTION", "Constitution", "CONST", "Const."]),
        ],
        [{"ORTH": "Rules"}, OF, COURT],
        titled_words("old code"),
        titled_words("philippine civil code"),
        titled_words("civil code of 1950"),
        titled_words("civil code of 1889"),
        titled_words("civil code"),
        titled_words("civil code") + OF_THE_PH_,
    ],
)

ENT_GENERIC_DOC = Rule(
    id="papers",
    label=Label.Document,
    patterns=[
        [
            {
                "IS_TITLE": True,
                "OP": "{1,3}",
                "ORTH": {"NOT_IN": ["This", "The", "A", "An"]},
            },
            _orth_in(["Writ", "Motion", "Notice", "Contract", "Agreement"]),
            {"ORTH": {"IN": ["of", "to", "for"]}},
            {"IS_TITLE": True, "OP": "+"},
            {"ORTH": {"IN": ["of", "as", "to"]}, "OP": "*"},
            {"IS_TITLE": True, "OP": "+"},
        ],
        [
            {
                "IS_TITLE": True,
                "OP": "{1,3}",
                "ORTH": {"NOT_IN": ["This", "The", "A", "An"]},
            },
            _orth_in(["Writ", "Motion", "Notice", "Contract", "Agreement"]),
            {"ORTH": {"IN": ["of", "to", "for"]}},
            {"IS_TITLE": True, "OP": "+"},
        ],
    ],
)
