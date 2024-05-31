from ollama import chat

from database import get_chat_messages


def get_answer(model="llava:v1.6"):
    response = chat(model=model, messages=get_chat_messages(), stream=True)

    return response
