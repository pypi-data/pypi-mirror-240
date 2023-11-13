import spacy  # type: ignore
from spacy.language import Language
from spacy.tokens import Doc, Span
from spacy.util import filter_spans

from .attrs import set_attribute_ruler
from .rules import BASIC_ENTITY_RULES, BASIC_SPAN_RULES, Rule
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
        Doc.set_extension("case_names", default=[])
        Doc.set_extension("provision_nums", default=[])
        Doc.set_extension("statute_nums", default=[])
        Doc.set_extension("docket_nums", default=[])
        Doc.set_extension("report_nums", default=[])
        Doc.set_extension("serial_nums", default=[])
        Doc.set_extension("stats", default=[])
        Doc.set_extension("cites", default=[])
        Doc.set_extension("sers", default=[])

    def __call__(self, doc):
        def _unent(doc: Doc, label: str) -> list[str]:
            return [ent.text.strip("*, ") for ent in doc.ents if ent.label_ == label]

        def _unspan(doc: Doc, key: str) -> list[str]:
            return [span.text.strip("*, ") for span in filter_spans(doc.spans[key])]

        # entity detection
        doc._.case_names = _unent(doc, "CaseName")
        doc._.provision_nums = _unent(doc, "ProvisionNum")
        doc._.statute_nums = _unent(doc, "StatuteNum")
        doc._.docket_nums = _unent(doc, "DocketNum")
        doc._.report_nums = _unent(doc, "ReporterNum")
        doc._.serial_nums = _unent(doc, "SerialNum")

        # span detection
        doc._.stats = _unspan(doc, "StatutoryProvision")
        doc._.cites = _unspan(doc, "DecisionCitation")
        doc._.sers = _unspan(doc, "SerialDocument")

        return doc
