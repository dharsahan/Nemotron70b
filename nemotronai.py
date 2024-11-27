'''from openai import OpenAI
import os
import time
os.system('clear')
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)
while True:
    try:
        promte = input("\nenter Prompt : ")
        completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[{"role":"user","content":f"{promte}"}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
        )

        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
    except(KeyboardInterrupt):
        print('\nExiting...')
        time.sleep(1)
        os.system('clear')
        break
'''


import streamlit as st
from openai import OpenAI
import os
import time

# Set page config for wide layout
st.set_page_config(layout="wide")

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"  # Replace with your actual API key
)

# Streamlit UI elements
st.title("Nemotron")

user_input = st.text_area("Enter your prompt:", height=100)
submit_button = st.button("Submit")

chat_history = st.empty()  # Placeholder for chat history


def display_message(role, content):
    """Displays a message in the chat history."""
    chat_history.markdown(f"**{role.capitalize()}:** {content}")



if submit_button:
    with st.spinner("Generating response..."):
        try:
            completion = client.chat.completions.create(
                model="nvidia/llama-3.1-nemotron-70b-instruct",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.5,
                top_p=1,
                max_tokens=1024,
                stream=True
            )

            response_content = ""
            for chunk in completion:
                if chunk.choices[0].delta.content is not None:
                    content_fragment = chunk.choices[0].delta.content
                    response_content += content_fragment
                    display_message("Assistant", response_content)  # Update in real-time
                    # Optional: Add a small delay for a more natural feel
                    # time.sleep(0.05)

            # Final display (in case the last chunk doesn't trigger a refresh)
            display_message("Assistant", response_content)


        except Exception as e:
            st.error(f"An error occurred: {e}")
