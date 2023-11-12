import speech_recognition as sr
from langdetect import detect
from googletrans import Translator, LANGUAGES
import pyttsx3
from recognizers import (
    google_speech_recognize,
    huggingface_speech_recognize,
    aws_speech_recognize,
    azure_speech_recognize,
)


r = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()

def recognize_speech_from_mic(recognizer, microphone, service='google', language='en-US'):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    response = {
        "success": True,
        "error": None,
        "transcription": None,
        "detected_language": None,
        "translation": None
    }
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        if service == 'google':
            response["transcription"] = google_speech_recognize(recognizer, audio, language)
        elif service == 'azure':
            response["transcription"] = azure_speech_recognize(audio, language)
        elif service == 'aws':
            response["transcription"] = aws_speech_recognize(audio, language)
        elif service == 'huggingface':
            response["transcription"] = huggingface_speech_recognize(audio)
        else:
            response["error"] = "Unsupported speech recognition service"
        # Process the transcription
        if response["transcription"]:
            detected_lang = detect(response["transcription"])
            response["detected_language"] = LANGUAGES.get(detected_lang, "Unknown language")
            if detected_lang != 'en':
                translation = translator.translate(response["transcription"], dest='en')
                response["translation"] = translation.text
            else:
                response["translation"] = response["transcription"]
    except sr.UnknownValueError:
        response["error"] = "Could not understand audio"
    except sr.RequestError as e:
        response["error"] = f"Could not request results; {e}"
    except Exception as e:
        response["success"] = False
        response["error"] = str(e)
    return response

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def process_speech(service="google"):
    print("Please enter the source language code (e.g., 'ru-RU' for Russian): ")
    source_language = input().strip()

    print("Please enter the target language code (e.g., 'en-US' for English): ")
    target_language = input().strip()

    print("Please speak into the microphone...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    # Call the recognition function with the specified source language
    response = recognize_speech_from_mic(r, source, service, source_language)
    
    if response["success"]:
        # Directly use the transcription without automatic language detection
        transcription = response["transcription"]
        print(f"Transcribed Text: {transcription}")

        # Translate only if the source and target languages are different
        if source_language != target_language:
            translated_text = translator.translate(transcription, src=source_language, dest=target_language).text
            print(f"Translated Text: {translated_text}")
            speak_text(translated_text)
        else:
            speak_text(transcription)
    else:
        print(f"Error: {response['error']}")

if __name__ == "__main__":
    process_speech()
