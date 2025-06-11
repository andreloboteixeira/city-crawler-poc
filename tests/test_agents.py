from agents.notes_agent import NotesOrganizerAgent
from agents.summarizer_agent import SummaryAgent


def test_notes_agent():
    agent = NotesOrganizerAgent()
    notes = "Buy milk!\nCall mom!\nIgnore"
    todos = agent.organize(notes)
    assert todos == ["TODO: Buy milk", "TODO: Call mom"]


def test_summary_agent():
    agent = SummaryAgent()
    text = "one two three four five"
    summary = agent.summarize(text, words=3)
    assert summary == "one two three"
