from utils.registry import FLOW_REGISTRY
import flows.city_crawler
import flows.notes_organizer
import flows.multi_agent_crawl


def test_flows_registered():
    assert "city_crawler_flow" in FLOW_REGISTRY
    assert "notes_organizer_flow" in FLOW_REGISTRY
    assert "crawling_summary_flow" in FLOW_REGISTRY
