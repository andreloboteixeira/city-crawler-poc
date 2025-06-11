from unittest.mock import patch

from flows.city_crawler import city_crawler_flow
from flows.notes_organizer import notes_organizer_flow
from flows.multi_agent_crawl import crawling_summary_flow


def test_city_crawler_flow():
    with patch('flows.city_crawler.fetch_url', return_value='<html>hi</html>'):
        files = city_crawler_flow()
        assert files


def test_notes_organizer_flow():
    todos = notes_organizer_flow("Task one!\nTask two!")
    assert len(todos) == 2


def test_crawling_summary_flow():
    with patch('flows.multi_agent_crawl.fetch_url', return_value='one two three four five six'):
        summary = crawling_summary_flow()
        assert summary.split()[:3] == ['one', 'two', 'three']
