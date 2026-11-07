import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

# Load .env from the project root
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("DATABASE_URL not found in .env")

try:
    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_database();")
            db_name = cur.fetchone()[0]

            print("Connected to:", db_name)

    print("PostgreSQL connection successful!")

except psycopg.Error as e:
    print("PostgreSQL connection failed.")
    print("Error:", e)
