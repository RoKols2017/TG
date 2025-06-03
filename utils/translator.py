from googletrans import Translator

_translator = Translator()


def to_english(text: str) -> str:
    """Переводит text на English (auto-detect исходный язык)."""
    return _translator.translate(text, dest="en").text
