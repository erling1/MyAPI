import requests

url_chats = "http://127.0.0.1:8001/chats"

create_response = requests.post(url_chats)

id = create_response.json()

print(id['id'])  # Debugging line



url = f"http://127.0.0.1:8001/chats/{id}"  # Replace with your endpoint

payload = {"Message": "how old are you"}

response = requests.post(url, json=payload, stream=True)

# Check if the response is a valid stream
if response.status_code == 200:
    print("Start Streaming Data:")
    for chunk in response.iter_content(chunk_size=1024, decode_unicode=True):
        if chunk:
            print(chunk)  # This will print each chunk of the streamed response
else:
    print("Failed to send message:", response.text)









