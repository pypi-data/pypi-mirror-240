import spacy  # type: ignore
from spacy.tokens import Doc

from .attrs import set_attribute_ruler
from .ents import set_entity_ruler
from .tokens import set_tokenizer


def lextok(
    model: str = "en_core_web_sm",
    merge_entities: bool = False,
) -> spacy.language.Language:
    """Override tokenizer default, use attribute + entity rulers.

    Default pipeline names:

    1. `attribute_ruler`
    2. `entity_ruler`
    """

    nlp = spacy.load(model)
    nlp.tokenizer = set_tokenizer(nlp)
    nlp = set_attribute_ruler(nlp)
    nlp = set_entity_ruler(nlp)
    if merge_entities:
        nlp.add_pipe("merge_entities", after="entity_ruler")
    return nlp


def pretest_entities(
    raw_nlp: spacy.language.Language,
    passages: list[str],
    test_ent_id: str = "XXX",
    patterns: list[list[dict]] | None = None,
) -> list[list[str]]:
    """All `passages` should result in a matching pattern
    from the list of possible `patterns`"""
    matches: list[list[str]] = []
    if not passages:
        return matches
    try:
        raw_nlp.remove_pipe("entity_ruler")
    except ValueError:
        pass

    if patterns:
        ruler = raw_nlp.add_pipe(
            "entity_ruler",
            config={"overwrite_ents": True},
            validate=True,
        )
        with raw_nlp.select_pipes(enable="tagger"):
            for pattern in patterns:
                ruler.add_patterns([{"id": test_ent_id, "label": "test", "pattern": pattern}])  # type: ignore

    for passage in passages:
        doc: Doc = raw_nlp(passage)  # type: ignore
        found = False
        passage_matches: list[str] = []
        for ent in doc.ents:
            if ent.ent_id_ == test_ent_id:
                found = True
                passage_matches.append(ent.text)
        if not found:
            raise Exception(f"Undetected {id}: {passage}")
        matches.append(passage_matches)

    return matches
