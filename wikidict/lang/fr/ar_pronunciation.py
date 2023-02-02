"""
manual conversion of Module:ar-pronunciation from
https://fr.wiktionary.org/wiki/Module:ar-pronunciation

Current version: 26 février 2020 22:21
    https://fr.wiktionary.org/w/index.php?title=Module:ar-pronunciation&oldid=27486992
"""

import re

correspondences = {
    "ʾ": "ʔ",
    "ṯ": "θ",
    "j": "d͡ʒ",
    "ḥ": "ħ",
    "ḵ": "x",
    "ḏ": "ð",
    "š": "ʃ",
    "ṣ": "sˁ",
    "ḍ": "dˁ",
    "ṭ": "tˁ",
    "ẓ": "ðˁ",
    "ž": "ʒ",
    "ʿ": "ʕ",
    "ḡ": "ɣ",
    "ḷ": "ɫ",
    "ū": "uː",
    "ī": "iː",
    "ā": "aː",
    "y": "j",
    "g": "ɡ",
    "ē": "eː",
    "ō": "oː",
    "": "",
}

vowels = "aāeēiīoōuū"
vowel = f"[{vowels}]"
long_vowels = "āēīōū"
long_vowel = f"[{long_vowels}]"
consonant = f"[^{vowels}. -]"
syllabify_pattern = f"({vowel})({consonant}?)({consonant}?)({vowel})"
tie = "‿"
closed_syllable_shortening_pattern = f"({long_vowel})({tie})({consonant})"


def syllabify(text: str) -> str:
    text = re.sub(rf"-({consonant})-({consonant})", r"\1.\2", text)
    text = re.sub(r"-", ".", text)
    # add syllable break

    def my_lambda(a: str, b: str, c: str, d: str) -> str:
        if not c and b:
            c = b
            b = ""
        return f"{a}{b}.{c}{d}"

    for _ in range(2):
        text = re.sub(
            syllabify_pattern,
            lambda m: my_lambda(m.group(1), m.group(2), m.group(3), m.group(4)),
            text,
        )

    text = re.sub(rf"({vowel}) ({consonant})\.*({consonant})", rf"\1{tie}\2.\3", text)

    return text


def closed_syllable_shortening(text: str) -> str:
    shorten = {
        "ā": "a",
        "ē": "e",
        "ī": "i",
        "ō": "o",
        "ū": "u",
    }
    return re.sub(
        closed_syllable_shortening_pattern,
        lambda m: shorten[m.group(1)] + m.group(2) + m.group(3),
        text,
    )


def toIPA(arabic: str = "", tr: str = "") -> str:
    """
    >>> toIPA(tr="tilivizyōn")
    'ti.li.viz.joːn'
    >>> toIPA(tr="ʾinglīziyy")
    'ʔinɡliː.zijj'

    >>> toIPA(tr="allāh")
    'aɫ.ɫaːh'
    >>> toIPA(tr="ʿabdu llāh")
    'ʕab.du‿ɫ.ɫaːh'
    >>> toIPA(tr="lillāh")
    'lil.laːh'
    >>> toIPA(tr="ḏū l-qarnayn")
    'ðu‿l.qar.najn'


    >>> toIPA(tr="yawmu l-iṯnayni")
    'jaw.mu l.iθ.naj.ni'

    >>> toIPA("طَبَّ")
    'tˁab.ba'
    >>> toIPA("رُوسِيَا")
    'ruː.si.jaː'
    >>> toIPA("أَنْتَ")
    'ʔan.ta'
    >>> toIPA("ذٰلِكَ")
    'ðaː.li.ka'
    >>> toIPA("صَغِير")
    'sˁa.ɣiːr'
    >>> toIPA("إِصْبَع")
    'ʔisˁ.baʕ'
    >>> toIPA("عَلَى")
    'ʕa.laː'
    >>> toIPA("جَزِيرَة")
    'd͡ʒa.ziː.ra'
    >>> toIPA("أَرْبَعَة")
    'ʔar.ba.ʕa'
    >>> toIPA("حُبّ")
    'ħubb'
    >>> toIPA("عَرَبِيّ")
    'ʕa.ra.bijj'
    >>> toIPA("خَاصّ")
    'xaːsˁsˁ'
    >>> toIPA("خَاصَّة")
    'xaːsˁ.sˁa'

    lasconic: this one is different in fr and en implementation
    we follow french implementation
    >>> toIPA("يَوْمُ ٱلِٱثْنَيْنِ")
    'jaw.mu l.iθ.naj.ni'
    >>> toIPA("تُدُووِلَ")
    'tu.duː.wi.la'
    >>> toIPA("اللّٰه")
    'aɫ.ɫaːh'
    >>> toIPA("عَبْدُ اللّٰه")
    'ʕab.du‿ɫ.ɫaːh'
    >>> toIPA("لِلّٰه")
    'lil.laːh'
    >>> toIPA("الْمَمْلَكَة الْعَرَبِيَّة السُّعُودِيَّة")
    'al.mam.la.ka‿l.ʕa.ra.bij.ja‿s.su.ʕuː.dij.ja'
    >>> toIPA("مَعَ اَلسَّلَامَة")
    'ma.ʕa‿s.sa.laː.ma'
    >>> toIPA("لٰكِنَّ الرَّئِيسَ كَانَ أَذْكَى مِمَّا تَوَقَّعَ النَّاسُ")
    'laː.kin.na‿r.ra.ʔiː.sa kaː.na ʔað.kaː mim.maː ta.waq.qa.ʕa‿n.naː.su'
    >>> toIPA("بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيمِ")
    'bis.mi‿l.laː.hi‿r.raħ.maː.ni‿r.ra.ħiː.mi'
    >>> toIPA("إِنْ شَاءَ ٱللَٰهُ")
    'ʔin ʃaː.ʔa‿ɫ.ɫaː.hu'
    >>> toIPA("بِٱلْهَنَاءِ وَٱلشِّفَاء")
    'bil.ha.naː.ʔi waʃ.ʃi.faːʔ'
    >>> toIPA("فِي الْبَيْت")
    'fi‿l.bajt'
    >>> toIPA("مَا ٱسْمُك")
    'ma‿s.muk'
    >>> toIPA("ذُو الْقَرْنَيْن")
    'ðu‿l.qar.najn'
    >>> toIPA("إِلَّا الله")
    'ʔil.la‿ɫ.ɫaːh'
    >>> toIPA("فِي ٱتِّحَادِنَا")
    'fi‿t.ti.ħaː.di.naː'
    >>> toIPA("فِي الله")
    'fi‿l.laːh'

    """
    translit = ""
    if tr:
        translit = tr
    elif arabic:
        from .ar_translit import tr as transliterate

        translit = transliterate(arabic)
        if not translit:
            return ""
    else:
        return ""

    translit = translit.replace("llāh", "ḷḷāh")
    translit = re.sub("([iī] ?)ḷḷ", "\\1ll", translit)
    # Remove the transliterations of any tāʾ marbūṭa not marked with a sukūn.
    translit = translit.replace("(t)", "")
    # Prodelision after tāʾ marbūṭa
    translit = re.sub(f"({vowel}) {vowel}", "\\1 ", translit)
    translit = syllabify(translit)
    translit = closed_syllable_shortening(translit)
    for k, v in correspondences.items():
        translit = translit.replace(k, v)
    translit = translit.replace("-", "")
    return translit
