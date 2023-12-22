import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return tokens

def simple_chatbot(user_input):
    user_tokens = preprocess_text(user_input)

    patterns = [
        {"pattern": ["hello", "hi", "hey"], "response": ["Hi there!", "Hello!", "Hey!"]},
        {"pattern": ["how", "you"], "response": ["I'm good, thank you!", "Not too bad, thanks for asking."]},
        {"pattern": ["bye", "goodbye"], "response": ["Goodbye!", "See you later!", "Bye!"]},
        {"pattern": ["your", "name"], "response": ["I'm a chatbot.", "You can call me Bot!"]},
        {"pattern": ["weather"], "response": ["I'm just a bot and don't know about the weather. You can check a weather website!"]},
        {"pattern": ["time"], "response": ["I don't have a clock, but your device should be able to tell you the time!"]},
        {"pattern": ["joke"], "response": ["Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!"]},
        {"pattern": ["thanks", "thank you"], "response": ["You're welcome!", "No problem!", "Glad I could help!"]},
    ]

    for pattern in patterns:
        if any(keyword in user_tokens for keyword in pattern["pattern"]):
            return random.choice(pattern["response"])

    return "I'm not sure how to respond to that."

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    response = simple_chatbot(user_input)
    print("Bot:", response)