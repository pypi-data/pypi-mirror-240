"""
Real Time Speech Translator (rtst)

The rtst is a comprehensive Python package designed to facilitate speech-to-text processing. It integrates multiple speech recognition services, language detection, translation, and text-to-speech capabilities into a unified and user-friendly interface.

Features:
- Speech Recognition: Support for multiple services including Google, Azure, AWS, and Hugging Face.
- Language Detection: Automatic detection of the language of spoken content.
- Translation: Capability to translate recognized speech into English.
- Text-to-Speech: Converts text into spoken words.

This package is ideal for applications that require handling spoken language input and output, such as virtual assistants, accessibility tools, language learning apps, and more.

Usage:
The package provides a simple yet powerful interface for speech recognition and processing. Users can capture speech from a microphone, recognize it using a preferred service, detect the language, translate it if necessary, and then use text-to-speech to vocalize the result.

Example:
    from rtst import process_speech
    process_speech(service='google', language='en-US')

For more detailed information on each function and advanced usage, refer to the module documentation within the package.

License:
This project is licensed under License.md - see the LICENSE file for details.

Contributing:
Contributions to rtst are welcome. Please follow the contribution guidelines specified in the repository.

Note:
Ensure you have the necessary API keys and credentials for using specific services like Azure, AWS, and Hugging Face.

"""
from .main import recognize_speech_from_mic, recognize_speech_from_mic_text, translate_speech, speak_text, process_speech, huggingface_speech_recognize, aws_speech_recognize, azure_speech_recognize
