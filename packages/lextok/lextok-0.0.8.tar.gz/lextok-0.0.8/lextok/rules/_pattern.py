import io
import itertools
import re
import string
from enum import Enum
from pathlib import Path
from typing import Any

import inflect
import jsonlines
import roman  # type: ignore
from pydantic import BaseModel, model_serializer

# PATTERN NODES

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


def _re(v: str, anchored: bool = True) -> dict[str, Any]:
    """Helper function to add an anchored, i.e. `^`<insert value `v` here>`$`
    regex pattern, following the convention `{"TEXT": {"REGEX": f"^{v}$"}}`
    spacy convention.
    """
    if anchored:
        v = f"^{v}$"
    return {"TEXT": {"REGEX": v}}


def _orth_in(v_list: list[str]):
    """Helper function to add a regex pattern where the options contained
    in the `v_list` are limited, following the convention `{"ORTH": {"IN": v_list}}`
    spacy convention.
    """
    return {"ORTH": {"IN": v_list}}


# REUSABLES


OF = {"LOWER": "of"}
"""Required `the`: `{"LOWER": "of"}`"""

TH = {"LOWER": "the", "OP": "?"}
"""Optional `the`: `{"LOWER": "the", "OP": "?"}`"""

COURT = {"ORTH": "Court"}
"""Required title cased `Court`"""

CODE = {"ORTH": "Code"}
"""Required title cased `Code`"""

THE = {"LOWER": "the"}
"""Required `the`: `{"LOWER": "the"}`"""

VS = _orth_in(["v.", "vs."])
"""Common formula for consistency: `{"ORTH": {"IN": ["v.", "vs."]}}`"""

PH = _orth_in(["Phil", "Phil.", "Phils", "Phils.", "Philippines"])

CM = {"ORTH": ","}

OF_THE_PH_ = [OF, THE, PH]

CONNECTOR = _orth_in(["of", "the", ",", "and", "&"]) | {"OP": "*"}
"""Setting this optional token ("of", "the", ",", "and", "&") allows for
ProvisionNums/serials to be merged later"""

### PATTERN FUNCS


def lower_words(words: str):
    """Will separate each word separated by spaces into a
    `{"LOWER": <word.strip().lower()>}` spacy pattern."""
    return [{"LOWER": word.strip().lower()} for word in words.split()]


def titled_words(words: str):
    """Will separate each word separated by spaces into a
    `{"LOWER": <word.lower()>, "IS_TITLE": True}` spacy pattern."""
    return [w | {"IS_TITLE": True} for w in lower_words(words)]


def name_code(fragments: str):
    """Use of `lower_words()` for Code names"""
    return [TH, {"LOWER": "code"}, OF] + lower_words(fragments)


def name_court(fragments: str):
    """Create title-based Court names"""
    return [TH, COURT, OF] + titled_words(fragments)


def name_statute(
    fragments: str | list[dict[str, Any]],
    options: list[str] = ["law", "act"],
) -> list[dict[str, Any]]:
    """If a string is passed as fragments, uses `lower_words()`
    in between options for named laws; if what is passed is a list of
    these same spacy patterns, these will be added as options."""
    bits: list[dict[str, Any]] = [TH]
    if isinstance(fragments, str):
        bits.extend(lower_words(fragments))
    elif isinstance(fragments, list):
        bits.extend(fragments)
    bits.append({"LOWER": {"IN": options}, "IS_TITLE": True})
    return bits


## DIGITS


p = inflect.engine()

roman_upper = [roman.toRoman(i) for i in range(1, 100)]
a_z_lower = [i for i in string.ascii_lowercase]
pairs = itertools.combinations_with_replacement(a_z_lower, r=2)
aa_zz_lower = [f"{a}{b}" for a, b in pairs]


class DigitLists(Enum):
    HundredDigit = [str(i) for i in range(0, 100)]
    WordHundredDigit = [p.number_to_words(num=i) for i in range(1, 100)]  # type: ignore
    RomanHundredLower = [i.lower() for i in roman_upper]
    RomanHundredUpper = [roman.toRoman(i) for i in range(1, 100)]
    AtoZSingleLower = a_z_lower
    AtoZSingleUpper = [i.upper() for i in a_z_lower]
    AtoZDoubleLower = aa_zz_lower
    AtoZDoubleUpper = [i.upper() for i in aa_zz_lower]

    @classmethod
    def generate_options(cls) -> list[str]:
        options: list[str] = []
        for member in cls:
            options.extend(member.value)  # type: ignore
        return options


HAS_DIGIT = _re(v=".*\\d.*")
"""Any token containing a digit should be used in tandem with an attribute ruler."""

IS_COVERED = _re(v=".*\\(\\w{1,2}\\).*")
"""Any token containing a digit should be used in tandem with an attribute ruler."""

SPECIFIC = _re("(" + "|".join(DigitLists.generate_options()) + ")")
"""Any token matching the options created by DigitLists"""

IS_ROMAN = _re(v="[IXV]+[-\\.][A-Z]{1,2}")
"""Handle combinations like I-A"""

PROV_DIGITS = [SPECIFIC, HAS_DIGIT, IS_COVERED, IS_ROMAN]
