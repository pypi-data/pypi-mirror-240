# lextok

![Github CI](https://github.com/justmars/lextok/actions/workflows/main.yml/badge.svg)

> [!IMPORTANT]
> Should be used in tandem with [doclex](https://github.com/justmars/doclex)

## Quickstart

```sh
poetry env use 3.11.6 # 3.12 not yet supported
poetry install
poetry shell
python -m spacy download en_core_web_sm # base model
```

## Rationale

### Before

```py
import spacy

nlp = spacy.load("en_core_web_sm")  # no modifications to the model
doc1 = nlp("Sec. 36(b)(21)")
for token in doc1:
    print(f"{token.text=} {token.pos_=} {token.ent_type_=}, {token.i=}")
"""
token.text='Sec' token.pos_='PROPN' token.ent_type_='ORG' token.i=0
token.text='.' token.pos_='PUNCT' token.ent_type_='' token.i=1
token.text='36(b)(21' token.pos_='NUM' token.ent_type_='CARDINAL' token.i=2
token.text=')' token.pos_='PUNCT' token.ent_type_='' token.i=3
"""
```

### After

```py
from lextok import lextok

lex = lextok()  # inclusion of custom tokenizer, attribute and entity ruler
doc2 = lex("Sec. 36(b)(21)")
for token in doc2:
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='Sec.' token.pos_='NOUN' token.ent_type_='ProvisionNum' token.i=0
token.text='36(b)(21)' token.pos_='NUM' token.ent_type_='ProvisionNum' token.i=1
"""
```

Token entities can be merged:

```py
from lextok import lextok

lex = lextok(finalize_entities=True)
doc2 = lex("Sec. 36(b)(21)")
for token in doc2:
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='Sec. 36(b)(21)' token.pos_='NUM' token.ent_type_='ProvisionNum' token.i=0
"""
```

## Pattern creation

A pattern consists of a list of tokens, e.g. space space between the word, a dot, and the number?

```py
[
    {"ORTH": {"IN": ["Tit", "Bk", "Ch", "Sub-Chap", "Art", "Sec", "Par", "Sub-Par"]}},
    {"ORTH": "."},  # with dot
    {"POS": "NUM"},
]
```

This is another pattern where the dot is connected to the word:

```py
[
    {
        "ORTH": {
            "IN": [
                "Tit.",
                "Bk.",
                "Ch.",
                "Sub-Chap.",
                "Art.",
                "Sec.",
                "Par.",
                "Sub-Par.",
            ]
        }
    },
    {"POS": "NUM"},
]  # no separate dot
```

There are many variations. It becomes possible to generate a list of patterns algorithmically and save them to a `*.jsonl` file, e.g.:

```py
from lextok import ENT_PROVISION_NUM

print(ENT_PROVISION_NUM.patterns)  # view patterns
ENT_PROVISION_NUM.create_file()  # create pattern file within /lektok/
```

## Entity list

Python | Label name | Example | Desc.
-- | -- | -- | --
`ENT_PROVISION_NUM`| ProvisionNum | Art. 2 | Part of a statute
`ENT_STATUTE_NUM`| StatuteNum | RA 386 | Statute references
`ENT_DOCKET_NUM`| DocketNum | GR No. 12345 | Docket citations, without the date
`ENT_REPORTER_NUM`| ReporterNum | 41 SCRA 1 | Court citations via reporter
`ENT_CASE_NAME`| CaseName | Juan de la Cruz v. Republic of the Philippines | Separated by `v.`
`ENT_SERIAL_NUM`| SerialNum | Doc No. 12345 | Unclassified, excludes `ENT_STATUTE_NUM`, `ENT_DOCKET_NUM` initials

## Detected combinations

### doc._.stats

```py
txt0 = "Sec. 36(b)(21), RA 12452"
doc = lex(txt0)
for token in doc:  # reveals 2 entities
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='Sec. 36(b)(21)' token.pos_='NUM' token.ent_type_='ProvisionNum' token.i=0
token.text=',' token.pos_='PUNCT' token.ent_type_='' token.i=1
token.text='RA 12452' token.pos_='PROPN' token.ent_type_='StatuteNum' token.i=2
"""
```

These entities, because of the `Provision` + `Statute` span ruler pattern can be detected with:

```py
doc._.stats
"""
['Sec. 36(b)(21), RA 12452']
"""
```

The reverse pattern (e.g. `Statute` + `Provision`) is likewise detected:

```py
txt1 = "Republic Act No. 141, Sec. 1"
doc = lex(txt1)
for token in doc:  # reveals 2 entities
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='Republic Act No. 141' token.pos_='PROPN' token.ent_type_='StatuteNum' token.i=0
token.text=', Sec. 1' token.pos_='NOUN' token.ent_type_='ProvisionNum' token.i=1
"""
doc._.stats
"""
['Republic Act No. 141, Sec. 1']
"""
```

### doc._.cites

```py
txt1 = "A v. B, G.R. Nos. 12414, 6546546, 324235 feb 1, 2021, 50 SCRA 510"
doc = lex(txt1)
for token in doc:  # reveals 2 entities
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='A v. B,' token.pos_='PROPN' token.ent_type_='CaseName' token.i=0
token.text='G.R. Nos. 12414' token.pos_='PROPN' token.ent_type_='DocketNum' token.i=1
token.text=',' token.pos_='PUNCT' token.ent_type_='' token.i=2
token.text='6546546' token.pos_='NUM' token.ent_type_='DATE' token.i=3
token.text=',' token.pos_='PUNCT' token.ent_type_='' token.i=4
token.text='324235' token.pos_='NUM' token.ent_type_='' token.i=5
token.text='feb 1, 2021' token.pos_='PROPN' token.ent_type_='DATE' token.i=6
token.text=',' token.pos_='PUNCT' token.ent_type_='' token.i=7
token.text='50 SCRA 510' token.pos_='PROPN' token.ent_type_='ReporterNum' token.i=8
"""
doc._.cites
"""
['A v. B, G.R. Nos. 12414, 6546546, 324235 feb 1, 2021, 50 SCRA 510']
"""
```

## Customization

### Label creation

A `Label` is shorthand for creating an `ENT_TYPE`. Each member of the `Label` Enum will contain properties:

1. `@node` to represent `{"ENT_TYPE": <Enum member name>}`
2. `@opt`: adds `{"OP": "?}` to the `@node`

### Existing labels

```py
from lextok import Label

for label in Label:
    print(label.name)
"""
PERSON
ORG
DATE
Personality
Common
GovtDivision
Concept
Doctrine
Document
ProvisionNum
StatuteNum
StatuteNamed
StatutoryProvision
CaseName
DocketNum
ReporterNum
DecisionCitation
SerialNum
SerialDocument
Pleading
CourtName
CourtOrder
"""
```

### Rule creation

A `Rule` enables the creation of pattern objects containing the same `Label` and custom `id`, if provided. Sample rule:

```py
sample = Rule(
    id="ministry-labor",
    label=Label.GovtDivision,
    patterns=[
        [
            {"LOWER": "the", "OP": "?"},
            {"LOWER": "ministry"},
            {"LOWER": "of"},
            {"LOWER": "labor"},
        ]
    ],
)
```

### Existing entity rules

```py
from lextok import BASIC_ENTITY_RULES

for rule in BASIC_ENTITY_RULES:
    print(rule)
"""
<Rule for Label (CaseName): 12 patterns>
<Rule for Label (CourtName): 8 patterns>
<Rule for Label (DATE): 109 patterns>
<Rule for Label (DocketNum): 68 patterns>
<Rule for Label (ProvisionNum): 24 patterns>
<Rule for Label (ReporterNum): 6 patterns>
<Rule for Label (SerialNum): 3 patterns>
<Rule for Label (StatuteNum): 124 patterns>
"""
```

### Add more entity rules

Create a list of `Rule` objects, e.g.:

```py
from lextok import lextok, Rule, BASIC_ENTITY_RULES, Label

added_rules = [
    Rule(
        id="ministry-labor",
        label=Label.GovtDivision,
        patterns=[
            [
                {"LOWER": "the", "OP": "?"},
                {"LOWER": "ministry"},
                {"LOWER": "of"},
                {"LOWER": "labor"},
            ]
        ],
    ),
    Rule(
        id="intermediate-scrutiny",
        label=Label.Doctrine,
        patterns=[
            [
                {"LOWER": "test", "OP": "?"},
                {"LOWER": "of", "OP": "?"},
                {"LOWER": "intermediate"},
                {"LOWER": "scrutiny"},
                {"LEMMA": {"IN": ["test", "approach"]}, "OP": "?"},
            ]
        ],
    ),
]

# Include new rules in lextok language
nlp = lextok(finalize_entities=True, entity_rules=BASIC_ENTITY_RULES + added_rules)

# Test detection
doc = nlp(
    "Lorem ipsum, sample text. The Ministry of Labor is a govt division. Hello world. The test of intermediate scrutiny is a constitutional law concept."
)
doc.ents  # (The Ministry of Labor, test of intermediate scrutiny)
```

### Add more span rules

Each span ruler is identified by a span key and each key should be _unique_. The basic span keys are derived from each `Rule`'s label, e.g. `StatutoryProvision`. To add more rules to this span key, modify the patterns field, likeso:

```py
from lextok.rules import SPAN_STAT

SPAN_STAT.patterns = SPAN_STAT.patterns + new_pattern
SPANS = [SPAN_SER, SPAN_CITE, SPAN_STAT]
```
