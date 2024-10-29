import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Generative AI API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Flask app initialization
app = Flask(__name__)

# Generative Model Configuration
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

# Homepage Route
@app.route('/')
def index():
    return render_template('index.html')

# Route for Sending Message to the AI Model
@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        chat_session = model.start_chat(
            history=[
                {"role": "user", "parts": ["hi\n"]},
                {"role": "model", "parts": ["Hi! What can I do for you today?\n"]},
            ]
        )
        response = chat_session.send_message(user_message)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
