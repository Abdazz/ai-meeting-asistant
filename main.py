import os
import gradio as gr
from dotenv import load_dotenv
from transcription import transcript_audio

load_dotenv()

audio_input = gr.Audio(sources=["upload"], type="filepath", label="Upload your audio file")
output_text = gr.Textbox(label="Meeting Minutes and Tasks")
download_file = gr.File(label="Download the Generated Meeting Minutes and Tasks")

iface = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input,
    outputs=[output_text, download_file],
    title="AI Meeting Assistant",
    description="Upload an audio file of a meeting. This tool will transcribe the audio, fix product-related terminology, and generate meeting minutes along with a list of tasks."
)

iface.launch(
    server_name=os.getenv("SERVER_NAME"),
    server_port=int(os.getenv("SERVER_PORT")),
    share=True
)