import gradio
from groq import Groq
client = Groq(api_key="GROQ_API_KEY")
def initialize_messages():
  return [{"role": "system",
           "content": """you are a skilled MVD officer with a
           successful track record in numerous cases.Your role is to
           assist people by providing guidance on indian laws and
           offering answers in a professional legal manner."""}]
  messages_prmt = initialize_messages()
  def customLLMBot(user_input, history):

    global messages_prmt

    messages_prmt.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages_prmt
    )

    LLM_reply = response.choices[0].message.content

    messages_prmt.append(
        {
            "role": "assistant",
            "content": LLM_reply
        }
    )

    return LLM_reply
    iface = gradio.ChatInterface(customLLMBot,
                             chatbot=gradio.Chatbot(height=300),
                             textbox=gradio.Textbox(placeholder="Ask me a question related to Motorcycle Laws"),
                             title="MVD chatbot",
                             description="chat bot law assistance",
                             examples=["hi","what are the Motorcycle Laws"]
                             )
    iface.launch(share=True)
