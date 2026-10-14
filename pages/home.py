import streamlit as st


def app():
    st.title("Language Tutor AI")

    st.write(
        "Welcome to your personal AI-powered English learning assistant!"
    )

    st.markdown(
        """
        Improve your English through interactive exercises, AI-generated
        questions, reading activities, and personalized translation feedback.
        Choose an activity from the sidebar to get started.
        """
    )

    st.divider()
    st.subheader("Your Learning Activities")

    with st.container(border=True):
        st.markdown("### 📘 Grammar Practice")
        st.write(
            "Strengthen your grammar through multiple-choice questions on "
            "tenses, articles, prepositions, subject-verb agreement, and more."
        )

    with st.container(border=True):
        st.markdown("### 📚 Vocabulary Practice")
        st.write(
            "Learn useful words by topic, test your understanding, and review "
            "definitions, example sentences, and explanations."
        )

    with st.container(border=True):
        st.markdown("### 📖 Reading Comprehension")
        st.write(
            "Read a level-appropriate passage, answer comprehension questions, "
            "and review explanations after submitting your answers."
        )

    with st.container(border=True):
        st.markdown("### 🌐 Translation Practice")
        st.write(
            "Translate text between supported languages and receive feedback "
            "on meaning, grammar, and natural phrasing."
        )

    st.divider()
    st.info(
        "Select Grammar Practice, Vocabulary Practice, Reading Comprehension, "
        "Reading Exam, or Translation Practice from the sidebar to begin."
    )
