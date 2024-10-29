import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the Google Generative AI
genai.configure(api_key=os.getenv("AIzaSyD2QdfKqET7Z40ZNiOoSUABCCx7b4A5Vk8"))

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get("message")
    chat_session = model.start_chat(history=[
        {"role": "user", "parts": ["hi\n"]},
        {"role": "model", "parts": ["Hi! What can I do for you today? \n"]}
    ])
    response = chat_session.send_message(user_message)
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
