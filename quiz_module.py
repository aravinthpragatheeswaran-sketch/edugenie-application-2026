from schemas import QuizResponse


def generate_quiz(text: str, count: int) -> QuizResponse:
    subject = "the provided material"
    words = text.split()
    if words:
        subject = " ".join(words[:8]).rstrip(".,")

    questions = []
    for number in range(1, count + 1):
        questions.append(
            {
                "question": f"What is the best first step when studying {subject}?",
                "options": [
                    "Identify the main idea",
                    "Skip the examples",
                    "Memorize every word immediately",
                    "Avoid asking questions",
                ],
                "answer": "Identify the main idea",
                "explanation": "Starting with the main idea gives the details a useful structure.",
            }
        )
    return QuizResponse(questions=questions)