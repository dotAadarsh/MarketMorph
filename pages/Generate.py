import streamlit as st
from functions.extract import extract_metadata
from functions.get_response import get_ai_response
import json
import pandas as pd
from functions.embeddings import generate_embeddings
from functions.embeddings import search_docs
from functions.get_rsa import get_ai_rsa_response

def main():
    
    method = st.selectbox("What do you want to generate?", ["RSA", "Sitelink"])

    if method == "Sitelink":

        url = st.text_input("Enter the landing page URL")
        languages = st.multiselect("Select Languages", ["English", "Spanish", "French", "German"], default=["English"])
        num_sitelinks = st.number_input("Number of sitelinks you want to generate", min_value=1, max_value=5, value=3)

        if st.button("Generate Assets"):
            if url is not None:
                metadata = extract_metadata(url)
                if "error" in metadata:
                    st.error(metadata["error"])

                else:
                    st.toast("Meta data received successfully!")
                    
                    st.write("Metadata extracted from the website:")
                    
                    if "title" in metadata:
                        st.write(f"**Title**: {metadata['title']}")
                        meta_data = f"**Title**: {metadata['title']}"
                    if "headline" in metadata:
                        st.write(f"**Headline**: {metadata['headline']}")
                        meta_data = f"**Headline**: {metadata['headline']}"
                    if "description" or  "Description" in metadata:
                        description = metadata.get("description") or metadata.get("Description")

                    if "keywords" in metadata:
                        st.write(f"**Keywords**: {metadata['keywords']}")
                        meta_data = f"**Keywords**: {metadata['keywords']}"
                    
                    prompt = f"Create {num_sitelinks} Sitelink extensions with the 1 sitelink headline(25 chars) and 2 descriptions(35 chars) each within the maximum allowed characted limit based on the following data in the {languages} language(s)."
                    
                    with st.spinner('Waiting for AI response...'):
                        result = get_ai_response(prompt, meta_data)
                    
                    # Parse the JSON string
                    response = json.loads(result)
                    # st.write(response)

                    # Extract the list of dictionaries
                    sitelinks_data = response["sitelinks"]

                    # Convert the list of dictionaries to a DataFrame
                    result = pd.DataFrame(sitelinks_data)

                    st.subheader("Generated Sitelinks")
                    # Display the DataFrame in a Streamlit table
                    st.dataframe(result, hide_index=1)

    if method == "RSA":

        
        uploaded_file = st.file_uploader("Please upload the search term report")
        user_preference = st.text_input("What are you expecting?", "Ads on Mens products")

        if uploaded_file and user_preference is not None:
            
            file_contents = uploaded_file.read()

            # Break file_contents into chunks
            chunks = []
            chunk_size = 1000  # Define the size of each chunk
            for i in range(0, len(file_contents), chunk_size):
                chunk = file_contents[i:i+chunk_size]
                chunks.append(chunk)

            # Generate embeddings for each chunk
            embeddings = []
            for chunk in chunks:
                embedding = generate_embeddings(chunk)
                embeddings.append(embedding)
            

            top_texts = search_docs("Generate Ad copies for the brand", chunks, embeddings, top_n=5)
            
            prompt = f"Create one Ad Copy strictly with the 15 headlines and 4 descriptions within the maximum allowed character limit according to the user preference: {user_preference} by using the following data: {top_texts}. Do not exceed the mentioned limit."

            with st.spinner('Waiting for AI response...'):
                ad_copy_json = get_ai_rsa_response(prompt)
            
           # st.write(ad_copy_json)

            # Convert JSON data to DataFrame
            ad_copy_data = json.loads(ad_copy_json)
            df = pd.DataFrame(ad_copy_data)

            # Create dataframe
            df = pd.DataFrame(df['adCopy'])
            
            st.dataframe(df)

if __name__ == "__main__":
    main()
