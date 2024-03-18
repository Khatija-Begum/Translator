
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO

def translate_text(text,dest_lang):
    translated_text = GoogleTranslator(source='en',target=dest_lang).translate(text)
    return translated_text


def text_to_speech(text,dest_lang):
    tts = gTTS(text=text,lang=dest_lang)
    with BytesIO() as buffer:
        tts.write_to_fp(buffer)
        buffer.seek(0)
        audio_data  = buffer.read()
    return audio_data

text = "A data scientist proficient in machine learning algorithms, statistical analysis, and data visualization, and extracting actionable insights from complex datasets to drive informed decision-making  "
dest_lang = 'te'

translated_text = translate_text(text,dest_lang)

tts_audio = text_to_speech(translated_text,dest_lang)
with open("translated_audio.mp3","wb") as audio_file:
    audio_file.write(tts_audio)

