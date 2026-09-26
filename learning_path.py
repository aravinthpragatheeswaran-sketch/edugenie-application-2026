from schemas import LearningPathResponse


def get_learning_recommendations(topic: str, level: str, weeks: int) -> LearningPathResponse:
    phases = ["Foundations", "Core concepts", "Guided practice", "Independent project"]
    steps = []
    for week in range(1, weeks + 1):
        phase = phases[(week - 1) % len(phases)]
        steps.append(
            {
                "week": week,
                "title": f"{phase}: {topic}",
                "focus": f"Study {topic} at {level} level and complete one small practice task.",
            }
        )
    return LearningPathResponse(steps=steps)