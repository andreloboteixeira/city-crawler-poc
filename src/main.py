import asyncio
from prefect import flow, task
from crawl4ai import AsyncWebCrawler
from datetime import datetime
import json


@task
async def crawl_city_website(city_name: str, url: str):
    """Task to crawl a city website and extract information"""
    print(f"Starting crawl for {city_name}: {url}")
    
    crawler_config = {
        "headless": True,
        "verbose": False
    }

    async with AsyncWebCrawler(**crawler_config) as crawler:
        result = await crawler.arun(
            url=url,
            word_count_threshold=50,
            exclude_external_links=True
        )
        
        if result.success:
            city_data = {
                "city": city_name,
                "url": url,
                "title": result.metadata.get('title', 'No title'),
                "word_count": result.metadata.get('word_count', 0),
                "crawled_at": datetime.now().isoformat(),
                "content_preview": result.markdown[:500],
                "content": result.markdown,
                "success": True
            }
            print(f"Successfully crawled {city_name} - "
                  f"{len(result.markdown)} chars")
        else:
            city_data = {
                "city": city_name,
                "url": url,
                "error": f"Failed to crawl: {result.status_code}",
                "crawled_at": datetime.now().isoformat(),
                "success": False
            }
            print(f"Failed to crawl {city_name}: {result.status_code}")
        
        return city_data


@task
def save_city_data(city_data: dict):
    """Task to save crawled city data"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    city_name = city_data['city']
    
    # Save JSON file
    json_filename = f"city_data_{city_name}_{timestamp}.json"
    with open(json_filename, 'w') as f:
        json.dump(city_data, f, indent=2)
    
    # Save markdown content if available
    if city_data.get('content'):
        md_filename = f"city_data_{city_name}_{timestamp}.md"
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(city_data['content'])
    
    print(f"Saved data for {city_name} to {json_filename}")
    return json_filename


@flow(name="City Crawler Flow")
async def city_crawler_flow():
    """Main flow that orchestrates city web crawling"""
    
    # Demo city targets
    city_targets = {
        "calgary": "https://www.calgary.ca/home.html",
        "nova_venecia": "https://www.novavenecia.es.gov.br/"
    }
    
    results = []
    
    # Crawl each city website
    for city_name, url in city_targets.items():
        city_data = await crawl_city_website(city_name, url)
        saved_file = save_city_data(city_data)
        results.append({
            "city": city_name,
            "data": city_data,
            "saved_to": saved_file
        })
    
    print(f"\nCompleted crawling {len(results)} cities")
    return results


if __name__ == "__main__":
    print("Running City Crawler Flow with Prefect + crawl4ai...\n")
    
    # Run the flow
    results = asyncio.run(city_crawler_flow())
    
    # Summary
    print("\n=== Crawl Summary ===")
    for result in results:
        status = "✅ Success" if result["data"]["success"] else "❌ Failed"
        print(f"{result['city']}: {status} -> {result['saved_to']}") 