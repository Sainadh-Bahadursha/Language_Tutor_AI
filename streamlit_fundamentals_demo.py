
import streamlit as st

st.set_page_config(
    page_title="Language Tutor AI",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Language Tutor AI")
st.header("Welcome to your learning dashboard")

st.write(
    "Practice grammar, vocabulary, reading, writing, and speaking."
)

st.markdown("### Today's Learning Goal")
st.info("Learn five new vocabulary words.")

st.success("Your Streamlit application is running!")

st.divider()

st.subheader("Explore your learning preferences")

learner_name = st.text_input("What should we call you?")
learner_level = st.selectbox(
    "Choose your English level",
    ["Beginner", "Intermediate", "Advanced"],
)

if st.button("Save Preferences"):
    if learner_name.strip():
        st.success(
            f"Welcome, {learner_name}! "
            f"Your selected level is {learner_level}."
        )
    else:
        st.warning("Please enter your name first.")
