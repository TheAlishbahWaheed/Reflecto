import os
import sys

# Make the project root (where app.py, data.py, templates/, static/ live)
# importable, since this file runs from inside /api.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app  # noqa: E402  (Flask app instance, used as the WSGI handler)
