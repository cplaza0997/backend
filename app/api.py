from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")


class UserCredentials(BaseModel):
    user: str
    password: str


def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


@app.post("/login")
def login(credentials: UserCredentials):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"""SELECT EXISTS(SELECT 1 FROM users
             WHERE username='{credentials.user}'
             AND password='{credentials.password}');"""
    cursor.execute(query, (credentials.user, credentials.password))
    exists = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if exists:
        return {"status": "Authorized"}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/items")
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    items = [{"name": row[0], "quantity": row[1]} for row in rows]
    return {"items": items}


@app.get("/health")
def health_check():
    return {"status": "OK"}
