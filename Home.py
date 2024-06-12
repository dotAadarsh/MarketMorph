import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Market Morph",  # Title of the page
    page_icon="📺",  # Icon for the page
    layout="centered",  # Layout of the page
    initial_sidebar_state="expanded",  # Initial state of the sidebar
    menu_items={
        'Get Help': 'https://twitter.com/dotAadarsh',  # Menu item for getting help
        'Report a bug': "https://github.com/dotAadarsh/MarketMorph",  # Menu item for reporting a bug
        'About': "Empower Your Brand's Voice Globally: One App, Infinite Adaptations."  # Menu item for about section
    }
)

# Title and caption
st.title("Market Morph")  # Main title of the app
st.caption("Empower Your Brand's Voice Globally: One App, Infinite Adaptations.")  # Caption for the app

# Streamlit app UI
def main():
    
    st.markdown("""
    ### **Ad Copy Generation**
    #### Business Challenge Addressed:
    - Relevant, Brand specific Ad Copy, produced for a given Ad Campaign
    - Ad Copy written in Brand specific Tone of Voice and using Brand Style guidelines, with the engine able to learn different brand styles
    - Ad Copy produced for multiple different ad channels and formats
    - Increasing creative efficiency & greater brand alignment for assets produced.
    """)

    if st.button("Generate"):
        st.switch_page("pages/Generate.py")

    st.markdown("""
    ### **Asset Localization and Adaptation at Scale**
    #### Business Challenge Addressed:
    - Produce multiple local creative adapts and variations, against a given master asset, for use across multiple channels, including social, video and display
    - Accelerate and automate the production of creative localizations, adapting copy, headlines, etc., and imagery/creative to local market content and needs.
    """)

    if st.button("Localize"):
        st.switch_page("pages/Localize.py")

if __name__ == "__main__":
    main()
