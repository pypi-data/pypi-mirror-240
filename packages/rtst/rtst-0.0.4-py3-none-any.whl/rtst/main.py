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


def recognize_speech_from_mic(
    recognizer, microphone, service="google", language="en-US"
):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    response = {
        "success": True,
        "error": None,
        "transcription": None,
        "detected_language": None,
        "translation": None,
    }
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        if service == "google":
            response["transcription"] = google_speech_recognize(
                recognizer, audio, language
            )
        elif service == "azure":
            response["transcription"] = azure_speech_recognize(audio, language)
        elif service == "aws":
            response["transcription"] = aws_speech_recognize(audio, language)
        elif service == "huggingface":
            response["transcription"] = huggingface_speech_recognize(audio)
        else:
            response["error"] = "Unsupported speech recognition service"
        # Process the transcription
        if response["transcription"]:
            detected_lang = detect(response["transcription"])
            response["detected_language"] = LANGUAGES.get(
                detected_lang, "Unknown language"
            )
            if detected_lang != "en":
                translation = translator.translate(response["transcription"], dest="en")
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


def process_speech(service="google", source_language="en-US", target_language="en-US"):
    print("Please speak into the microphone...")
    response = recognize_speech_from_mic(
        r, sr.Microphone(), service=service, language=source_language
    )
    print("Recognizing speech...")
    if response["success"]:
        detected_lang = response["detected_language"]
        print(f"Detected Language: {detected_lang}")
        if detected_lang != target_language:
            translation = translator.translate(response["transcription"], src=detected_lang, dest=target_language)
            translated_text = translation.text
            print(f"Translated Text: {translated_text}")
            speak_text(translated_text)
        else:
            print(f"Original Text: {response['transcription']}")
            speak_text(response['transcription'])
    else:
        print(f"Error: {response['error']}")

if __name__ == "__main__":
    process_speech()
