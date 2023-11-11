import io
import re
from pathlib import Path
from typing import Any

import jsonlines
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated


def check_titlecased_word(v: str) -> str:
    assert all(bit.istitle for bit in v.split("-")), f"{v} is not titlecased."
    return v


TitledString = Annotated[str, AfterValidator(check_titlecased_word)]

# PATTERN FILES

camel_case_pattern = re.compile(
    r".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)"
)


def convert_from_camel_case(text: str):
    """For filenames that are in camelCaseFormatting."""
    return [m.group(0) for m in camel_case_pattern.finditer(text)]


def create_pattern_file(file: Path, patterns: list[dict]) -> Path:
    """See generally:

    1. https://spacy.io/usage/rule-based-matching#entityruler-files
    2. https://spacy.io/usage/rule-based-matching#spanruler-files
    """
    fp = io.BytesIO()
    with jsonlines.Writer(fp) as writer:
        for pattern in patterns:
            writer.write(pattern)
    file.unlink(missing_ok=True)
    file.write_bytes(fp.getbuffer())
    return file


def create_pattern_obj(
    nodes: list[dict[str, Any]], id: str | None = None, label: str | None = None
) -> dict[str, Any]:
    pattern = {}
    if id:
        pattern["id"] = id
    if label:
        pattern["LABEL"] = label
    pattern["PATTERN"] = nodes  # type: ignore
    return pattern


# PATTERN NODES


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


def make_special_rule(texts: list[str]):
    """Add a period after every text item in `texts`, to consider each a single token.
    These patterns can be used as a special rule in creating a custom tokenizer."""
    return {f"{t}.": [{"ORTH": f"{t}."}] for t in texts if not t.endswith(".")}


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
provisions/serials to be merged later"""

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


# CASE VARIATION

CASED_STYLE = (None, "lower", "upper")
