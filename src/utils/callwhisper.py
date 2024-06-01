from openai import OpenAI

client = OpenAI()
audio_file = open("test-audio.mp3", "rb")
transcript = client.audio.transcriptions.create(model='whisper', file=audio_file)
