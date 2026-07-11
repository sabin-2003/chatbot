import os
import gradio as gr
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role": "system",
        "content": """You are a skilled MVD officer with a successful
        track record in numerous cases. Your role is to assist people by
        providing guidance on Indian laws and offering answers in a
        professional legal manner."""
    }
]

def customLLMBot(message, history):
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    return reply

demo = gr.ChatInterface(
    fn=customLLMBot,
    title="MVD Chatbot",
    description="Motor Vehicle Law Assistant",
    examples=[
        "Hi",
        "What are the motorcycle laws in India?"
    ]
)

demo.launch(server_name="0.0.0.0",
            server_port=int(os.environ.get("PORT", 7860)))
