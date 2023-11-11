import itertools
from enum import Enum
from typing import Any

from ._pattern import VS, _re


class GenericParty(Enum):
    ent = {"ENT_TYPE": {"IN": ["ORG", "PERSON"]}, "OP": "+"}
    pos = {"POS": {"IN": ["PROPN", "PUNCT"]}, "OP": "{1,4}"}
    title = {"IS_TITLE": True, "OP": "{1,4}"}
    upper = {"IS_UPPER": True, "OP": "{1,4}"}

    @classmethod
    def permute_patterns(cls):
        minimum = {"LENGTH": {">=": 2}, "IS_PUNCT": False}
        possibilities = (member.value | minimum for member in cls)
        permutations = itertools.permutations(possibilities, 2)
        patterns = [cls._pair(first, second) for first, second in permutations]
        return patterns

    @staticmethod
    def _pair(first_party: dict[str, Any], second_party: dict[str, Any]):
        extras = """. ,
                    et al. et al of the
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
