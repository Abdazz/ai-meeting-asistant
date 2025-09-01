from transformers import pipeline
from product_assistant import remove_non_ascii, product_assistant
from llm import chain
import os
from dotenv import load_dotenv
load_dotenv()

def transcript_audio(audio_file):
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-medium",
        chunk_length_s=30,
    )
    raw_transcript = pipe(audio_file, batch_size=8)["text"]
    ascii_transcript = remove_non_ascii(raw_transcript)
    adjusted_transcript = product_assistant(ascii_transcript)
    result = chain.invoke({"context": adjusted_transcript})

    output_file = "outputs/meeting_minutes_and_tasks.md"
    with open(output_file, "w") as file:
        file.write(result)

    return result, output_file