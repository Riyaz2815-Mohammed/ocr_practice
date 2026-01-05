# mistral_client.py

from mistralai import Mistral

def get_mistral_client(api_key: str) -> Mistral:
    return Mistral(api_key=api_key)