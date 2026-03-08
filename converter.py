import subprocess
import os

OGG_DIR = "ogg_to_wav"
WAV_DIR = "waves"
MP3_DIR = "output"

os.makedirs(OGG_DIR, exist_ok=True)
os.makedirs(WAV_DIR, exist_ok=True)
os.makedirs(MP3_DIR, exist_ok=True)


def ensure_ext(name, ext):
    name = name.strip()
    if not name.lower().endswith(ext):
        name += ext
    return name


def ogg_to_wav():
    name = input("Enter OGG file name (with or without .ogg): ")
    name = ensure_ext(name, ".ogg")

    input_path = os.path.join(OGG_DIR, name)

    if not os.path.exists(input_path):
        print(f"❌ {name} not found in '{OGG_DIR}'")
        return

    base = os.path.splitext(name)[0]
    output_path = os.path.join(WAV_DIR, base + ".wav")

    subprocess.run(["ffmpeg", "-y", "-i", input_path, output_path])

    print(f"✅ WAV created: {output_path}")


def wav_to_mp3():
    name = input("Enter WAV file name (with or without .wav): ")
    name = ensure_ext(name, ".wav")

    input_path = os.path.join(WAV_DIR, name)

    if not os.path.exists(input_path):
        print(f"❌ {name} not found in '{WAV_DIR}'")
        return

    base = os.path.splitext(name)[0]
    output_path = os.path.join(MP3_DIR, base + ".mp3")

    subprocess.run(["ffmpeg", "-y", "-i", input_path, output_path])

    print(f"✅ MP3 created: {output_path}")


def menu():
    while True:
        print("\n===== AUDIO CONVERTER =====")
        print("1 - Convert OGG → WAV")
        print("2 - Convert WAV → MP3")
        print("3 - Exit")

        choice = input("What do you want to do? ")

        if choice == "1":
            ogg_to_wav()
        elif choice == "2":
            wav_to_mp3()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice")


menu()