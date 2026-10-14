
import json
import os
from typing import Literal

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

from prompts.prompt_library import PROMPT_REGISTRY


MODEL_NAME = "gemini-3.1-flash-lite"


class GrammarQuestion(BaseModel):
    """Schema for one multiple-choice grammar question."""

    id: int = Field(ge=1, description="Question number")
    question: str = Field(min_length=1)
    options: dict[Literal["A", "B", "C", "D"], str] = Field(
        description="Four answer options labelled A, B, C and D"
    )
    correct_answer: Literal["A", "B", "C", "D"]
    explanation: str = Field(min_length=1)


class GrammarQuiz(BaseModel):
    """Schema for a complete grammar quiz."""

    topic: str = Field(min_length=1)
    level: str = Field(min_length=1)
    questions: list[GrammarQuestion] = Field(min_length=1)


class VocabularyQuestion(BaseModel):
    """Schema for one vocabulary multiple-choice question."""

    id: int = Field(ge=1, description="Question number")
    word: str = Field(min_length=1, description="Target vocabulary word")
    question: str = Field(
        min_length=1,
        description="Question testing the meaning or usage of the word",
    )
    options: dict[Literal["A", "B", "C", "D"], str] = Field(
        description="Four possible meanings or answers labelled A, B, C and D"
    )
    correct_answer: Literal["A", "B", "C", "D"]
    definition: str = Field(min_length=1)
    example_sentence: str = Field(min_length=1)
    explanation: str = Field(min_length=1)


class VocabularyQuiz(BaseModel):
    """Schema for a complete vocabulary quiz."""

    topic: str = Field(min_length=1)
    level: str = Field(min_length=1)
    questions: list[VocabularyQuestion] = Field(min_length=1)


def _get_api_key() -> str:
    """Read the Google API key from the environment or Streamlit secrets."""

    api_key = os.getenv("GOOGLE_API_KEY")

    if api_key:
        return api_key

    try:
        api_key = st.secrets.get("GOOGLE_API_KEY")
    except Exception:
        api_key = None

    if not api_key:
        raise ValueError(
            "Google API key not found. Add GOOGLE_API_KEY to "
            ".streamlit/secrets.toml or set the GOOGLE_API_KEY "
            "environment variable."
        )

    return api_key


def _get_structured_model(schema: type[BaseModel]):
    """Create a Gemini model that returns output matching a Pydantic schema."""

    model = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        google_api_key=_get_api_key(),
        temperature=0.3,
    )

    return model.with_structured_output(schema)


def _validate_options(questions: list[dict]) -> None:
    """Check that every question has exactly four labelled options."""

    expected_labels = {"A", "B", "C", "D"}

    for question in questions:
        if set(question["options"].keys()) != expected_labels:
            raise ValueError(
                f"Question {question['id']} must contain options A, B, C and D."
            )


def generate_grammar_questions(
    topic: str,
    level: str,
    number_of_questions: int = 3,
) -> dict:
    """Generate a validated grammar quiz as a Python dictionary."""

    if not topic.strip():
        raise ValueError("Grammar topic cannot be empty.")

    if not level.strip():
        raise ValueError("Learner level cannot be empty.")

    if not 1 <= number_of_questions <= 10:
        raise ValueError(
            "number_of_questions must be between 1 and 10."
        )

    structured_model = _get_structured_model(GrammarQuiz)

    prompt = PROMPT_REGISTRY["grammar_questions"]
    chain = prompt | structured_model

    quiz = chain.invoke(
        {
            "topic": topic,
            "level": level,
            "number_of_questions": number_of_questions,
        }
    )

    if isinstance(quiz, BaseModel):
        quiz_data = quiz.model_dump()
    elif isinstance(quiz, dict):
        quiz_data = GrammarQuiz.model_validate(quiz).model_dump()
    else:
        raise TypeError(
            f"Unexpected structured output type: {type(quiz).__name__}"
        )

    if len(quiz_data["questions"]) != number_of_questions:
        raise ValueError(
            f"Requested {number_of_questions} questions, but Gemini "
            f"returned {len(quiz_data['questions'])}."
        )

    _validate_options(quiz_data["questions"])

    return quiz_data


def generate_vocabulary_questions(
    topic: str,
    level: str,
    number_of_questions: int = 3,
) -> dict:
    """Generate a validated vocabulary quiz as a Python dictionary."""

    if not topic.strip():
        raise ValueError("Vocabulary topic cannot be empty.")

    if not level.strip():
        raise ValueError("Learner level cannot be empty.")

    if not 1 <= number_of_questions <= 10:
        raise ValueError(
            "number_of_questions must be between 1 and 10."
        )

    structured_model = _get_structured_model(VocabularyQuiz)

    prompt = PROMPT_REGISTRY["vocabulary_questions"]
    chain = prompt | structured_model

    quiz = chain.invoke(
        {
            "topic": topic,
            "level": level,
            "number_of_questions": number_of_questions,
        }
    )

    if isinstance(quiz, BaseModel):
        quiz_data = quiz.model_dump()
    elif isinstance(quiz, dict):
        quiz_data = VocabularyQuiz.model_validate(quiz).model_dump()
    else:
        raise TypeError(
            f"Unexpected structured output type: {type(quiz).__name__}"
        )

    if len(quiz_data["questions"]) != number_of_questions:
        raise ValueError(
            f"Requested {number_of_questions} questions, but Gemini "
            f"returned {len(quiz_data['questions'])}."
        )

    _validate_options(quiz_data["questions"])

    return quiz_data


if __name__ == "__main__":
    print("Running Gemini structured-output smoke test...")
    print(f"Model: {MODEL_NAME}")

    try:
        result = generate_vocabulary_questions(
            topic="Education",
            level="Beginner",
            number_of_questions=3,
        )

        print("\nVocabulary smoke test successful.")
        print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as error:
        print("\nVocabulary smoke test failed.")
        print(f"Error type: {type(error).__name__}")
        print(f"Error details: {error}")
        raise SystemExit(1)
