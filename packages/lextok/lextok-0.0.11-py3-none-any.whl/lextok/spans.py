import spacy

from .rules import Rule


def create_custom_entities(
    nlp: spacy.language.Language, rules: list[Rule], pipename: str = "entity_ruler"
):
    ents = nlp.add_pipe(
        factory_name="entity_ruler",
        name=pipename,
        config={"overwrite_ents": True, "validate": True},
        validate=True,
    )
    for rule in rules:
        ents.add_patterns(rule.model_dump())  # type: ignore
    return nlp


def create_custom_spans(nlp: spacy.language.Language, rules: list[Rule]):
    for rule in rules:
        spans = nlp.add_pipe(
            "span_ruler",
            name=f"ruler{rule.label.name}",
            config={"spans_key": rule.label.name, "validate": True},
            validate=True,
        )
        spans.add_patterns(rule.model_dump())  # type: ignore
    return nlp
