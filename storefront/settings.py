import os
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent

TEMPLATE_PATH=os.path.join(BASE_DIR, "templates")

STATIC_PATH=os.path.join(BASE_DIR, "static")

HOST="localhost"

DATABASE_NAME="tma"

COOKIE_SECRET="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="

LOGIN_URL="/login"