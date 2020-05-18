"""Functions that can be used in *templates_multi*."""
import re
from typing import Tuple
from warnings import warn

from .lang import all_langs


def capitalize(text: str) -> str:
    """Capitalize the first letter only.

        >>> capitalize("alice")
        'Alice'
        >>> capitalize("BOB")
        'BOB'
        >>> capitalize("alice and bob")
        'Alice and bob'
    """
    return f"{text[0].capitalize()}{text[1:]}"


def eval_expr(expr: str) -> str:
    """Eval the given *expr*.

        >>> eval_expr("cat /etc/passwd")  # doctest: +ELLIPSIS
        Traceback (most recent call last):
          File ".../doctest.py", line 1329, in __run
            compileflags, 1), test.globs)
          File "<doctest scripts.user_functions.eval_expr[0]>", line 1, in <module>
          File ".../user_functions.py", line 33, in eval_expr
            raise ValueError(f"Dangerous characters in the expr {expr!r}")
        ValueError: Dangerous characters in the expr 'cat /etc/passwd'
        >>> eval_expr("2 ^ 30")
        '1073741824'
    """
    # Prevent horrors
    # digits, space and operators (+-*^)
    if re.search(r"[^\d\s\*\-\+\^\.\,]+", expr):
        raise ValueError(f"Dangerous characters in the expr {expr!r}")

    # Replace signs
    expr = expr.replace("^", "**")

    return f"{eval(expr)}"


def format_chimy(composition: Tuple[str, ...]) -> str:
    """Format chimy notations.

        >>> format_chimy(["H", "2", "O"])
        'H<sub>2</sub>O'
        >>> format_chimy(["FeCO", "3", ""])
        'FeCO<sub>3</sub>'
    """
    return "".join(f"<sub>{c}</sub>" if c.isdigit() else c for c in composition)


def format_num(number: str, fsep: str, tsep: str) -> str:
    """Format a number using the provided float and thousands separator.

        >>> format_num("1 000 000 000 000", ",", " ")
        '1 000 000 000 000'
        >>> format_num("1000000", ",", " ")
        '1 000 000'
        >>> format_num("1000000", ".", "")
        '1000000'
        >>> format_num("1000000", ".", ",")
        '1,000,000'
        >>> format_num("-1000000", ",", " ")
        '-1 000 000'
        >>> format_num("-1000000", "", "")
        '-1000000'
        >>> format_num("-1000000", ".", ",")
        '-1,000,000'
        >>> format_num("4.54609", "," , " ")
        '4,54609'
        >>> format_num("4.54609", "." , ",")
        '4.54609'
    """
    # Remove superfluous spaces
    number = number.replace(" ", "")

    try:
        # Integer
        res = f"{int(number):,}"
    except ValueError:
        # Float
        res = f"{float(number):,}"

    return res.replace(",", tsep).replace(".", fsep)


def handle_calc(parts: Tuple[str, ...]) -> str:
    """Handle the 'calque' template.
    Source: https://fr.wiktionary.org/wiki/Mod%C3%A8le:calque

        >>> handle_calc("calque|la|fr".split("|"))
        'latin'
        >>> handle_calc("calque|en|fr|mot=to date|sens=à ce jour".split("|"))
        'anglais <i>to date</i> (« à ce jour »)'
        >>> handle_calc("calque|sa|fr|mot=वज्रयान|tr=vajrayāna|sens=véhicule du diamant".split("|"))
        'sanskrit वज्रयान, <i>vajrayāna</i> (« véhicule du diamant »)'
    """
    l10n_src = parts[1]
    l10n_dst = parts[2]
    res = all_langs[l10n_dst][l10n_src]
    if len(parts) == 3:
        return res

    data = {}
    for part in parts[3:]:
        key, value = part.split("=")
        data[key] = value

    if "tr" in data:
        res += f" {data['mot']}, <i>{data['tr']}</i>"
    else:
        res += f" <i>{data['mot']}</i>"
    if "sens" in data:
        res += f" (« {data['sens']} »)"

    return res


def handle_century(parts: Tuple[str, ...], century: str) -> str:
    """Handle different century templates.

        >>> handle_century(["siècle", "XVI"], "siècle")
        'XVI<sup>e</sup> siècle'
        >>> handle_century(["siècle", "XVIII", "XIX"], "century")
        'XVIII<sup>e</sup> century - XIX<sup>e</sup> century'
    """
    return " - ".join(f"{p}<sup>e</sup> {century}" for p in parts[1:])


