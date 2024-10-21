import streamlit as st
from PIL import Image

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

# Load the image
img = Image.open('certificate.jpg')

# Create a CSS style to hide the full screen button


# Display the image with the CSS style
st.image(img)

if st.button("Back"):
    st.switch_page("2")
