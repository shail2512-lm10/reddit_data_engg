from etls.aws_etl import connect_to_s3_client, create_bucket_if_not_exist, upload_to_s3
from utils.configs import AWS_BUCKET


def upload_s3_pipeline(filepath):
    s3 = connect_to_s3_client()
    create_bucket_if_not_exist(s3, AWS_BUCKET)
    upload_to_s3(s3, filepath, AWS_BUCKET, filepath.split('/')[-1])