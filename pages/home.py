import streamlit as st


def app():
    st.title("Language Tutor AI")

    st.write(
        "Welcome to your personal AI-powered English learning assistant!"
    )

    st.markdown(
        """
        Practice English at your own pace with interactive exercises
        designed to improve your grammar skills.
        """
    )

    st.divider()

    st.subheader("Your Learning Activities")

    st.markdown("### 📘 Grammar Practice")

    st.write(
        "Learn grammar rules and test your understanding "
        "with AI-generated multiple-choice questions."
    )

    st.info(
        "Select Grammar Practice from the sidebar to get started."
    )
