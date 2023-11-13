import spacy  # type: ignore
from spacy.language import Language
from spacy.tokens import Doc, Span
from spacy.util import filter_spans

from .attrs import set_attribute_ruler
from .rules import (
    BASIC_ENTITY_RULES,
    BASIC_SPAN_RULES,
    EXT_ENTS,
    EXT_SPANS,
    Label,
    Rule,
    uncamel,
)
from .spans import create_custom_entities, create_custom_spans
from .tokens import set_tokenizer


def lextok(
    model: str = "en_core_web_sm",
    finalize_entities: bool = False,
    entity_rules: list[Rule] = BASIC_ENTITY_RULES,
    span_rules: list[Rule] = BASIC_SPAN_RULES,
) -> Language:
    """Modifies the `model`'s tokens based on a a custom tokenizer and attribute ruler
    then allows the inclusion of extendible `entity_rules` and `span_rules` to modify the `Doc`
    instance.

    Args:
        model (str, optional): Spacy language model. Defaults to "en_core_web_sm".
        finalize_entities (bool, optional): Whether to consider consecutive entities as a single token. Defaults to False.
        entity_rules (list[Rule], optional): List of generic Pydantic models with serialization. Defaults to BASIC_ENTITY_RULES.
        span_rules (list[Rule], optional): List of generic Pydantic models with serialization. Defaults to BASIC_SPAN_RULES.

    Returns:
        Language: A customized rule-based spacy model.
    """
    nlp = spacy.load(model)
    nlp.tokenizer = set_tokenizer(nlp)
    nlp = set_attribute_ruler(nlp)
    create_custom_entities(nlp, rules=entity_rules, pipename="entity_ruler")
    if finalize_entities:
        nlp.add_pipe("merge_entities", after="entity_ruler")
        nlp.add_pipe("provision_num_merger", after="merge_entities")
        create_custom_spans(nlp, rules=span_rules)
        nlp.add_pipe("detector", last=True)
    return nlp


@Language.component("provision_num_merger")
def merge_provisions(doc: Doc) -> Doc:
    """All ProvisionNum entities
    (that have previously been merged together) will be merged a single
    ProvisionNum token / entity."""
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
                Span(doc=doc, start=pair[0], end=pair[1], label="ProvisionNum")
            )
    if new_ents:
        doc.ents = filter_spans(new_ents + list(doc.ents))
    return doc


@Language.factory("detector")
class DetectorComponent:
    def __init__(self, nlp, name):
        """Initializes each doc._.<value> to be an empty list."""
        for label in EXT_ENTS + EXT_SPANS:
            Doc.set_extension(label.snakecase, default=[])

    def __call__(self, doc):
        """Assigns each doc._.<value> dynamically."""
        # `EXT_ENTS` refers to those custom attributes that refer to the document entity texts
        for label in EXT_ENTS:
            doc._.set(label.snakecase, label.get_entities(doc))

        # `EXT_SPANS` refers to document span ruler patterns.
        for label in EXT_SPANS:
            doc._.set(label.snakecase, label.get_spans(doc))
        return doc
