from datetime import datetime
try:
    from prefect import flow, task
except ImportError:  # Prefect not installed in test env
    def flow(*args, **kwargs):
        def decorator(fn):
            return fn
        return decorator

    def task(fn=None, **_):
        if fn is not None:
            return fn
        return lambda f: f

from tools.web import fetch_url
from utils.registry import register_flow


@task
def crawl(city: str, url: str) -> dict:
    html = fetch_url(url)
    return {
        "city": city,
        "url": url,
        "crawled_at": datetime.utcnow().isoformat(),
        "length": len(html),
    }


@task
def store(data: dict) -> str:
    filename = f"city_data_{data['city']}.json"
    with open(filename, "w", encoding="utf-8") as f:
        import json
        json.dump(data, f, indent=2)
    return filename


@register_flow
@flow(name="CityCrawler")
def city_crawler_flow() -> list[str]:
    cities = {"example": "https://example.com"}
    files = []
    for city, url in cities.items():
        data = crawl(city, url)
        file = store(data)
        files.append(file)
    return files
