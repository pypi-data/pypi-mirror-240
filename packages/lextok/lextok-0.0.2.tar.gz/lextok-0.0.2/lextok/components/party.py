import itertools
from enum import Enum
from typing import Any

from ._pattern import COURT, VS, _re, name_court, titled_words


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
    ent = {"ENT_TYPE": {"IN": ["ORG", "PERSON"]}, "OP": "+"}
    pos = {"POS": {"IN": ["PROPN", "PUNCT"]}, "OP": "{1,6}"}
    title = {"IS_TITLE": True, "OP": "{1,6}"}
    upper = {"IS_UPPER": True, "OP": "{1,6}"}

    @classmethod
    def get_patterns(cls):
        minimum = {"LENGTH": {">=": 2}, "IS_PUNCT": False}
        possibilities = (member.value | minimum for member in cls)
        return itertools.permutations(possibilities, 2)

    @classmethod
    def permute_patterns(cls):
        return [cls._pair(first, second) for first, second in cls.get_patterns()]

    @staticmethod
    def _pair(first_party: dict[str, Any], second_party: dict[str, Any]):
        extras = """. ,
                    et al. et al the
                    Jr Jr. Sr Sr. III IV
                    Inc Inc. Incorporated
                    Phil Phil. Phils Phils. Philippines
                    Co Co. Company
                    Corp Corp. Corporation
                    Ltd Ltd. Limited
                    Partnership Dev't"""
        parenthesized_abbreviation = _re("(\\(|\\[)[A-Z]+(\\)|\\])") | {"OP": "?"}
        extraneous_detail = {"ORTH": {"IN": extras.split()}, "OP": "*"}
        a = [first_party, parenthesized_abbreviation, extraneous_detail]
        b = [second_party, parenthesized_abbreviation, extraneous_detail]
        return a + [VS] + b
