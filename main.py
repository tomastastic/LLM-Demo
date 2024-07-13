from openai import OpenAI
from dotenv import load_dotenv

import os


# Load environment variables from .env file
load_dotenv()

key = os.getenv('API_KEY')
client = OpenAI(api_key=key)
'''
def chat_with_gpt(prompt):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ],
    max_tokens=10  # token limit for the response
    )
    return response.choices[0].message['content']
'''
def chat_with_gpt(user_message):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Be nice"},
            {"role": "user", "content": user_message}
        ],
        max_tokens=5  # token limit for the response
    )
    return completion


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        print("Chatbot: ", chat_with_gpt(user_input))

