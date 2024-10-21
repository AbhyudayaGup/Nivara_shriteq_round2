import streamlit as st
import requests
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


API_KEY = '6535dac296854c1681a46c2045bdfe74'


def fetch_news(api_key, query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    return response.json()

# Streamlit App
def main():
    st.title("News Fetcher App")
    
    # Input search term (no need to input API key)
    query = st.text_input("Enter the topic you want to search for")

    if query:
        # Fetch the news using the hardcoded API key
        news_data = fetch_news(API_KEY, query)

        if news_data.get("status") == "ok":
            articles = news_data.get("articles", [])
            
            if articles:
                for article in articles:
                    st.subheader(article['title'])
                    st.write(f"Source: {article['source']['name']}")
                    st.write(f"Published at: {article['publishedAt']}")
                    st.write(article['description'])
                    st.write(f"[Read more]({article['url']})")
                    st.write("---")
                    if st.button('Review me'):
                        switch_page("3")
            else:
                st.write("No articles found.")
        else:
            st.error("Failed to fetch news. Check your query.")
    
if __name__ == "__main__":
    main()
