import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('OPENAI_API_KEY')

"""def AI_respons(message: str):

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content"""

def AI_respons(message: str):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Enable streaming in the API call
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system", "content": "You are a chatbot that only answers questions about my Website, Erlings Nettsted . If a question is unrelated, politely redirect them. ",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo",
        stream=True  # Enable streaming mode
    )

    # Stream the chunks from the API
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:  # Only yield if there's content
            print(chunk.choices[0].delta.content)
            yield f"id: 123 \n"
            yield f"type: event\n"
            yield f"event:{message}\n"
            yield f"data: {chunk.choices[0].delta.content}\n\n" #SSE stream


for response in AI_respons("What is a phone?"):
    print( response)

