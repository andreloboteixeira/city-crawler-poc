# City Crawler PoC - Learning Prefect & crawl4ai

This repository contains a proof-of-concept for building a city knowledge base crawler using **Prefect** (workflow orchestration) and **crawl4ai** (web crawling).

## Learning Objectives

- Understand Prefect's core concepts: flows, tasks, and orchestration
- Learn crawl4ai's capabilities for AI-focused web scraping
- Combine both tools to build a scalable city data collection system

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Basic Examples

#### Understanding Prefect Basics
```bash
python ./basic_concepts/01_basic_prefect.py
```
This demonstrates:
- **Tasks**: Individual units of work (`@task`)
- **Flows**: Orchestration containers (`@flow`)
- **Data passing**: How results flow between tasks

#### Understanding crawl4ai Basics
```bash
python ./basic_concepts/02_basic_crawl4ai.py
```
This demonstrates:
- **AsyncWebCrawler**: The main crawling interface
- **Configuration options**: Headless mode, selectors, filters
- **Result handling**: Extracting content, metadata, and markdown

#### Combined Prefect + crawl4ai
```bash
python ./src/main.py
```
This demonstrates:
- **Async tasks**: Using crawl4ai within Prefect tasks
- **Data persistence**: Saving crawled data to JSON files and markdown
- **Error handling**: Managing failed crawls gracefully
