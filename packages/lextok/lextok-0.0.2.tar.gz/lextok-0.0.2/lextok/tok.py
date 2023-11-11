import spacy  # type: ignore
from spacy.lang.char_classes import (
    ALPHA,
    ALPHA_LOWER,
    ALPHA_UPPER,
    CONCAT_QUOTES,
    LIST_ELLIPSES,
    LIST_ICONS,
)
from spacy.tokenizer import Tokenizer  # type: ignore

from .attrs import set_attribute_ruler
from .components import (
    Abbv,
    DocketNo,
    Prov,
    Provision,
    StatuteNo,
    make_special_rule,
)


def create_special_rules():
    a = DocketNo.make_special_rules()
    b = StatuteNo.make_special_rules()
    c = Abbv.make_special_rules()
    d = Prov.make_special_rules()
    e = make_special_rule("vs v s et al etc Ll Pp PP P.P R.P H.B S.B a.k.a".split())
    return a | b | c | d | e


# Remove hyphen '-' as infix, see https://spacy.io/usage/linguistic-features#native-tokenizer-additions
INFIXES_OVERRIDE = (
    LIST_ELLIPSES
    + LIST_ICONS
    + [
        r"(?<=[0-9])[+\\-\\*^](?=[0-9-])",
        r"(?<=[{al}{q}])\\.(?=[{au}{q}])".format(
            al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
        ),
        r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
        # ✅ Commented out regex that splits on hyphens between letters:
        # r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
        r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
    ]
)


def create_prefix_list(nlp: spacy.language.Language):
    pre = list(nlp.Defaults.prefixes)  # type: ignore
    pre.remove("\\(")
    pre.remove("\\[")
    pre.append("\\((?!\\w+)")  # only use prefix ( if not followed by a single word
    pre.append("\\[(?!\\w+)")  # only use prefix [ if not followed by a single word
    return pre


def create_suffix_list(nlp: spacy.language.Language):
    sfx = list(nlp.Defaults.suffixes)  # type: ignore
    sfx.remove("\\)")
    sfx.remove("\\]")
    for i in ["\\s", "\\.", ",", "!"]:
        sfx.append(f"\\)(?={i})")  # only use suffix ) if followed by allowed char
        sfx.append(f"\\](?={i})")  # only use prefix ] if followed by allowed char
    return sfx


def set_tokenizer(nlp: spacy.language.Language):
    infix_re = spacy.util.compile_infix_regex(INFIXES_OVERRIDE)  # type: ignore
    suffix_re = spacy.util.compile_suffix_regex(create_suffix_list(nlp))
    prefix_re = spacy.util.compile_prefix_regex(create_prefix_list(nlp))
    return Tokenizer(
        nlp.vocab,
        rules=create_special_rules(),
        prefix_search=prefix_re.search,
        suffix_search=suffix_re.search,
        infix_finditer=infix_re.finditer,
    )


def lextok(model: str = "en_core_web_sm") -> spacy.language.Language:
    """Override tokenizer default and adjust numeric tokens."""

    nlp = spacy.load(model)
    nlp.tokenizer = set_tokenizer(nlp)
    nlp = set_attribute_ruler(nlp)
    return nlp
