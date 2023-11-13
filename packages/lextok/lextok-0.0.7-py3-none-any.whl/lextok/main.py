import spacy  # type: ignore
from spacy.language import Language
from spacy.tokens import Doc, Span
from spacy.util import filter_spans

from .attrs import set_attribute_ruler
from .rules import ENTS, SPANS
from .tokens import set_tokenizer


def lextok(model: str = "en_core_web_sm", merge_entities: bool = False) -> Language:
    """Override tokenizer default, use attribute + entity rulers.

    Default pipeline names:

    1. `attribute_ruler` (custom)
    2. `entity_ruler` (custom)

    Includes:

    1. `merge_entities`, e.g. all tokens of a given `Doc` object
    that match the `ProvisionNum` pattern will be merged as a single token.
    2. `provision_num_merger` (custom), e.g. all ProvisionNum entities
    (that have previously been merged together) will be merged a single
    ProvisionNum token / entity.
    3. `span_ruler` to relate entities together
    """

    # Affect tokens
    nlp = spacy.load(model)
    nlp.tokenizer = set_tokenizer(nlp)
    nlp = set_attribute_ruler(nlp)

    # Create custom entities
    ents = nlp.add_pipe(
        "entity_ruler",
        config={"overwrite_ents": True, "validate": True},
        validate=True,
    )
    for ent in ENTS:
        ents.add_patterns(ent.model_dump())  # type: ignore

    if merge_entities:
        nlp.add_pipe("merge_entities", after="entity_ruler")
        nlp.add_pipe("provision_num_merger", after="merge_entities")

    # Combine spans
    for el in SPANS:
        spans = nlp.add_pipe(
            "span_ruler",
            name=f"ruler{el.label}",
            config={"spans_key": el.label, "validate": True},
            validate=True,
        )
        spans.add_patterns(el.model_dump())  # type: ignore

    nlp.add_pipe("detector")
    return nlp


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
            return [ent.text for ent in doc.ents if ent.label_ == label]

        def _unspan(doc: Doc, key: str) -> list[str]:
            return [span.text for span in filter_spans(doc.spans[key])]

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
