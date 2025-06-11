from typing import Callable, Dict

# Global registry for workflows
FLOW_REGISTRY: Dict[str, Callable] = {}

def register_flow(func: Callable) -> Callable:
    """Decorator to register a Prefect flow."""
    FLOW_REGISTRY[func.__name__] = func
    return func

def get_flow(name: str) -> Callable | None:
    """Retrieve a flow by name."""
    return FLOW_REGISTRY.get(name)

