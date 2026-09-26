def summarize_text(text: str, length: str = "short") -> str:
    sentences = [part.strip() for part in text.replace("\n", " ").split(".") if part.strip()]
    limit = 2 if length == "short" else 4
    summary = ". ".join(sentences[:limit])
    return f"{summary}." if summary else "No summary could be created from the provided text."