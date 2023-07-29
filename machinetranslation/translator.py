"""
This module contains functions for translating text between languages.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French using the MyMemoryTranslator.

    Args:
        english_text (str): The text to translate.

    Returns:
        str: The translated text.
    """
    # Create an instance of the MyMemoryTranslator for English to French translation
    translator = MyMemoryTranslator(source="english", target="french")
    
    # Use the translator to translate the English text to French
    french_text = translator.translate(english_text)
    
    # Return the translated text
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English using the MyMemoryTranslator.

    Args:
        french_text (str): The text to translate.

    Returns:
        str: The translated text.
    """
    # Create an instance of the MyMemoryTranslator for French to English translation
    translator = MyMemoryTranslator(source="french", target="english")
    
    # Use the translator to translate the French text to English
    english_text = translator.translate(french_text)
    
    # Return the translated text
    return english_text
