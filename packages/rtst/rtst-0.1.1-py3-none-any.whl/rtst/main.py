import speech_recognition as sr
from langdetect import detect
from googletrans import Translator, LANGUAGES
import pyttsx3
import azure.cognitiveservices.speech as speechsdk
import boto3
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import numpy as np
import tensorflow as tf
import soundfile as sf
import io
import librosa

# Initialize the recognizer
r = sr.Recognizer()
# Initialize the translator
translator = Translator()
# Initialize text-to-speech engine
engine = pyttsx3.init()

def google_speech_recognize(recognizer, audio, language):
    return recognizer.recognize_google(audio, language=language)

def huggingface_speech_recognize(audio, language, model_name="facebook/wav2vec2-base-960h", tokenizer_name="facebook/wav2vec2-base-960h"):
    model_name, tokenizer_name = get_huggingface_model_for_language(language)
    tokenizer = Wav2Vec2Tokenizer.from_pretrained(tokenizer_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name, from_pt=True)
    # Convert the AudioData to a NumPy array and resample
    audio_data = np.frombuffer(audio.frame_data, np.int16)
    audio_np, samplerate = sf.read(io.BytesIO(audio_data), dtype='float32')
    if samplerate != 16000:
        audio_np = librosa.resample(audio_np, orig_sr=samplerate, target_sr=16000)
    input_values = tokenizer(audio_np, return_tensors="tf", padding="longest").input_values
    logits = model(input_values).logits
    # Decode the predicted IDs
    predicted_ids = tf.argmax(logits, axis=-1)
    transcription = tokenizer.batch_decode(predicted_ids.numpy())
    return transcription[0]


def aws_speech_recognize(audio, language, region="us-east-1"):
    aws_language = convert_to_aws_language_code(language)
    # Initialize boto3 client for AWS
    transcribe_client = boto3.client('transcribe', region_name=region)
    filename = "temp_audio.wav"
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
    # Start transcription
    job_name = "transcription" + str(int(time.time()))
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': 'file://' + filename},
        MediaFormat='wav',
        LanguageCode=aws_language
    )
    # Wait for the transcription job to complete
    while True:
        status = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        time.sleep(5)
    # Fetch and return the transcription result
    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        transcript_file_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
        transcript_response = requests.get(transcript_file_uri)
        transcript = transcript_response.json()['results']['transcripts'][0]['transcript']
        return transcript
    else:
        raise Exception("AWS Transcription failed")

def azure_speech_recognize(audio, language):
    azure_language = convert_to_azure_language_code(language)
    speech_config = speechsdk.SpeechConfig(subscription="YourSubscriptionKey", region="YourServiceRegion", speech_recognition_language=azure_language)
    audio_config = speechsdk.AudioConfig(use_default_microphone=True)
    azure_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = azure_recognizer.recognize_once()
    return result

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

def main():
    print("Please speak into the microphone...")
    language = input("Enter the language code (e.g., 'en-US' for English, 'es-ES' for Spanish): ")
    response = recognize_speech_from_mic(r, sr.Microphone(), service='google', language=language)
    #response = recognize_speech_from_mic(r, sr.Microphone(), service='google')
    print("Please speak into the microphone...")
    if response["success"]:
        detected_lang = response["detected_language"]
        translation = response["translation"]
        print(f"Detected Language: {detected_lang}")
        print(f"Translated Text: {translation}")
        speak_text(translation)
    else:
        print(f"Error: {response['error']}")

if __name__ == "__main__":
    main()