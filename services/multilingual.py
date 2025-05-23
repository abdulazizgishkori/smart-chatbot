from deep_translator import GoogleTranslator
from langdetect import detect

def translate_input(text, target_lang):
    detected = detect(text)
    if detected != target_lang:
        return GoogleTranslator(source='auto', target='en').translate(text)
    return text

def translate_output(text, target_lang):
    return GoogleTranslator(source='en', target=target_lang).translate(text)
