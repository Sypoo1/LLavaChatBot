import streamlit as st

from database import clear_chat_history, get_chat_messages, update_chat_messages
from model import get_answer
from utils import byte_to_string

st.title("LLava Chat Bot")


st.sidebar.title("Options")
button1 = st.sidebar.button("Clear Chat History")
button2 = st.sidebar.file_uploader("Upload Image")


if not button1:
    for msg in get_chat_messages():
        st.chat_message(msg["role"]).write(msg["content"])

if button1:
    clear_chat_history()


if user_prompt := st.chat_input():
    images = []

    if button2 is not None:
        image = button2.read()
        images = [byte_to_string(image)]

    st.chat_message("user").write(user_prompt)

    new_message = {"role": "user", "content": user_prompt, "images": images}

    update_chat_messages(new_message)

    with st.spinner("Generating..."):
        response = get_answer()
    

        response_text = ""
        message_container = st.empty()

        for chunk in response:
            response_text += chunk["message"]["content"]
            message_container.chat_message("assistant").write(response_text)



        new_bot_message = {"role": "assistant", "content": response_text}
        update_chat_messages(new_bot_message)
