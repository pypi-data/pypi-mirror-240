from enum import Enum

from ._pattern import CM, OF


class DocNumSeriesConstructor(Enum):
    of = OF
    comma = CM
    indicator = {"LOWER": {"IN": ["s.", "series"]}}
    year = {
        "IS_DIGIT": True,
        "LENGTH": 4,
        "TEXT": {"REGEX": "^(194\\d|195\\d|196\\d|197\\d|198\\d|199\\d|20\\d{2})$"},
    }

    @classmethod
    def get_patterns(cls) -> list:
        return [b.value for b in [cls.comma, cls.indicator, cls.of, cls.year]]
