
from flask import Flask, request, render_template, jsonify
import google.generativeai as palm

app = Flask(__name__)

# Configure the API key
API_KEY = "AIzaSyBgv0a3DuNlGQy6zxarbWHiVJsUIZhy4Bc"
palm.configure(api_key=API_KEY)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/index')
def chat():
    return render_template('index.html')

@app.route('/get_response')
def get_response():
    user_message = request.args.get('message')
    conversation = chat_with_palm(user_message)
    bot_response = conversation[-1]['content'] if conversation else "An error occurred."

    return jsonify({"botMessage": bot_response})

def chat_with_palm(prompt):
    examples = [
        ('Hello', 'Hi there, how can I assist you today?'),
        ('Take me to London from Japan', 'Enter a flight then go the closest route to the nearest mall')
    ]

    conversation = []
    if prompt.lower() == "exit":
        return conversation

    response = palm.chat(messages=prompt, temperature=0.2, context='Speak like a texi driver', examples=examples)
    for message in response.messages:
        conversation.append({'author': message['author'], 'content': message['content']})

    return conversation

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/')
# def home():
#     return render_template('chat.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.form['user-input']
#     conversation = chat_with_palm(user_input)
#     return render_template('chat.html', conversation=conversation)

# def chat_with_palm(prompt):
#     conversation = []
#     if prompt.lower() == "exit":
#         return conversation

#     response = palm.chat(messages=prompt, temperature=1)
#     for message in response.messages:
#         conversation.append({'author': message['author'], 'content': message['content']})

#     return conversation

# if __name__ == '__main__':
#     app.run(debug=True)
