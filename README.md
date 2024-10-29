
# AI Chat Bot

This AI Chat Bot is a simple web-based chat application that uses the Gemini AI API to generate responses based on user inputs. The frontend is styled with a clean and modern look, providing an engaging chat experience.

## Features

- **Responsive Chat Interface**: A visually appealing chat interface with floating messages and a footer.
- **Backend Integration**: Uses Flask to handle user messages and interact with the Gemini AI API.
- **Auto Scroll**: Automatically scrolls to show the latest messages in the chat.
- **Send with Enter Key**: User can hit enter to send a message instead of clicking "Send."
- **User-Friendly Footer**: Footer displaying the developer's name.

## Demo

<img src="https://github.com/user-attachments/assets/68aa100d-449e-4d11-a340-bb3ca15de23d" alt="Chatbot Demo" width="600" />

## Prerequisites

- Python 3.7 or higher
- Google Gemini API key

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/ai-chat-bot.git
   cd ai-chat-bot
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   - Create a `.env` file in the project root directory with your Gemini API key:

     ```plaintext
     GEMINI_API_KEY=your_api_key_here
     ```

5. **Run the Flask App**

   ```bash
   python app.py
   ```

6. **Access the Chatbot**

   Open your browser and go to `http://127.0.0.1:5000` to start chatting with the AI bot.

## Project Structure

```
ai-chat-bot/
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # HTML frontend with chat UI
├── static/
│   └── style.css         # Styles for the chat UI
├── .env                  # Environment variables for API keys
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Dependencies

- `Flask` - Python web framework for handling HTTP requests.
- `python-dotenv` - For loading environment variables from a `.env` file.
- `google-generativeai` - SDK to access the Google Gemini AI API.

## Usage

- **Send a Message**: Type your message in the input field and either press `Enter` or click the "Send" button.
- **Bot Response**: The bot's response will appear instantly after the message is processed.
- **Developed By**: Your name, displayed at the bottom, provides a professional touch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed by Haritha Mihimal
```

This `README.md` provides clear steps for anyone to set up and run the chatbot, along with a concise description of the project’s features and structure. Make sure to add the `.env` and `requirements.txt` files as outlined. Let me know if you need help with anything else!
