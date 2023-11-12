# lextok

![Github CI](https://github.com/justmars/lextok/actions/workflows/main.yml/badge.svg)

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

lex = lextok(merge_entities=True)
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
from lextok import PROVISION_NUM

print(PROVISION_NUM.patterns)  # view patterns
PROVISION_NUM.create_file()  # create pattern file within /lektok/
```

## Entity list

1. `PROVISION_NUM`, e.g. Art. 2
2. `STATUTE_NUM`, e.g. RA 386
3. `CASE_NAME`, e.g. Juan de la Cruz v. Republic of the Philippines
4. `DOCKET_NUM`, e.g. GR No. 12345
5. `REPORTER_NUM`, e.g. 41 SCRA 1
