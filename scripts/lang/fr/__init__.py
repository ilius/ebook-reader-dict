"""French language."""

# Titre des sections qui sont intéressantes à analyser.
# https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_des_sections_de_types_de_mots
patterns = (
    "{{S|adjectif|fr}",
    "{{S|adjectif|fr|",
    "{{S|adjectif démonstratif|fr}",
    "{{S|adjectif démonstratif|fr|",
    "{{S|adjectif exclamatif|fr}",
    "{{S|adjectif exclamatif|fr|",
    "{{S|adjectif indéfini|fr}",
    "{{S|adjectif indéfini|fr|",
    "{{S|adjectif interrogatif|fr}",
    "{{S|adjectif interrogatif|fr|",
    "{{S|adjectif numéral|fr}",
    "{{S|adjectif numéral|fr|",
    "{{S|adjectif possessif|fr}",
    "{{S|adjectif possessif|fr|",
    "{{S|adjectif relatif|fr}",
    "{{S|adjectif relatif|fr|",
    "{{S|adverbe|fr}",
    "{{S|adverbe|fr|",
    "{{S|adverbe indéfini|fr|",
    "{{S|adverbe indéfini|fr}",
    "{{S|adverbe interrogatif|fr|",
    "{{S|adverbe interrogatif|fr}",
    "{{S|adverbe pronominal|fr|",
    "{{S|adverbe pronominal|fr}",
    "{{S|adverbe relatif|fr|",
    "{{S|adverbe relatif|fr}",
    "{{S|adverbe|conv}",
    "{{S|adverbe|fr}",
    "{{S|article|fr}",
    "{{S|article|fr|",
    "{{S|article défini|fr}",
    "{{S|article défini|fr|",
    "{{S|article indéfini|fr}",
    "{{S|article indéfini|fr|",
    "{{S|article partitif|fr}",
    "{{S|article partitif|fr|",
    "{{S|circonfixe|fr}",
    "{{S|circonfixe|fr|",
    "{{S|classificateur|fr}",
    "{{S|classificateur|fr|",
    "{{S|conjonction|fr}",
    "{{S|conjonction|fr|",
    "{{S|conjonction de coordination|fr}",
    "{{S|conjonction de coordination|fr|",
    "{{S|copule|fr}",
    "{{S|copule|fr|",
    "{{S|déterminant|fr}",
    "{{S|déterminant|fr|",
    "{{S|enclitique|fr}",
    "{{S|enclitique|fr|",
    "{{S|gismu|fr}",
    "{{S|gismu|fr|",
    "{{S|infixe|fr}",
    "{{S|infixe|fr|",
    "{{S|interfixe|fr}",
    "{{S|interfixe|fr|",
    "{{S|interjection|fr}",
    "{{S|interjection|fr|",
    "{{S|lettre|fr}",
    "{{S|lettre|fr|",
    "{{S|locution|fr}",
    "{{S|locution|fr|",
    "{{S|locution-phrase|fr}",
    "{{S|locution-phrase|fr|",
    "{{S|nom|fr}",
    "{{S|nom|fr|",
    "{{S|nom|conv}",
    "{{S|nom commun|fr}",
    "{{S|nom commun|fr|",
    # "{{S|nom de famille|fr}",
    # "{{S|nom de famille|fr|",
    # "{{S|nom propre|fr}",
    # "{{S|nom propre|fr|",
    "{{S|nom scientifique|fr}",
    "{{S|nom scientifique|fr|",
    "{{S|numéral|conv}",
    "{{S|onomatopée|fr}",
    "{{S|onomatopée|fr|",
    "{{S|particule|fr}",
    "{{S|particule|fr|",
    "{{S|particule numérale|fr}",
    "{{S|particule numérale|fr|",
    # "{{S|patronyme|fr}",
    # "{{S|patronyme|fr|",
    "{{S|postposition|fr}",
    "{{S|postposition|fr|",
    "{{S|proclitique|fr}",
    "{{S|proclitique|fr|",
    "{{S|pronom|fr}",
    "{{S|pronom|fr|",
    "{{S|pronom démonstratif|fr}",
    "{{S|pronom démonstratif|fr|",
    "{{S|pronom indéfini|fr}",
    "{{S|pronom indéfini|fr|",
    "{{S|pronom interrogatif|fr}",
    "{{S|pronom interrogatif|fr|",
    "{{S|pronom personnel|fr}",
    "{{S|pronom personnel|fr|",
    "{{S|pronom relatif|fr}",
    "{{S|pronom relatif|fr|",
    "{{S|pronom-adjectif|fr}",
    "{{S|pronom-adjectif|fr|",
    "{{S|proverbe|fr}",
    "{{S|proverbe|fr|",
    "{{S|pré-nom|fr}",
    "{{S|pré-nom|fr|",
    "{{S|pré-verbe|fr}",
    "{{S|pré-verbe|fr|",
    "{{S|préfixe|fr}",
    "{{S|préfixe|fr|",
    # "{{S|prénom|fr}",
    # "{{S|prénom|fr|",
    "{{S|préposition|fr}",
    "{{S|préposition|fr|",
    "{{S|quantificateur|fr}",
    "{{S|quantificateur|fr|",
    "{{S|radical|fr}",
    "{{S|radical|fr|",
    "{{S|rafsi|fr}",
    "{{S|rafsi|fr|",
    # "{{S|sinogramme|fr}",
    # "{{S|sinogramme|fr|",
    "{{S|suffixe|fr}",
    "{{S|suffixe|fr|",
    "{{S|symbole|fr}",
    "{{S|symbole|fr|",
    "{{S|symbole|conv}",
    "{{S|variante par contrainte typographique|fr}",
    "{{S|variante par contrainte typographique|fr|",
    "{{S|verbe|fr}",
    "{{S|verbe|fr|num=",
)

