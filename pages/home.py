
import streamlit as st


def app():
    st.title("Language Tutor AI")

    st.write(
        "Welcome to your personal AI-powered English learning assistant!"
    )

    st.markdown(
        """
        Improve your English through interactive exercises,
        AI-generated questions, and personalized feedback.
        """
    )

    st.divider()

    st.subheader("Your Learning Activities")

    # Grammar Practice
    st.markdown("### 📘 Grammar Practice")

    st.write(
        "Strengthen your understanding of English grammar through "
        "multiple-choice questions on tenses, articles, prepositions, "
        "subject-verb agreement, and other grammar topics."
    )

    # Vocabulary Practice
    st.markdown("### 📚 Vocabulary Practice")

    st.write(
        "Build your English vocabulary by exploring words across "
        "different topics, learning their meanings, and reviewing "
        "example sentences with AI-powered feedback."
    )

    st.divider()

    st.info(
        "Select Grammar Practice or Vocabulary Practice from "
        "the sidebar to begin learning."
    )
