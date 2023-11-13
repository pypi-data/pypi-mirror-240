import spacy
from spacy.lang.char_classes import (
    ALPHA,
    ALPHA_LOWER,
    ALPHA_UPPER,
    CONCAT_QUOTES,
    LIST_ELLIPSES,
    LIST_ICONS,
)
from spacy.tokenizer import Tokenizer  # type: ignore

from .rules import Abbv, DocketNum, Prov, StatuteNum

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


def make_special_rule(texts: list[str]):
    """Add a period after every text item in `texts`, to consider each a single token.
    These patterns can be used as a special rule in creating a custom tokenizer."""
    return {f"{t}.": [{"ORTH": f"{t}."}] for t in texts if not t.endswith(".")}


def create_special_rules():
    a = {
        k: v
        for member in DocketNum
        if member.value.initials
        for k, v in member.value.initials.as_token.items()
    }

    b = {
        k: v
        for member in StatuteNum
        if member.value.initials
        for k, v in member.value.initials.as_token.items()
    }

    c = {
        f"{bit}.": [{"ORTH": f"{bit}."}]
        for style in (None, "lower", "upper")
        for bit in Abbv.set_abbvs(cased=style)
    }

    d = {
        f"{bit}.": [{"ORTH": f"{bit}."}]
        for style in (None, "lower", "upper")
        for bit in Prov.set_abbvs(cased=style)
    }

    e = make_special_rule("vs v s et al etc Ll Pp PP P.P R.P H.B S.B a.k.a".split())
    return a | b | c | d | e


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