def handle_etyl(parts: Tuple[str, ...]) -> str:
    """Handle the 'etyl' (etymological language) template.
    Source: https://fr.wiktionary.org/wiki/Mod%C3%A8le:%C3%A9tyl

        >>> handle_etyl("étyl|grc|fr".split("|"))
        'grec ancien'
        >>> handle_etyl("étyl|no|fr|mot=ski".split("|"))
        'norvégien <i>ski</i>'
        >>> handle_etyl("étyl|la|fr|mot=invito|type=verb".split("|"))
        'latin <i>invito</i>'
        >>> handle_etyl("étyl|grc|fr|mot=λόγος|tr=lógos|type=nom|sens=étude".split("|"))
        'grec ancien λόγος, <i>lógos</i> (« étude »)'
        >>> handle_etyl("étyl|grc|fr|λόγος|lógos|étude|type=nom|lien=1".split("|"))
        'grec ancien λόγος, <i>lógos</i> (« étude »)'
    """
    l10n_src = parts[1]
    l10n_dst = parts[2]
    res = all_langs[l10n_dst][l10n_src]
    if len(parts) == 3:
        return res

    data = {}
    for part in parts[3:]:
        if "=" in part:
            key, value = part.split("=")
            data[key] = value
        elif "mot" not in data:
            data["mot"] = part
        elif "tr" not in data:
            data["tr"] = part
        elif "sens" not in data:
            data["sens"] = part

    if "tr" in data:
        res += f" {data['mot']}, <i>{data['tr']}</i>"
    else:
        res += f" <i>{data['mot']}</i>"
    if "sens" in data:
        res += f" (« {data['sens']} »)"

    return res


def handle_name(parts: Tuple[str, ...]) -> str:
    """Handle the 'name' template to display writers/authors or any full name person.
    Source: https://fr.wiktionary.org/wiki/Mod%C3%A8le:nom_w_pc

        >>> handle_name(["nom w pc", "Aldous", "Huxley"])
        "Aldous <span style='font-variant:small-caps'>Huxley</span>"
        >>> handle_name(["nom w pc", "L. L. Zamenhof"])
        'L. L. Zamenhof'
        >>> handle_name(["nom w pc", "Théodore Agrippa d’", "Aubigné"])
        "Théodore Agrippa d’ <span style='font-variant:small-caps'>Aubigné</span>"
        >>> handle_name(["nom w pc", "Théodore Agrippa d’", "Aubigné", "'=oui"])
        "Théodore Agrippa d’<span style='font-variant:small-caps'>Aubigné</span>"
    """
    res = parts[1]
    if len(parts) > 2:
        if parts[-1] != "'=oui":
            res += " "
        res += f"<span style='font-variant:small-caps'>{parts[2]}</span>"
    else:
        warn(f"Malformed template in the Wikicode (parts={parts})")
    return res


def handle_sport(tpl: str, parts: Tuple[str, ...]) -> str:
    """Handle the 'sport' template.

        >>> handle_sport("sport", [""])
        '<i>(Sport)</i>'
        >>> handle_sport("sport", ["sport", "fr", "collectif"])
        '<i>(Sport collectif)</i>'
    """
    res = f"<i>({capitalize(tpl)}"
    if len(parts) >= 3:
        # {{sport|fr|collectif}}
        res += f" {parts[2]}"
    res += ")</i>"
    return res


def handle_term(text: str) -> str:
    """Format a term.

        >>> handle_term("")
        ''
        >>> handle_term("foo")
        '<i>(Foo)</i>'
        >>> handle_term("Foo")
        '<i>(Foo)</i>'
        >>> handle_term("<i>(Foo)</i>")
        '<i>(Foo)</i>'
    """
    if text.startswith("<i>("):
        return text
    elif not text:
        return ""
    return f"<i>({capitalize(text)})</i>"


def handle_unit(parts: Tuple[str, ...]) -> str:
    """Pretty format a 'unit'.

        >>> handle_unit(["92", "%"])
        '92%'
    """
    return "".join(parts)


def int_to_roman(number: int) -> str:
    """
    Convert an integer to a Roman numeral.
    Source: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html

        >>> int_to_roman(12)
        'XII'
        >>> int_to_roman(19)
        'XIX'
        >>> int_to_roman(2020)
        'MMXX'
    """

    # if not 0 < number < 4000:
    #     raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    result = []
    for i in range(len(ints)):
        count = int(number / ints[i])
        result.append(nums[i] * count)
        number -= ints[i] * count
    return "".join(result)


__all__ = (
    "capitalize",
    "eval_expr",
    "format_chimy",
    "format_num",
    "handle_calc",
    "handle_century",
    "handle_etyl",
    "handle_name",
    "handle_sport",
    "handle_term",
    "handle_unit",
    "int_to_roman",
)
