import os
from openai import AzureOpenAI
import streamlit as st

AZURE_API_KEY = st.secrets["AZURE_API_KEY"]
AZURE_API_VERSION = st.secrets["GPT_35_AZURE_API_VERSION"]
AZURE_API_ENDPOINT = st.secrets["AZURE_API_ENDPOINT"]

client = AzureOpenAI(
  api_key = AZURE_API_KEY,
  api_version = AZURE_API_VERSION,
  azure_endpoint = AZURE_API_ENDPOINT
)

def get_ai_rsa_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-35-turbo-southindia",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful assistant designed to output JSON."""},
                {"role": "user", "content": prompt}
            ]
        )
        print(response)
        # print(response.model_dump_json(indent=2))
        st.toast("Success! AI response received.")
        return response.choices[0].message.content
    
    except Exception as e:
        error_message = str(e)
        st.toast(error_message)
        st.toast("Something went wrong! Try again!")
        return None

