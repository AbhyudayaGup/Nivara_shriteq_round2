import streamlit as st
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

# Title of the page
st.title("Rate the Information")

st.markdown("Did you know writing a short summary on what you just read leads to better understanding and retention of the material! Try it out yourself!")
comment = st.text_area("Please write a short 50 word summary on the article you just read:", max_chars=800)

word_count = len(comment.split())

st.write(f"Word count: {word_count}/50")

if word_count >= 50:
    # Rating slider (1 to 5)
    rating = st.slider("Rate the content from 1 to 5", 1, 5)

    # Dropdown for marking misinformation status
    misinfo_status = st.selectbox(
        "Mark the information as:",
        ("Severe Misinformation", "Slight Misinformation", "Completely True")
    )

    # Button for submitting the rating
    if st.button("Submit Rating"):
        st.success(f"Rating: {rating}/5")
        st.write(f"Misinformation status: {misinfo_status}")
        st.write(f"Your comment: {comment}")
        st.write("Thank you for your feedback it is greatly appreciated!")
        if st.button("Check out my profile"):
            st.switch_page("4")
else:
    # Inform the user they need to write at least 50 words
    st.warning("Please enter at least 50 words before you can rate the content.")

# Back button to return to page1.py
if st.button("Back"):
    switch_page("2")
