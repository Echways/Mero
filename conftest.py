import os
import sys
from pathlib import Path

import django

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TimeTicket.settings")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DATABASE_URL", "sqlite:///db.sqlite3")

django.setup()
