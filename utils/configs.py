from dotenv import load_dotenv
import configparser
import os
from pathlib import Path

env_path = Path.cwd().resolve() / ".env"
config_path = Path.cwd().resolve() / "config" / "config.conf"

load_dotenv(env_path)
parser = configparser.ConfigParser()
parser.read(config_path)

## Environment Variables
AWS_ACCESS_KEY = os.environ["aws_access_key_id"]
AWS_SECRET_KEY = os.environ["aws_secret_Access_key"]
AWS_SESSION_TOKEN = os.environ["aws_session_token"]
REDDIT_CLIENT_ID = os.environ["reddit_client_id"]
REDDIT_SECRET_KEY = os.environ["reddit_secret_key"]

## Configurations
DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USER = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET = parser.get('aws', 'aws_bucket_name')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)