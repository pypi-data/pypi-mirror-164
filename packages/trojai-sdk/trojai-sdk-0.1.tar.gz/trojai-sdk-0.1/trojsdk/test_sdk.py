from trojsdk.client import TrojClient
from trojsdk.core.data_utils import load_json_from_disk
from pathlib import Path


def test_sdk():
    config = load_json_from_disk(Path("testing_config.json"))
    print(config["auth_config"]["auth_keys"]["id_token"])
    client = TrojClient(
        api_endpoint=config["auth_config"]["api_endpoint"], api_key="api"
    )
    client.set_credentials(
        id_token=config["auth_config"]["auth_keys"]["id_token"],
        refresh_token=config["auth_config"]["auth_keys"]["refresh_token"],
        api_key=config["auth_config"]["auth_keys"]["api_key"],
    )
    
    docker_metadata = {
        "docker_image_url": "trojai/troj-engine-base-nlp:fbb0186ecdbd3da67e583bb773ecae1395ae1262",
        "docker_secret_name": "trojaicreds"
    }

    res = client.post_job(config_json=config, docker_metadata=docker_metadata)
    assert res["status_code"] == 200
