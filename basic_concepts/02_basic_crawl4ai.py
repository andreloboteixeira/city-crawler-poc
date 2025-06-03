import asyncio
from crawl4ai import AsyncWebCrawler


async def crawl_with_options():
    """Example showing crawl4ai configuration options"""
    
    crawler_config = {
        "headless": True,
        "verbose": True
    }
    
    async with AsyncWebCrawler(**crawler_config) as crawler:
        # Crawl with custom options
        result = await crawler.arun(
            url="https://www.calgary.ca/home.html",
            word_count_threshold=50,  # Only extract if content has 50+ words
            css_selector="body",      # Focus on body content
            exclude_external_links=True
        )
        
        print("=== Crawl with Options Results ===")
        print(f"URL: {result.url}")
        print(f"Success: {result.success}")
        print(f"Word Count: {result.metadata.get('word_count', 0)}")
        # print(f"Metadata: {result.metadata}")
        
        if result.success:
            print(f"Content preview: {result.markdown[:300]}...")
            print("Full content:\n\n")
            print(result.markdown)
        
        return result


if __name__ == "__main__":
    print("Running basic crawl4ai...\n")
   
    # Run example with options
    asyncio.run(crawl_with_options())