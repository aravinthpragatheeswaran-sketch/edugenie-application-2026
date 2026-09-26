from pydantic import BaseModel, Field


class ExplainRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=20000)
    level: str = Field(default="beginner", max_length=40)


class QARequest(BaseModel):
    question: str = Field(min_length=1, max_length=20000)


class QuizRequest(BaseModel):
    text: str = Field(min_length=1, max_length=20000)
    count: int = Field(default=5, ge=1, le=10)


class SummaryRequest(BaseModel):
    text: str = Field(min_length=1, max_length=20000)
    length: str = Field(default="short", max_length=20)


class LearningPathRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=200)
    level: str = Field(default="beginner", max_length=40)
    weeks: int = Field(default=4, ge=1, le=24)


class TextResponse(BaseModel):
    result: str


class QuizQuestion(BaseModel):
    question: str
    options: list[str]
    answer: str
    explanation: str


class QuizResponse(BaseModel):
    questions: list[QuizQuestion]


class LearningPathStep(BaseModel):
    week: int
    title: str
    focus: str


class LearningPathResponse(BaseModel):
    steps: list[LearningPathStep]