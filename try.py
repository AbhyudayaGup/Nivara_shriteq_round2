import streamlit as st
import requests
import pandas as pd
from streamlit_extras.switch_page_button import switch_page  # Import the switch_page function

# Function to fetch articles from CrossRef
def fetch_articles_crossref(topic):
    url = "https://api.crossref.org/works"
    params = {
        "query": topic,
        "rows": 10,  # Number of articles to fetch
        "sort": "relevance"  # You can sort by 'relevance' or 'published'
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles = []

    for item in data['message']['items']:
        article = {
            "Title": item.get("title", ["N/A"])[0],
            "Journal": item.get("container-title", ["N/A"])[0],
            "URL": item.get("URL", "N/A")
        }
        articles.append(article)

    return articles

# Streamlit interface
st.title("Search Scholarly Articles using CrossRef")
topic = st.text_input("Enter a topic to search for recent research papers", "")

if topic:
    articles = fetch_articles_crossref(topic)
    if articles:
        df = pd.DataFrame(articles)

        # Add an index starting from 1
        df.index = df.index + 1

        # Display the dataframe without index column (since we're customizing below)
        st.write("### Articles Found")

        # Loop through each row to display title and add buttons for each article
        for idx, row in df.iterrows():
            col1, col2, col3 = st.columns([6, 1, 1])
            with col1:
                st.write(f"**{idx}. {row['Title']}**")
                st.write(f"*{row['Journal']}*")
            with col2:
                st.write("")
                if st.button(f"View Article {idx}", key=f"view_{idx}"):
                    st.write(f"[Click to View]({row['URL']})")
            with col3:
                st.write("")
                # Button to switch to the review page (3.py)
                if st.button(f"Review {idx}", key=f"review_{idx}"):
                    # Store the selected article details in session state
                    st.session_state.selected_article = row.to_dict()
                    # Switch to the 3.py page
                    switch_page("3")
    else:
        st.write("No articles found for this topic.")
