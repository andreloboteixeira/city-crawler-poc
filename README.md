# Prefect Orchestration Template

This project demonstrates how to orchestrate workflows using Prefect. It includes
examples for simple agents, multi-agent collaboration, and web crawling.

## Project Structure

- `flows/` – Prefect flow definitions
- `agents/` – Reusable agent classes
- `tools/` – Utility tools that agents or flows can use
- `utils/` – Shared utilities like the workflow registry
- `config/` – Configuration files
- `main.py` – CLI for listing and running registered flows

## Example Workflows

- **CityCrawler** – Fetches a web page and saves metadata
- **NotesOrganizer** – Converts notes ending with `!` into TODO items
- **CrawlerWithSummary** – Crawls a page and summarizes the text using two agents

Run `python main.py list` to see available workflows.
Run `python main.py run <flow_name>` to execute one.

## Extending

Create new flows in `flows/` and decorate them with `@register_flow` from
`utils.registry`. They will automatically appear in the CLI.

Agents and tools can be added under `agents/` and `tools/` to build more complex
workflows.

## Testing

Install dev dependencies and run `pytest` to execute the tests.
