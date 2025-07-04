import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created for your internship project."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm just a bot, but I'm fine :)"]
    ],
    [
        r"(.*) your internship (.*)",
        ["I'm built to help you complete your internship task!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help. Ask me anything about your internship project."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "See you later!", "Thanks for chatting!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?"]
    ]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("🤖 Chatbot: Hello! Type 'quit' to exit.")
chatbot.converse()
