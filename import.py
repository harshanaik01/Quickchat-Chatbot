from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot with logic adapters
chatbot = ChatBot(
    'TestBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch'  # Ensures the best response is picked
    ]
)

# Create a new trainer
trainer = ListTrainer(chatbot)

# Train with improved general conversation
general_conversations = [
    "Hello", "Hi there!",
    "Hi", "Hello!",
    "Hey", "Hey! How can I help?",
    "Hii", "Hi! How are you?",
    "Helo", "Hello!",
    "Helllo", "Hello! You seem excited!",
    "How are you?", "I'm good. How can I assist you?",
    "What is your name?", "I am Quickchat, your friendly chatbot.",
    "Who created you?", "I was created by a Harsha using Python and ChatterBot."
]

# Train with math questions
math_conversations = [
    "What is 2 + 2?", "2 + 2 is 4.",
    "Solve 10 - 3", "10 minus 3 equals 7.",
    "What is 5 * 6?", "5 times 6 is 30.",
    "Divide 20 by 4", "20 divided by 4 is 5."
]

# Train with general political questions
political_conversations = [
    "Who is the president of the USA?", "The current president of the USA is Joe Biden. (Update if needed)",
    "What is democracy?", "Democracy is a system of government where citizens vote for their leaders.",
    "What is the UN?", "The United Nations (UN) is an international organization founded to promote peace and cooperation."
]

# Train with Indian political questions
indian_political_conversations = [
    "Who is the Prime Minister of India?", "The Prime Minister of India is Narendra Modi. (Update if needed)",
    "Who is the President of India?", "The current President of India is Droupadi Murmu. (Update if needed)",
    "What is Lok Sabha?", "Lok Sabha is the lower house of India's Parliament, where Members of Parliament (MPs) are elected by the public.",
    "What is Rajya Sabha?", "Rajya Sabha is the upper house of India's Parliament, with members appointed by the President and elected by state legislatures.",
    "Which party is currently ruling India?", "The Bharatiya Janata Party (BJP) is currently in power. (Update if needed)",
    "Who was the first Prime Minister of India?", "Pandit Jawaharlal Nehru was the first Prime Minister of India.",
    "What is Article 370?", "Article 370 granted special status to Jammu and Kashmir, but it was revoked in August 2019.",
    "What is GST?", "GST (Goods and Services Tax) is a unified tax system in India that replaced multiple indirect taxes.",
    "What is the Election Commission of India?", "The Election Commission of India is an autonomous body responsible for conducting free and fair elections in India."
]

# Train with tech questions
tech_conversations = [
    "What is AI?", "AI, or Artificial Intelligence, is the simulation of human intelligence in machines.",
    "What is Python?", "Python is a popular programming language known for its simplicity and power.",
    "What is cloud computing?", "Cloud computing is the delivery of computing services over the internet.",
    "Who founded Microsoft?", "Microsoft was founded by Bill Gates and Paul Allen."
]

# Train chatbot with all the conversations
trainer.train(general_conversations + math_conversations + political_conversations + indian_political_conversations + tech_conversations)

print("Hello! I am your chatbot. Type 'quit' to exit.")

# Chat loop
while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        print("Goodbye! Have a great day!")
        break
    response = chatbot.get_response(user_input)
    print(response)
