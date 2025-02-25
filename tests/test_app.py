import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app  # Now it should work

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
