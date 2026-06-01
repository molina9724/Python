import pyttsx3
from pyttsx3 import Engine

engine: Engine = pyttsx3.init()
# engine.say("Hello!")
# engine.say("How are you today?")
# engine.say("Happy birthday to you!")

print(engine.getProperty("volume"))
print(engine.getProperty("rate"))
# print(engine.getProperty("voices"))

all_voices = engine.getProperty("voices")

for voice in all_voices:  # type: ignore
    print(voice.name, voice.gender, voice.age, voice.languages, voice.id)

engine.setProperty("rate", 200)
engine.setProperty("volume", 1)
# engine.setProperty("voice", "com.apple.speech.synthesis.voice.Albert")

# engine.say("Hablando some Spanglish")
engine.save_to_file(
    "I created this thing with my hands, how about it?",
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter24/my_audio.wav",
)
engine.runAndWait()

import whisper
from whisper import Whisper

model: Whisper = whisper.load_model("base")
result = model.transcribe(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter24/my_audio.wav",
    language="English",
)
print(result["text"])

write_function = whisper.utils.get_writer(  # type: ignore
    "srt", "/Users/daniel_molina/Downloads/Python/Python/Book/chapter24/"
)
write_function(
    result,
    "audio",
)

import yt_dlp

# with yt_dlp.YoutubeDL() as ydl:
#     ydl.download(["https://www.youtube.com/watch?v=xAA-bQk662w"])

video_url = "https://www.youtube.com/watch?v=xAA-bQk662w"
options = {
    "quiet": True,  # Suppress the output.
    "no_warnings": True,  # Suppress warnings.
    "outtmpl": "downloaded_content.%(ext)s",
    "format": "m4a/bestaudio/best",
    "postprocessors": [
        {  # Extract audio using ffmpeg.
            "key": "FFmpegExtractAudio",
            "preferredcodec": "m4a",
        }
    ],
}

# with yt_dlp.YoutubeDL(options) as ydl:  # type: ignore
#     ydl.download([video_url])

import json
from typing import Any

url = "https://www.youtube.com/watch?v=kSrnLbioN6w"
options: dict[str, Any] = {
    "quiet": True,
    "no_warnings": True,
    "skip_download": True,
}

with yt_dlp.YoutubeDL(options) as ydl:  # type: ignore
    info = ydl.extract_info(video_url)
    json_info = ydl.sanitize_info(info)
    if json_info is not None:
        print(json_info.keys())
    with open(
        "/Users/daniel_molina/Downloads/Python/Python/Book/chapter24/video_to_json.json",
        "w",
        encoding="utf-8",
    ) as json_file:
        json_file.write(json.dumps(json_info))
