import spacy
from spacy.tokens import Doc


def pretest_entities(
    raw_nlp: spacy.language.Language,
    patterns: list[list[dict]],
    passages: list[str],
    test_ent_id="XXX",
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

    ruler = raw_nlp.add_pipe(
        "entity_ruler",
        config={"overwrite_ents": True},
        validate=True,
    )
    with raw_nlp.select_pipes(enable="tagger"):
        for pattern in patterns:
            ruler.add_patterns([{"id": test_ent_id, "label": "test", "pattern": pattern}])  # type: ignore

    for passage in passages:
        doc: Doc = raw_nlp(passage)
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
