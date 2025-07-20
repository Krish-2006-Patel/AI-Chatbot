from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow JS frontend calls

# Configure Gemini API
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

@app.route('/chat', methods=['POST'])
def chat_route():
    data = request.get_json()
    user_input = data.get('message', '')

    if not user_input:
        return jsonify({'error': 'Message is required'}), 400

    response = chat.send_message(user_input)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(port=8081)
