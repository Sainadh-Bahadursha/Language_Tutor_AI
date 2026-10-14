from langchain_core.prompts import ChatPromptTemplate


# Version 1: Grammar question generation
GRAMMAR_QUESTIONS_V1 = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a friendly English grammar tutor.

            Generate exactly {number_of_questions}
            multiple-choice questions.

            Topic: {topic}
            Learner level: {level}

            Each question must contain:
            - A question
            - Four options: A, B, C and D
            - One correct answer
            - A short explanation

            Return output matching the application's
            structured output schema.
            """,
        ),
        ("human", "Generate the grammar quiz."),
    ]
)


# Central prompt registry
PROMPT_REGISTRY = {
    "grammar_questions": GRAMMAR_QUESTIONS_V1,
}