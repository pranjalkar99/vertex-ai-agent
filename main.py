from dotenv import load_dotenv
from src.agents.sqlagent import (
    runnable as sqlagentrunnable
)
load_dotenv()


# from openai import OpenAI

# client = OpenAI()
# audio_file = open("test-audio.mp3", "rb")
# transcript = client.audio.transcriptions.create(model='whisper', file=audio_file)


inputs = {
    "ORDER_DETAILS" : "Add debt for Kavya for 1.5 kg of tomatoes at 40 rs per kg, 0.25 kg \
        of spinach at 20 rs per kg, and 1 pack of cookies at 30 rs."
    }
out = sqlagentrunnable.invoke(inputs)
print(out)
from src.utils.sqloutputparser import extract_sql

print(extract_sql(out))
