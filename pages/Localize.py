import streamlit as st
import numpy as np
from functions.get_rsa import get_ai_rsa_response
import pandas as pd 
import json

st.set_page_config(
    page_title="Market Morph",
    page_icon="📺",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://twitter.com/dotAadarsh',
        'Report a bug': "https://github.com/dotAadarsh/ghost",
        'About': "Global Reach, Local Impact: Empower Your Brand's Adaptation Journey with Effortless Precision"
    })


def main():
    st.header("Localizer")

    uploaded_file1 = st.file_uploader("Upload your master Ad copy/sitelink asset")
    uploaded_file2 = st.file_uploader("Upload search terms specific to the market")
    market = st.selectbox("Select the market:", ["EMEA", "APAC", "North America", "Latin America"])

    generate_asset_button = st.button("Generate Asset")

    if generate_asset_button:
        if uploaded_file1 is None or uploaded_file2 is None or market == "":
            st.write("Please provide all the inputs before generating the asset.")
        else:
            file_contents1 = uploaded_file1.read()
            file_contents2 = uploaded_file2.read()
            prompt = f"Based on the following content: {file_contents2}, localize the {file_contents1} for the top local languages present in the {market} market. use localized_content as key"
            localized_responese = get_ai_rsa_response(prompt)
            localized_responese = json.loads(localized_responese)
            print(localized_responese)
            # Convert JSON to DataFrame
            df = pd.DataFrame.from_dict(localized_responese['localized_content'], orient='index')

            # Display DataFrame
            st.write(df)


if __name__ == "__main__":
    main()
