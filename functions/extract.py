import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to extract metadata from a given URL
def extract_metadata(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # st.write(str(soup))
            meta_tags = soup.find_all('meta')
            metadata = {}
            for tag in meta_tags:
                if tag.get('name'):
                    metadata[tag.get('name')] = tag.get('content')
                elif tag.get('property'):
                    metadata[tag.get('property')] = tag.get('content')
            title_tag = soup.find('title')
            if title_tag:
                metadata['title'] = title_tag.string
            return metadata
        else:
            return {"error": f"Failed to retrieve the webpage. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}