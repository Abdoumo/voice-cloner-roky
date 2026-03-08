import sounddevice as sd
import scipy.io.wavfile as wav
import requests
import os
import re
from faster_whisper import WhisperModel
from TTS.api import TTS

# ===============================
# CONFIG
# ===============================

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "your_model_name_here_in_lm_studio"

SAMPLE_RATE = 16000
RECORD_SECONDS = 4

folder = "waves"
folder_output = "output"

file_input = "your_file"
ROKY_VOICE_FILE = folder + f"/{file_input}.wav"

# language mapping for TTS
LANG_MAP = {
    "fr": "fr-fr",
    "en": "en",
    "pt": "pt-br"
}

# ===============================
# LOAD MODELS
# ===============================

print("Loading Whisper...")
whisper_model = WhisperModel("medium", compute_type="int8")

print("Loading TTS...")
tts = TTS("tts_models/multilingual/multi-dataset/your_tts")

print("Assistant ready!")

# ===============================
# RECORD AUDIO
# ===============================

def record_audio(filename="input.wav"):
    print("🎤 Listening...")
    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1
    )
    sd.wait()
    wav.write(filename, SAMPLE_RATE, audio)
    return filename


# ===============================
# SPEECH → TEXT
# ===============================

def transcribe(audio_file):
    segments, info = whisper_model.transcribe(audio_file)
    text = "".join([segment.text for segment in segments])

    print("📝 User:", text)
    print("🌍 Language:", info.language)

    return text, info.language


# ===============================
# LLM RESPONSE
# ===============================

def ask_llm(prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "Reply in the same language as the user. Be concise."
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    r = requests.post(LM_STUDIO_URL, json=payload)
    data = r.json()

    reply = data["choices"][0]["message"]["content"]

    print("🤖 AI:", reply)

    return reply


# ===============================
# SPLIT TEXT INTO SENTENCES
# ===============================

def split_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)


# ===============================
# TEXT → SPEECH
# ===============================

def speak(text, language, speaker_file=ROKY_VOICE_FILE):

    # fix language code
    language = LANG_MAP.get(language, "en")

    output_file = folder_output + f"/{file_input}.wav"

    tts.tts_to_file(
        text=text,
        file_path=output_file,
        language=language,
        speaker_wav=speaker_file,
        speed=0.60
    )

    # play audio
    if os.name == "nt":
        os.system("start " + output_file)
    else:
        os.system("afplay " + output_file)


# ===============================
# MAIN LOOP
# ===============================

while True:

    audio_file = record_audio()

    text, lang = transcribe(audio_file)

    if not text.strip():
        continue

    reply = ask_llm(text)

    sentences = split_sentences(reply)

    for sentence in sentences:
        speak(sentence, lang)

