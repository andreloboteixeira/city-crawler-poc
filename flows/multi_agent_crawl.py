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
from agents.summarizer_agent import SummaryAgent
from tools.web import fetch_url
from utils.registry import register_flow


@task
def crawl(url: str) -> str:
    return fetch_url(url)


@task
def summarize(text: str) -> str:
    agent = SummaryAgent()
    return agent.summarize(text)


@register_flow
@flow(name="CrawlerWithSummary")
def crawling_summary_flow(url: str = "https://example.com") -> str:
    html = crawl(url)
    summary = summarize(html)
    return summary
