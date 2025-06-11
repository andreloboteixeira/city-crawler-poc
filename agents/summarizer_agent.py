class SummaryAgent:
    """Agent that returns the first N words of text as a summary."""

    def summarize(self, text: str, words: int = 20) -> str:
        tokens = text.split()
        return " ".join(tokens[:words])
