import os

import requests

metadata_root_url = os.environ["METADATA_API_URL"]


def exists_movie(metadata_id: int) -> bool:
    metadata_response = requests.get(f"{metadata_root_url}/{metadata_id}")
    return metadata_response.status_code == 200
