import requests
from datetime import datetime
from .logger import Logger

class NetworkLogger(Logger):
    """Sends log entries via HTTP POST to a remote service."""
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def log(self, level: str, message: str) -> None:
        payload = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message
        }
        resp = requests.post(self.endpoint, json=payload, timeout=5)
        resp.raise_for_status()
