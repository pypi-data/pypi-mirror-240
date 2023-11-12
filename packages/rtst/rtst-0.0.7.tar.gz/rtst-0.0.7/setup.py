from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="rtst",
    version="0.0.7",
    packages=find_packages(),
    install_requires=[
        "speechrecognition",
        "langdetect",
        "googletrans==3.1.0a0",
        "pyttsx3",
        "azure-cognitiveservices-speech",
        "boto3",
        "transformers",
        "numpy",
        "tensorflow",
        "soundfile",
        "librosa",
        "PyAudio",
    ],
    entry_points={"console_scripts": ["speech-recog=rtst.main:main"]},
    long_description=long_description,
    long_description_content_type='text/markdown',
)
