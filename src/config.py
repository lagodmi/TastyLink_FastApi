import os
from dotenv import load_dotenv


load_dotenv()


USER = os.getenv("POSTGRES_USER", "user")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB = os.getenv("POSTGRES_DB", "TastyLink_db")
HOST = os.getenv("DB_HOST", "db")
PORT = os.getenv("DB_PORT", "5432")


DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
ECHO = True
