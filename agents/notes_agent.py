from typing import List

class NotesOrganizerAgent:
    """Simple agent that converts raw notes into TODO items."""

    def organize(self, notes: str) -> List[str]:
        todos = []
        for line in notes.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.endswith("!"):
                todos.append(f"TODO: {line[:-1]}")
        return todos
