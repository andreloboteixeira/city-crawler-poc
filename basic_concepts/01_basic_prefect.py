from prefect import flow, task
from datetime import datetime
import time


@task
def extract_data(source: str):
    """Basic task that simulates data extraction"""
    print(f"Extracting data from {source}")
    time.sleep(1)  # Simulate work
    return f"Data from {source} at {datetime.now()}"


@task
def transform_data(data: str):
    """Basic task that simulates data transformation"""
    print(f"Transforming: {data}")
    time.sleep(0.5)  # Simulate work
    return data.upper()


@task
def load_data(data: str):
    """Basic task that simulates data loading"""
    print(f"Loading: {data}")
    return f"Successfully loaded: {data}"


@flow(name="Basic ETL Flow")
def basic_etl_flow(source: str = "example-source"):
    """A simple ETL flow demonstrating Prefect concepts"""
    raw_data = extract_data(source)
    transformed_data = transform_data(raw_data)
    result = load_data(transformed_data)
    return result


if __name__ == "__main__":
    # Run the flow locally
    result = basic_etl_flow("test-website")
    print(f"\nFlow completed with result: {result}") 