# Modèle à ignorer : le texte sera supprimé.
# https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_tous_les_mod%C3%A8les/Bandeaux
templates_ignored = (
    "ancre",
    "créer-séparément",
    "désabrévier",
    "doute",
    "ébauche",
    "ébauche-déc",
    "ébauche-déf",
    "ébauche-étym",
    "ébauche-étym-nom-scientifique",
    "ébauche-exe",
    "ébauche-gent",
    "ébauche-pron",
    "ébauche-syn",
    "ébauche-trad",
    "ébauche-trad-exe",
    "ébauche-trans",
    "ébauche2-exe",
    "graphie",
    "préciser",
    "R",
    "refnec",
    "réfnéc",
    "réfnec",
    "référence nécessaire",
    "réf",
    "réf?",
    "source",
    "trad-exe",
    "trier",
)

# Modèles qui seront remplacés par du texte italique.
# https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_tous_les_mod%C3%A8les
templates_italic = {
    "absol": "Absolument",
    "adj-indéf-avec-de": "Avec de",
    "admin": "Administration",
    "aéro": "Aéronautique",
    "agri": "Agriculture",
    "alcaloïdes": "Chimie",
    "analogie": "Par analogie",
    "angl": "Anglicisme",
    "animaux": "Zoologie",
    "antonomase": "Antonomase",
    "antiq": "Antiquité",
    "apposition": "En apposition",
    "arbres": "Botanique",
    "arch": "Archaïsme",
    "archaïque": "Archaïsme",
    "archi": "Architecture",
    "Argadz": "Argot des Gadz’Arts",
    "argot internet": "Argot Internet",
    "argot typographes": "Argot des typographes",
    "argot voleurs": "Argot des voleurs",
    "astron": "Astronomie",
    "au figuré": "Figuré",
    "auto": "Automobile",
    "automo": "Automobile",
    "avant 1835": "Archaïque, orthographe d’avant 1835",
    "BDD": "Bases de données",
    "BE": "Belgique",
    "bdd": "Bases de données",
    "bioch": "Biochimie",
    "biol": "Biologie",
    "boissons": "Boisson",
    "CA": "Canada",
    "cartes": "Cartes à jouer",
    "catholicisme": "Christianisme",
    "chiens": "Zoologie",
    "chim": "Chimie",
    "chir": "Chirurgie",
    "ciné": "Cinéma",
    "cuis": "Cuisine",
    "comm": "Commerce",
    "commerces": "Commerce",
    "composants": "Électronique",
    "cour": "Courant",
    "cout": "Couture",
    "couvre-chefs": "Habillement",
    "danses": "Danse",
    "dermatol": "Dermatologie",
    "didact": "Didactique",
    "dinosaures": "Paléontologie",
    "diplo": "Diplomatie",
    "élec": "Électricité",
    "ellipse": "Par ellipse",
    "enclit": "Enclitique",
    "enfantin": "Langage enfantin",
    "euph": "Par euphémisme",
    "euphém": "Par euphémisme",
    "euphémisme": "Par euphémisme",
    "exag": "Par hyperbole",
    "exagération": "Par hyperbole",
    "éduc": "Éducation",
    "éléments": "Chimie",
    "énergie": "Industrie de l’énergie",
    "épithète": "Employé comme épithète",
    "FR": "France",
    "ferro": "Chemin de fer",
    "ferroviaire": "Chemin de fer",
    "finan": "Finance",
    "finances": "Finance",
    "fonderie": "Métallurgie",
    "formations musicales": "Musique",
    "formel": "Soutenu",
    "fortification": "Architecture",
    "fromages": "Fromage",
    "genres musicaux": "Musique",
    "graphe": "Théorie des graphes",
    "gâteaux": "Cuisine",
    "géog": "Géographie",
    "géol": "Géologie",
    "géom": "Géométrie",
    "habil": "Habillement",
    "hérald": "Héraldique",
    "hist": "Histoire",
    "hyperb": "Par hyperbole",
    "hyperbole": "Par hyperbole",
    "idiomatique": "Figuré",
    "impr": "Imprimerie",
    "improprement": "Usage critiqué",
    "indén": "Indénombrable",
    "indus": "Industrie",
    "info": "Informatique",
    "injur": "Injurieux",
    "insectes": "Entomologie",
    "intrans": "Intransitif",
    "iron": "Ironique",
    "jardi": "Jardinage",
    "juri": "Droit",
    "jurisprudence": "Droit",
    "just": "Justice",
    "langues": "Linguistique",
    "ling": "Linguistique",
    "litt": "Littéraire",
    "logi": "Logique",
    "légumes": "Botanique",
    "maladie": "Nosologie",
    "maladies": "Nosologie",
    "manège": "Équitation",
    "marque": "Marque commerciale",
    "math": "Mathématiques",
    "médecine non conv": "Médecine non conventionnelle",
    "mélio": "Mélioratif",
    "menu": "Menuiserie",
    "métrol": "Métrologie",
    "meubles": "Mobilier",
    "meubles héraldiques": "Héraldique",
    "mili": "Militaire",
    "minér": "Minéralogie",
    "minéraux": "Minéralogie",
    "muscles": "Anatomie",
    "musi": "Musique",
    "mythol": "Mythologie",
    "méca": "Mécanique",
    "métaph": "Figuré",
    "métaphore": "Figuré",
    "métaplasmes": "Linguistique",
    "météo": "Météorologie",
    "météorol": "Météorologie",
    "méton": "Par métonymie",
    "métonymie": "Par métonymie",
    "numis": "Numismatique",
    "néol": "Néologisme",
    "oenol": "Œnologie",
    "oiseaux": "Ornithologie",
    "opti": "Optique",
    "ornithol": "Ornithologie",
    "ortho1990": "Orthographe rectifiée de 1990",
    "POO": "Programmation orientée objet",
    "par ext": "Par extension",
    "part": "En particulier",
    "partic": "En particulier",
    "particulier": "En particulier",
    "pêch": "Pêche",
    "péj": "Péjoratif",
    "philo": "Philosophie",
    "photo": "Photographie",
    "phys": "Physique",
    "plais": "Par plaisanterie",
    "plantes": "Botanique",
    "poés": "Poésie",
    "poissons": "Ichtyologie",
    "popu": "Populaire",
    "prog": "Programmation informatique",
    "programmation": "Programmation informatique",
    "pronl": "Pronominal",
    "propre": "Sens propre",
    "propriété": "Droit",
    "propulsion": "Propulsion spatiale",
    "prov": "Proverbial",
    "psychol": "Psychologie",
    "QC": "Québec",
    "reli": "Religion",
    "réseaux": "Réseaux informatiques",
    "salles": "Construction",
    "sci-fi": "Science-fiction",
    "scol": "Éducation",
    "sexe": "Sexualité",
    "sout": "Soutenu",
    "spéc": "Spécialement",
    "sports": "Sport",
    "stat": "Statistiques",
    "TAAF": "Vocabulaire des TAAF",
    "tech": "Technique",
    "technol": "Technologie",
    "text": "Textile",
    "théol": "Théologie",
    "télécom": "Télécommunications",
    "trans": "Transitif",
    "transit": "Transitif",
    "tradit": "orthographe traditionnelle",
    "typo": "Typographie",
    "typog": "Typographie",
    "unités": "Métrologie",
    "usines": "Industrie",
    "vents": "Météorologie",
    "vieux": "Vieilli",
    "vête": "Habillement",
    "vêtements": "Habillement",
    "zool": "Zoologie",
    "zootechnie": "Zoologie",
}

