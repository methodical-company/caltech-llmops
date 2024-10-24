import streamlit as st
import requests
import json

# Lab 04: Chatbot with CloudRun integration

# Show title and description.
st.title("💬 Chatbot with CloudRun")
st.write(
    "This is a simple chatbot that sends messages to a CloudRun endpoint and receives responses. "
    "To use this app, you need to provide your CloudRun endpoint URI."
)

# Ask user for the CloudRun endpoint URI.
cloudrun_endpoint = st.text_input("CloudRun Endpoint URI")
if not cloudrun_endpoint:
    st.info("Please add your CloudRun endpoint URI to continue.", icon="🗝️")
else:

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Send the user's message to the CloudRun endpoint.
        try:
            response = requests.post(
                cloudrun_endpoint,
                headers={"Content-Type": "application/json"},
                data=json.dumps({"message": prompt}),
            )

            # Process the response.
            if response.status_code == 200:
                assistant_reply = response.text
            else:
                assistant_reply = "Error: Could not get a response from the CloudRun endpoint."

        except Exception as e:
            assistant_reply = f"Error: {str(e)}"

        # Display the assistant's reply.
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)
        
        # Store the assistant's response.
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
