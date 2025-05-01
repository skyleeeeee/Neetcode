from datetime import datetime
from .logger import Logger

class FileLogger(Logger):
    """Writes log entries to a local file."""
    def __init__(self, filepath: str):
        self.filepath = filepath

    def log(self, level: str, message: str) -> None:
        timestamp = datetime.now().isoformat()
        with open(self.filepath, "a") as f:
            f.write(f"{timestamp} [{level}] {message}\n")
