import spacy  # type: ignore
from spacy.language import Language
from spacy.tokens import Doc, Span
from spacy.util import filter_spans

from .attrs import set_attribute_ruler
from .ents import set_entity_ruler
from .tokens import set_tokenizer


@Language.component("provision_num_merger")
def merge_provisions(doc: Doc) -> Doc:
    """Multiple consecutive `ProvisionNum` entities combined into single `ProvisionNum`."""
    pairs = [(e.start, e.end) for e in doc.ents if e.label_ == "ProvisionNum"]
    pair = None
    new_ents = []
    for ent in doc.ents:
        if ent.label_ == "ProvisionNum":
            s = ent.start
            if pair and s == pair[1]:
                s = pair[0]
            pair = (s, ent.end)
        if pair and pair not in pairs:
            new_ents.append(
                Span(
                    doc=doc,
                    start=pair[0],
                    end=pair[1],
                    label="ProvisionNum",
                )
            )
    if new_ents:
        doc.ents = filter_spans(new_ents + list(doc.ents))
    return doc


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
        nlp.add_pipe("provision_num_merger", after="merge_entities")
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
