from typing import Any, NamedTuple


class Duo(NamedTuple):
    """Given two letters, create possible patterns using uppercase text."""

    a: str
    b: str

    @property
    def x(self):
        return self.a.upper()

    @property
    def y(self):
        return self.b.upper()

    @property
    def as_token(self) -> dict[str, list[dict[str, str]]]:
        """Used to create special rules for custom tokenizer."""
        return {f"{self.x}.{self.y}.": [{"ORTH": f"{self.x}.{self.y}."}]}

    @property
    def v1(self) -> list[dict[str, str]]:
        # R . A .
        return [{"ORTH": self.x}, {"ORTH": "."}, {"ORTH": self.y}, {"ORTH": "."}]

    @property
    def v2(self) -> list[dict[str, str]]:
        return [{"ORTH": f"{self.x}."}, {"ORTH": f"{self.y}."}]  # R. A.

    @property
    def v3(self) -> list[dict[str, str]]:
        return [{"ORTH": f"{self.x}.{self.y}."}]  # R.A.

    @property
    def v4(self) -> list[dict[str, str]]:
        return [{"ORTH": f"{self.x}{self.y}"}]  # RA

    @property
    def patterns(self) -> list[list[dict[str, str]]]:
        return [self.v1, self.v2, self.v3, self.v4]

    def add_to_each_pattern(self, terminators: list[dict[str, Any]]):
        for p in self.patterns:
            yield p + terminators
