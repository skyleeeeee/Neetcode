import os
from .file_logger import FileLogger
from .db_logger import DbLogger
from .network_logger import NetworkLogger

def get_logger_from_env():
    """Reads LOG_MODE and related vars to return a configured Logger."""
    mode = os.getenv("LOG_MODE", "file").lower()
    if mode == "file":
        path = os.getenv("LOG_FILEPATH", "app.log")
        return FileLogger(path)
    elif mode == "db":
        conn = os.getenv("DB_CONN")
        if not conn:
            raise RuntimeError("DB_CONN must be set for db mode")
        return DbLogger(conn)
    elif mode == "network":
        endpoint = os.getenv("LOG_ENDPOINT")
        if not endpoint:
            raise RuntimeError("LOG_ENDPOINT must be set for network mode")
        return NetworkLogger(endpoint)
    else:
        raise ValueError(f"Unknown LOG_MODE: {mode}")
