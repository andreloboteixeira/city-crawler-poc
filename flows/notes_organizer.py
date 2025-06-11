try:
    from prefect import flow, task
except ImportError:
    def flow(*args, **kwargs):
        def decorator(fn):
            return fn
        return decorator

    def task(fn=None, **_):
        if fn is not None:
            return fn
        return lambda f: f
from agents.notes_agent import NotesOrganizerAgent
from utils.registry import register_flow


@task
def organize_notes(notes: str) -> list[str]:
    agent = NotesOrganizerAgent()
    return agent.organize(notes)


@register_flow
@flow(name="NotesOrganizer")
def notes_organizer_flow(notes: str = "Buy milk!\nCall mom!\nRead book") -> list[str]:
    return organize_notes(notes)
