from urllib.request import urlopen
from urllib.error import URLError


def fetch_url(url: str) -> str:
    """Fetch text content from a URL using urllib."""
    try:
        with urlopen(url, timeout=10) as resp:
            return resp.read().decode()
    except URLError as exc:
        raise RuntimeError(f"failed to fetch {url}: {exc}")
