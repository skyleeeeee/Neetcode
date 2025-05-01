import psycopg2
from datetime import datetime
from .logger import Logger

class DbLogger(Logger):
    """Inserts log entries into a PostgreSQL table."""
    def __init__(self, connection_string: str):
        self.conn = psycopg2.connect(connection_string)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                level VARCHAR(10),
                message TEXT,
                timestamp TIMESTAMP
            );
        """)
        self.conn.commit()

    def log(self, level: str, message: str) -> None:
        timestamp = datetime.now()
        self.cursor.execute(
            "INSERT INTO logs (level, message, timestamp) VALUES (%s, %s, %s)",
            (level, message, timestamp)
        )
        self.conn.commit()
