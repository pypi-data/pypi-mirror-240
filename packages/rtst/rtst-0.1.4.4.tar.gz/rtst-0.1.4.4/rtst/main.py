import speech_recognition as sr
from langdetect import detect
from googletrans import Translator, LANGUAGES
import pyttsx3
from .recognizers import (
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

def process_speech(service='google'):
    print("Enter the language code (e.g., 'en' for English, 'es' for Spanish): ")
    language = input().strip()

    print("Please speak into the microphone...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = recognize_speech_from_mic(recognizer, source, service, language)
    if response["success"]:
        detected_lang = response["detected_language"]
        translation = response["translation"]
        print(f"Transcribed Text: {response['transcription']}")
        print(f"Detected Language: {detected_lang}")
        print(f"Translated Text: {translation}")
        speak_text(translation)
    else:
        print(f"Error: {response['error']}")
        
############## with text ################        
def recognize_speech_from_mic_text(recognizer, microphone, service='google', source_language='en-US', target_language='en-US'):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    response = {
        "success": True,
        "error": None,
        "transcription": None,
        "translation": None
    }
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        # Speech recognition using the specified service
        if service == 'google':
            response["transcription"] = google_speech_recognize(recognizer, audio, source_language)
        elif service == 'azure':
            response["transcription"] = azure_speech_recognize(audio, source_language)
        elif service == 'aws':
            response["transcription"] = aws_speech_recognize(audio, source_language)
        elif service == 'huggingface':
            response["transcription"] = huggingface_speech_recognize(audio, source_language)
        else:
            raise ValueError("Unsupported speech recognition service")

        # Translation to target language if different from source language
        if response["transcription"] and source_language != target_language:
            translation = translator.translate(response["transcription"], src=source_language, dest=target_language)
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
        
def translate_speech(service="google", source_language="en-US", target_language="en-US"):
    print("Please speak into the microphone...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    response = recognize_speech_from_mic(r, source, service, source_language)

    if response["success"]:
        transcription = response["transcription"]
        print(f"Transcribed Text: {transcription}")

        if source_language != target_language:
            translated_text = translator.translate(transcription, src=source_language, dest=target_language).text
            print(f"Translated Text: {translated_text}")
            response["translation"] = translated_text
            speak_text(translated_text)
        else:
            response["translation"] = transcription
            speak_text(transcription)
    else:
        print(f"Error: {response['error']}")

    return response

def main():
    print("Select a mode to test:")
    print("1. Process Speech (Automatic Language Detection)")
    print("2. Recognize and Translate Speech (Specify Source and Target Languages)")
    choice = input("Enter choice (1 or 2): ")
    if choice == '1':
        process_speech()
    elif choice == '2':
        print("Enter source language code (e.g., 'ru-RU' for Russian): ")
        source_language = input().strip()
        print("Enter target language code (e.g., 'en-US' for English): ")
        target_language = input().strip()
        translate_speech(service="google", source_language=source_language, target_language=target_language)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
    process_speech()
