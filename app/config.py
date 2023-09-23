import secrets

SECRET_KEY = secrets.token_hex(32)

ALGORITHM = "HS256"

DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"