# Modèles un peu plus complexes à gérer, leur prise en charge demande plus de travail.
# Le code de droite sera passer à une fonction qui l'exécutera. Il est possible d'utiliser
# n'importe quelle fonction Python et celles définies dans utils.py.
#
# # Les arguments disponibles sont :
#   - *tpl* (texte) qui contient le nom du modèle.
#   - *parts* (liste de textes) qui contient les autres parties du modèle.
#
# Exemple avec le modèle complet "{{comparatif de|bien|fr|adv}}" :
#   - *tpl* contiendra le texte "comparatif de".
#   - *parts* contiendra la liste ["bien", "fr", "adv"].
#
# L'accès à *tpl* et *parts* permet ensuite de modifier assez aisément le résultat souhaité.
templates_multi = {
    # {{cf|tour d’échelle}}
    # {{cf|lang=fr|faire}}
    "cf": "f\"→ voir {parts[len(parts) - 1] if len(parts) > 1 else ''}\"",
    # {{comparatif de|bien|fr|adv}}
    "comparatif de": 'f"{capitalize(tpl)} {parts[1]}"',
    # {{couleur|#B0F2B6}}
    "couleur": 'f"[RGB {parts[1]}]"',
    # {{fchim|H|2|O}}
    "fchim": "format_chimy(parts[1:])",
    # XIX{{e}}
    # {{e|-1}}
    "e": "f\"<sup>{parts[1] if len(parts) > 1 else 'e'}</sup>\"",
    # {{er}}
    "er": "'<sup>er</sup>'",
    # {{emploi|au passif}}
    "emploi": 'f"<i>({capitalize(parts[1])})</i>"',
    # {{étyl|la|fro|mot=invito|type=verb}}
    "étyl": "handle_etyl(parts)",
    # {{forme pronominale|mutiner}}
    "forme pronominale": 'f"{capitalize(tpl)} de {parts[1]}"',
    # {{in|5}}
    "in": 'f"<sub>{parts[1]}</sub>"',
    # {{lien|étrange|fr}}
    "lien": "parts[1]",
    # {{nom w pc|Aldous|Huxley}}
    "nom w pc": "handle_name(parts)",
    # {{nombre romain|12}}
    "nombre romain": "int_to_roman(int(parts[1]))",
    # {{petites capitales|Dupont}}
    # {{pc|Dupont}}
    # {{smcp|Dupont}}
    "petites capitales": "f\"<span style='font-variant:small-caps'>{parts[1]}<span>\"",
    "pc": "f\"<span style='font-variant:small-caps'>{parts[1]}<span>\"",
    "smcp": "f\"<span style='font-variant:small-caps'>{parts[1]}<span>\"",
    # {{pron|plys|fr}}
    "pron": r'f"\\{parts[1]}\\"',
    # {{pron-API|/j/}}
    "pron-API": "parts[1]",
    # {{RFC|5322}}
    "RFC": 'f"{capitalize(tpl)} {parts[1]}"',
    # {{région}}
    # {{région|Lorraine et Dauphiné}}
    "région": "f\"<i>({parts[1] if len(parts) > 1 else 'Régionalisme'})</i>\"",
    # {{siècle|XVI}}
    # {{siècle|XVIII|XIX}}
    "siècle": "f\"<i>({handle_century(parts, 'siècle')})</i>\"",
    # {{siècle2|XIX}}
    "siècle2": 'f"{parts[1]}ème"',
    # {{sport|fr}}
    # {{sport|fr|collectifs}}
    "sport": "handle_sport(tpl, parts)",
    # {{superlatif de|petit|fr}}
    "superlatif de": 'f"{capitalize(tpl)} {parts[1]}"',
    # {{term|ne … guère que}}
    "term": "handle_term(parts[1])",
    # {{terme|Astrophysique}}
    "terme": "f\"<i>({parts[1] if len(parts) > 1 else 'Terme'})</i>\"",
    # {{trad+|conv|Sitophilus granarius}}
    "trad+": "parts[2]",
    # {{unité|92|%}}
    "unité": "handle_unit(parts[1:])",
    # {{variante de|ranche|fr}}
    "variante de": 'f"{capitalize(tpl)} {parts[1]}"',
    # {{variante ortho de|acupuncture|fr}}
    "variante ortho de": 'f"Variante orthographique de {parts[1]}"',
    # {{ws|Bible Segond 1910/Livre de Daniel|Livre de Daniel}}
    # {{ws|Les Grenouilles qui demandent un Roi}}
    "ws": "parts[2] if len(parts) > 2 else parts[1]",
    # {{wsp|Panthera pardus|''Panthera pardus''}}
    # {{wsp|Brassicaceae}}
    "wsp": "parts[2] if len(parts) > 2 else parts[1]",
}

