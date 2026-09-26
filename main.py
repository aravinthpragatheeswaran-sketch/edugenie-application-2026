from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import settings
from schemas import (
    ExplainRequest,
    QARequest,
    QuizRequest,
    SummaryRequest,
    LearningPathRequest,
    TextResponse,
    QuizResponse,
    LearningPathResponse,
)

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)


# --------------------------------------------------
# Static files
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


# --------------------------------------------------
# Templates
# --------------------------------------------------

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"app_name": settings.app_name},
    )


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "application": settings.app_name,
        "gemini_configured": bool(settings.gemini_api_key),
        "model": settings.gemini_model,
    }


# --------------------------------------------------
# Question Answering
# --------------------------------------------------

@app.post("/qa", response_model=TextResponse)
async def qa(payload: QARequest):

    result = answer_question(
        payload.question
    )

    return TextResponse(
        result=result
    )


# --------------------------------------------------
# Explanation
# --------------------------------------------------

@app.post("/explain", response_model=TextResponse)
async def explain(payload: ExplainRequest):

    result = explain_topic(
        payload.topic,
        payload.level,
    )

    return TextResponse(
        result=result
    )


# --------------------------------------------------
# Quiz
# --------------------------------------------------

@app.post("/quiz", response_model=QuizResponse)
async def quiz(payload: QuizRequest):

    return generate_quiz(
        payload.text,
        payload.count,
    )


# --------------------------------------------------
# Summary
# --------------------------------------------------

@app.post("/summarize", response_model=TextResponse)
async def summarize(payload: SummaryRequest):

    result = summarize_text(
        payload.text,
        payload.length,
    )

    return TextResponse(
        result=result
    )


# --------------------------------------------------
# Learning Path
# --------------------------------------------------

@app.post(
    "/learn/recommendations",
    response_model=LearningPathResponse,
)
async def learning_recommendations(
    payload: LearningPathRequest,
):

    return get_learning_recommendations(
        payload.topic,
        payload.level,
        payload.weeks,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )