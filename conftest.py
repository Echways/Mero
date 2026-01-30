import os
import sys
from pathlib import Path

import django

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR / "TimeTicket"
MANAGE_PATH = PROJECT_DIR / "manage.py"

project_path = str(PROJECT_DIR.resolve())
base_path = str(BASE_DIR.resolve())

if MANAGE_PATH.exists():
    if project_path in sys.path:
        sys.path.remove(project_path)
    sys.path.insert(0, project_path)

if base_path in sys.path:
    sys.path.remove(base_path)
sys.path.insert(1, base_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TimeTicket.settings")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DATABASE_URL", "sqlite:///db.sqlite3")

django.setup()
