# Import necessary libraries
import speech_recognition as sr
import azure.cognitiveservices.speech as speechsdk
import boto3
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import numpy as np
import tensorflow as tf
import soundfile as sf
import io
import librosa


def google_speech_recognize(recognizer, audio, language):
    try:
        return recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"


def huggingface_speech_recognize(
    audio,
    language,
    model_name="facebook/wav2vec2-base-960h",
    tokenizer_name="facebook/wav2vec2-base-960h",
):
    model_name, tokenizer_name = get_huggingface_model_for_language(language)
    tokenizer = Wav2Vec2Tokenizer.from_pretrained(tokenizer_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name, from_pt=True)
    # Convert the AudioData to a NumPy array and resample
    audio_data = np.frombuffer(audio.frame_data, np.int16)
    audio_np, samplerate = sf.read(io.BytesIO(audio_data), dtype="float32")
    if samplerate != 16000:
        audio_np = librosa.resample(audio_np, orig_sr=samplerate, target_sr=16000)
    input_values = tokenizer(
        audio_np, return_tensors="tf", padding="longest"
    ).input_values
    logits = model(input_values).logits
    # Decode the predicted IDs
    predicted_ids = tf.argmax(logits, axis=-1)
    transcription = tokenizer.batch_decode(predicted_ids.numpy())
    return transcription[0]


def aws_speech_recognize(audio, language, region="us-east-1"):
    aws_language = convert_to_aws_language_code(language)
    # Initialize boto3 client for AWS
    transcribe_client = boto3.client("transcribe", region_name=region)
    filename = "temp_audio.wav"
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
    # Start transcription
    job_name = "transcription" + str(int(time.time()))
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": "file://" + filename},
        MediaFormat="wav",
        LanguageCode=aws_language,
    )
    # Wait for the transcription job to complete
    while True:
        status = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        if status["TranscriptionJob"]["TranscriptionJobStatus"] in [
            "COMPLETED",
            "FAILED",
        ]:
            break
        time.sleep(5)
    # Fetch and return the transcription result
    if status["TranscriptionJob"]["TranscriptionJobStatus"] == "COMPLETED":
        transcript_file_uri = status["TranscriptionJob"]["Transcript"][
            "TranscriptFileUri"
        ]
        transcript_response = requests.get(transcript_file_uri)
        transcript = transcript_response.json()["results"]["transcripts"][0][
            "transcript"
        ]
        return transcript
    else:
        raise Exception("AWS Transcription failed")


def azure_speech_recognize(audio, language):
    azure_language = convert_to_azure_language_code(language)
    speech_config = speechsdk.SpeechConfig(
        subscription="YourSubscriptionKey",
        region="YourServiceRegion",
        speech_recognition_language=azure_language,
    )
    audio_config = speechsdk.AudioConfig(use_default_microphone=True)
    azure_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config
    )
    result = azure_recognizer.recognize_once()
    return result
