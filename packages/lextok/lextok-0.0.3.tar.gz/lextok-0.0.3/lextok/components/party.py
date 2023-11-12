import itertools
from enum import Enum
from typing import Any

from ._pattern import COURT, VS, _orth_in, _re, name_court, titled_words
from .abbv import ORG_SUFFIXES


class Court(Enum):
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


class Party(Enum):
    ent = {
        "ENT_TYPE": {"IN": ["ORG", "PERSON"]},
        "OP": "+",
        "ORTH": {"NOT_IN": [";"]},
    }
    pos = {
        "POS": {"IN": ["PROPN", "PUNCT", "ADP"]},
        "OP": "+",
        "ORTH": {"NOT_IN": [";"]},
    }
    upper = {
        "IS_UPPER": True,
        "OP": "{1,6}",
        "ORTH": {"NOT_IN": [";"]},
    }
    title = {
        "IS_TITLE": True,
        "OP": "{1,6}",
        "ORTH": {"NOT_IN": [";"]},
    }

    @classmethod
    def get_patterns(cls):
        return itertools.permutations((m.value for m in cls), 2)

    @staticmethod
    def _pair(first_party: dict[str, Any], second_party: dict[str, Any]):
        extras = " ".join(set(op for s in ORG_SUFFIXES for op in s.value.options))
        extras += " . , et al. et al the Jr Jr. Sr Sr. III IV Partnership Dev't"
        parenthesized = _re("\\([A-Z]+\\)") | {"OP": "?"}
        extra_suffix = _orth_in(extras.split()) | {"OP": "*"}
        a = [first_party, parenthesized, extra_suffix]
        b = [second_party, parenthesized, extra_suffix]
        return a + [VS] + b

    @classmethod
    def permute_patterns(cls):
        return [cls._pair(first, second) for first, second in cls.get_patterns()]
