import os

import requests

metadata_endpoint = os.environ["METADATA_ENDPOINT"]


def exists_movie(metadata_id: int) -> bool:
    metadata_response = requests.get(f"{metadata_endpoint}/{metadata_id}")
    return metadata_response.status_code == 200
