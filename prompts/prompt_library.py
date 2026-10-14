
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


# Version 1: Vocabulary question generation
VOCABULARY_QUESTIONS_V1 = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a friendly and encouraging English vocabulary tutor.

            Generate exactly {number_of_questions}
            multiple-choice vocabulary questions.

            Topic: {topic}
            Learner level: {level}

            Adapt the vocabulary and question difficulty to the
            specified learner level.

            Each question must contain:
            - A target vocabulary word
            - A question testing its meaning or correct usage
            - Four possible answers labelled A, B, C and D
            - Exactly one correct answer
            - A clear definition of the target word
            - One natural example sentence using the word correctly
            - A short explanation of why the answer is correct

            Make the questions useful for learning English.
            Avoid duplicate target words within the same quiz.
            Ensure the correct answer matches the definition
            and the question.

            Do not reveal the correct answer inside the question.
            Return output matching the application's
            structured output schema.
            """,
        ),
        ("human", "Generate the vocabulary quiz."),
    ]
)


# Central prompt registry
PROMPT_REGISTRY = {
    "grammar_questions": GRAMMAR_QUESTIONS_V1,
    "vocabulary_questions": VOCABULARY_QUESTIONS_V1,
}
