from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

from app import create_app

# The Flask application instance
app = create_app()

if __name__ == "__main__":
    # For running with python wsgi.py
    port = int(os.environ.get("PORT", 8000))
    # Note: Use Gunicorn in production!
    app.run(host="0.0.0.0", port=port, debug=True)
