import boto3
from botocore.exceptions import ClientError

from utils import configs

def connect_to_s3_client():
    """_Connects to S3 client_

    Returns:
        S3 Client
    """
    try:
        s3_client = boto3.client('s3',
                                 aws_access_key_id = configs.AWS_ACCESS_KEY,
                                 aws_secret_access_key = configs.AWS_SECRET_KEY,
                                 region_name = configs.AWS_REGION)
        
        return s3_client

    except ClientError as e:
        print(e)


def create_bucket_if_not_exist(s3_client, bucket_name) -> None:
    """_Create an S3 Bucket_

    Args:
        s3_client: s3 client 
        bucket_name (_str_): _description_
    """
    location = {'LocationConstraint': configs.AWS_REGION}
    try:
        if not bucket_name in (bucket["Name"] for bucket in s3_client.list_buckets()["Buckets"]):
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration = location)
        else:
            print("Bucket Already Exists!")

    except ClientError as e:
        print(e)


def upload_to_s3(s3_client, filepath: str, bucket_name: str, s3_filename: str):
    """Uploads the file to S3 bucket

    Args:
        s3_client : S3 Client
        filepath (str): path to the file that we want to upload
        bucket_name (str): bucket name
        s3_filename (str): object name that will be displyed in s3 bucket
    """
    try:
        s3_client.upload_file(filepath, bucket_name, f"raw/{s3_filename}")
    except ClientError as e:
        print(e)