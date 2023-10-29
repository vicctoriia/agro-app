from os import getenv
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

PORT = getenv('GUNICORN_PORT', '8080')

bind = f'0.0.0.0:{PORT}'
timeout = getenv('GUNICORN_TIMEOUT', '1000')
threads = getenv('GUNICORN_THREADS', '100')
worker_class = getenv('GUNICORN_WORKER_CLASS', 'gevent')
loglevel = getenv('GUNICORN_LOG_LEVEL', 'info')
errorlog = getenv('GUNICORN_ERROR_LOG', '-')
accesslog = getenv('GUNICORN_ACCESS_LOG', '-')
