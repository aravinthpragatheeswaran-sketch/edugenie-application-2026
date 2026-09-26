def explain_topic(topic: str, level: str = "beginner") -> str:
    return (
        f"{topic} is best understood as a set of ideas that work together. "
        f"At a {level} level, start with the purpose, identify the key terms, "
        "and then connect each idea to a small example.\n\n"
        f"A useful first exercise is to explain {topic} in your own words, "
        "then check which part still feels unclear."
    )