# Modèles qui seront remplacés par du texte personnalisé.
templates_other = {
    "absolu": "<i>absolu</i>",
    "apocope": "Apocope",
    "au singulier uniquement": "<i>au singulier uniquement</i>",
    "au pluriel uniquement": "<i>au pluriel uniquement</i>",
    "collectif": "<i>collectif</i>",
    "contraction": "contraction",
    "dépendant": "<i>dépendant</i>",
    "déterminé": "déterminé",
    "f": "<i>féminin</i>",
    "fm": "féminin ou masculin (l’usage hésite)",
    "fplur": "<i>féminin pluriel</i>",
    "genre ?": "Genre à préciser",
    "i": "<i>intransitif</i>",
    "impers": "<i>impersonnel</i>",
    "indéterminé": "indéterminé",
    "invar": "<i>invariable</i>",
    "m": "<i>masculin</i>",
    "majus": "<i>majuscule</i>",
    "mf": "<i>masculin et féminin identiques</i>",
    "mf ?": "<i>masculin ou féminin (l’usage hésite)</i>",
    "minus": "<i>minuscule</i>",
    "nombre ?": "Nombre à préciser",
    "note": "<b>Note :</b>",
    "peu attesté": "/!\\ Ce terme est très peu attesté.",
    "p": "<i>pluriel</i>",
    "palind": "<i>palindrome</i>",
    "prnl": "<i>pronominal</i>",
    "s": "<i>singulier</i>",
    "sp": "<i>singulier et pluriel identiques</i>",
    "sp ?": "<i>singulier et pluriel identiques ou différenciés (l’usage hésite)</i>",
    "réfl": "<i>réfléchi</i>",
    "réciproque": "<i>réciproque</i>",
    "t": "<i>transitif</i>",
    "tr-dir": "<i>transitif direct</i>",
    "tr-indir": "<i>transitif indirect</i>",
    "usage": "<b>Note d'usage :</b>",
}

# Le parseur affichera un avertissement quand un modèle contient des espaces superflus,
# sauf pour ceux listés ci-dessous :
template_warning_skip = ("fchim", "graphie", "lien web", "ouvrage", "source")

# Traductions diverses
translations = {
    # Contenu de la release telle qu'elle sera générée sur
    # https://github.com/BoboTiG/ebook-reader-dict/releases/tag/fr
    "release_desc": """Nombre de mots : {words_count}
Export Wiktionnaire : {dump_date}

:arrow_right: Téléchargement : [dicthtml-fr.zip]({url})

---

<sub>Mis à jour le {creation_date}</sub>
""",
    # Séparateur des milliers
    "thousands_separator": " ",
}

# Le nom du dictionnaire qui sera affiché en-dessous de chaque définition
wiktionary = "Wiktionnaire (ɔ) {year}"
