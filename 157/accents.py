from unicodedata import decomposition


def filter_accents(text):
    """Return a sequence of accented characters found in
    the passed in lowercased text string
    """
    return {c for c in text.lower() if decomposition(c)}


text = (
    "The 5 French accents;"
    "The cédille (cedilla) Ç ..."
    "The accent aigu (acute accent) é ..."
    "The accent circonflexe (circumflex) â, ê, î, ô, û ..."
    "The accent grave (grave accent) à, è, ù ..."
    "The accent tréma (dieresis/umlaut) ë, ï, ü"
)
