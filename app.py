
import streamlit as st
from pages import home, grammar_practice


st.set_page_config(
    page_title="Language Tutor AI",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="expanded"
)


PAGES = {
    "Home": home,
    "Grammar Practice": grammar_practice,
}


def main():
    st.sidebar.title("Language Tutor AI")

    selection = st.sidebar.radio(
        "Go to",
        list(PAGES.keys())
    )

    page = PAGES[selection]
    page.app()


if __name__ == "__main__":
    main()