"""CLI to list and run registered workflows."""
import argparse
from utils.registry import FLOW_REGISTRY


def list_flows() -> None:
    for name in FLOW_REGISTRY:
        print(name)


def run_flow(name: str, **kwargs):
    flow = FLOW_REGISTRY.get(name)
    if not flow:
        raise SystemExit(f"Unknown flow: {name}")
    result = flow(**kwargs)
    print(result)


def main():
    parser = argparse.ArgumentParser(description="Prefect workflow orchestrator")
    parser.add_argument("command", choices=["list", "run"])
    parser.add_argument("flow", nargs="?")
    args = parser.parse_args()

    if args.command == "list":
        list_flows()
    elif args.command == "run":
        if not args.flow:
            raise SystemExit("Specify a flow name")
        run_flow(args.flow)


if __name__ == "__main__":
    main()
