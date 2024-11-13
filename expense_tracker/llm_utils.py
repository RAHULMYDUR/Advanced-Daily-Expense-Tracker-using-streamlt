import requests
import json
from .config import LLM_API_KEY

def generate_response(retrieved_chunks, user_query):
    prompt = f'''
    You are a chatbot that answers questions based on the following documents, where this data is about the daily expense:
    {retrieved_chunks}

    User Question: "{user_query}"

    Provide a coherent and contextually relevant answer.
    '''
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={LLM_API_KEY}"

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt,
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
        response.raise_for_status()
        generated_content = response.json().get("candidates", [])[0].get("content", {}).get("parts", [])[0].get("text", "No response available.")
        return generated_content.strip()
    except requests.exceptions.RequestException as e:
        return "Error in generating response."

