import os
import sys
from datetime import datetime

from airflow import DAG
from datetime import datetime
from airflow.decorators import task, dag
from airflow.utils.dates import days_ago

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'Shail Shah',
    'start_date': days_ago(1)
}

file_postfix = datetime.now().strftime("%Y%m%d")

@dag(schedule_interval='@daily', default_args=default_args, catchup=False)
def etl_reddit_aws():
    
    @task
    def reddit_extraction() -> str:
        filepath = reddit_pipeline(filename=f"reddit_{file_postfix}",
                        subreddit="dataengineering",
                        time_filter="day",
                        limit=5)
        return filepath
    
    @task
    def s3_upload(filepath: str):
        upload_s3_pipeline(filepath)

    s3_upload(reddit_extraction())

dag = etl_reddit_aws()