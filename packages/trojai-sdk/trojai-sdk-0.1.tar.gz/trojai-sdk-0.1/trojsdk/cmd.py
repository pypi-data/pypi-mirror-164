from pathlib import Path
from trojsdk.client import TrojClient
from trojsdk.core.data_utils import load_json_from_disk

def main():
    import argparse
    parser = argparse.ArgumentParser(prog="trojsdk", description="Troj sdk command line utils")
    parser.add_argument(
        "-config", metavar="-c", type=str, help="Path to the config file"
    )
    args = parser.parse_args()

    if args.config is not None:
        config = load_json_from_disk(Path(args.config))
    else:
        print("no config supplied")
    # config = load_json_from_disk(Path("troj-sdk/testing_config.json"))
    client = TrojClient(api_endpoint="http://localhost:8080/api/v1", api_key="api")

    res = client.post_job(config)
    print(res)
    res = client.get_jobs()
    print(res)


# if __name__ == "__main__":
#     main()
    