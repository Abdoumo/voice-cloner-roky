# ROKY Audio Tools

A collection of Python audio tools by **Abdoumo**.

* **Audio Converter** – Convert **OGG → WAV → MP3** using `ffmpeg`.
* **Voice Cloner Assistant** – Record your voice, transcribe it, generate AI responses via **LM Studio**, and speak back using **TTS with a custom voice**.

---

# Table of Contents

1. [Audio Converter](#audio-converter)
2. [Voice Cloner Assistant](#voice-cloner-assistant)
3. [License](#license)

---

# Audio Converter

A simple command-line tool to convert audio files between **OGG → WAV** and **WAV → MP3** formats.

## Features

* Convert **OGG files → WAV**
* Convert **WAV files → MP3**
* Automatically handles file extensions
* Organizes outputs into directories

```
ogg_to_wav/   → input OGG files
waves/        → generated WAV files
output/       → generated MP3 files
```

---

## Requirements

* Python **3.10+**
* `ffmpeg` installed and available in PATH

Python packages:

```
sounddevice==0.5.5
scipy==1.11.4
requests==2.32.3
numpy>=1.24.0
```

---

## Windows Setup for ffmpeg

1. Download
   `ffmpeg-2026-03-05-git-74cfcd1c69-essentials_build.7z`

2. Extract to:

```
C:\ffmpeg\
```

3. Add to **System PATH**:

```
C:\ffmpeg\bin
```

4. Test installation:

```
ffmpeg -version
```

---

## Installation

```
pip install -r converter/requirements.txt
python converter/converter.py
```

---

## Usage

1. Place your **OGG files** in:

```
ogg_to_wav/
```

2. Run the script and choose an option:

```
===== AUDIO CONVERTER =====

1 - Convert OGG → WAV
2 - Convert WAV → MP3
3 - Exit
```

Outputs:

```
WAV → waves/
MP3 → output/
```

---

# Voice Cloner Assistant

A Python voice assistant that:

1. Records audio from your microphone
2. Transcribes speech using **faster_whisper**
3. Generates responses using **LM Studio**
4. Speaks replies using **TTS with a custom voice**

---

## Features

* Microphone recording (default **4 seconds**)
* Speech transcription via **faster_whisper**
* AI responses via **LM Studio API**
* Custom **voice cloning TTS**

---

## Requirements

* Python **3.10+**
* `ffmpeg` installed and available in PATH

Python packages:

```
sounddevice==0.5.5
scipy==1.11.4
requests==2.32.3
faster-whisper==1.2.1
TTS==0.21.1
numpy>=1.24.0
torch>=2.1.0
torchaudio>=2.1.0
```

---

## Setup

1. Place your **ROKY voice WAV file** inside:

```
voice_cloner/waves/
```

2. Edit `voice_roky.py`:

```python
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "your_model_name_here_in_lm_studio"

folder = "waves"
folder_output = "output"

file_input = "your_file"  # name of ROKY voice file without extension
```

Optional language mapping:

```python
LANG_MAP = {
    "fr": "fr-fr",
    "en": "en",
    "pt": "pt-br"
}
```

---

## Installation

```
pip install -r voice_cloner/requirements.txt
python voice_cloner/voice_roky.py
```

---

## Usage

Run the script and speak into the microphone.

The assistant will:

1. Transcribe your speech
2. Generate a response via **LM Studio**
3. Speak the reply using **TTS**

Example interaction:

```
🎤 Listening...

📝 User: Hello, how are you?
🌍 Language: en

🤖 AI: I'm doing great, thanks!
```

---

## Folder Structure

```
voice_cloner/
│
├── waves/            # Input WAV files (custom voice)
├── output/           # Generated TTS files
├── voice_roky.py     # Main script
└── requirements.txt  # Dependencies
```

---

# License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.
