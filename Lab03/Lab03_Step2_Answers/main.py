from flask import Flask, request, render_template
from utils import chat
import os

app = Flask(__name__)

MODEL = "crumb/nano-mistral"

# to warm up the model
chat("hi", MODEL)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

    
# Handle POST requests to dialo endpoint
@app.route("/api/chat", methods=["POST"])
def dialo_chatbot():
    # Get the input message from the request
    input_message = request.json["message"]
    print("Received message:", input_message)
    
    # Return response
    response = chat(input_message, MODEL)
    response = response.get("response", "")  # Extract the "response" value
    print("Generated response:", response)

    return response

# Run the Flask application
if __name__ == "__main__":
    app.run(port=5000)
