
import streamlit as st

st.set_page_config(
    page_title="Language Tutor AI",
    page_icon="📚",
    layout="wide",
)

# Sidebar
st.sidebar.title("📚 Language Tutor AI")
page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Grammar", "Vocabulary", "Reading"],
)

learner_level = st.sidebar.selectbox(
    "English level",
    ["Beginner", "Intermediate", "Advanced"],
)

# Main page
st.title(f"Welcome to {page}")

st.write(f"Your selected level: {learner_level}")

# Three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Lessons completed", 4)

with col2:
    st.metric("Quiz score", "80%")

with col3:
    st.metric("Learning streak", "3 days")

st.divider()

# Group related content
with st.container(border=True):
    st.subheader("Today's learning activity")
    st.write("Practice five new vocabulary words.")

    if st.button("Start learning"):
        st.success("Your learning activity is ready!")

# Hide optional information
with st.expander("What will I learn?"):
    st.write("You will learn new words, meanings, and example sentences.")
