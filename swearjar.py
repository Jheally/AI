import sounddevice as sd
from scipy.io.wavfile import write
import whisper

# Swear severity rankings
swear_words = {
    "poop": 4,
    "shoot": 2,
    "darn": 1,
    "67": 5,
    "skibidi": 5,
    "frick": 3,
    "chuzz": 4,
    "chud": 5,
    "gyatt": 5,
    "fart": 2,
    "crud": 3,
    "crap": 4,
    "holy cow": 2,
    "heck": 2,
    "stupid": 5,
    "idiot": 4,
    "dum dum": 3,
    "geez louise": 2,
    "chopped": 4,
    "fudge": 2,
    "mother trucker": 5,
    "doofus": 4,
    "freak": 5,
    "flip": 1,
    "shart": 2,
    "shat": 3
}

print("Loading AI speech recognition model...")
model = whisper.load_model("base")

total_score = 0

while True:

    input("\nPress ENTER to record 5 seconds...")

    fs = 44100
    seconds = 5

    print("Recording now...")

    audio = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1
    )

    sd.wait()

    write("temp.wav", fs, audio)

    print("Transcribing speech with AI...")

    result = model.transcribe("temp.wav")

    text = result["text"].lower()

    print("\nDetected Speech:")
    print(text)

    found_any = False

    for word, severity in swear_words.items():

        if word in text:

            found_any = True
            total_score += severity

            print(f"\nDetected: {word}")
            print(f"Severity: {severity}/5")

    if not found_any:
        print("\nNo swear words detected.")

    print(f"\nTotal Swear Score: {total_score}")
