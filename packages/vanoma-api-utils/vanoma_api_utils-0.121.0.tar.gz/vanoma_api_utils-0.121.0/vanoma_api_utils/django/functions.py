import json
import boto3
from typing import Union, Optional
from django.conf import settings



s3client = boto3.client(
    "s3",
    region_name=settings.AWS_S3_REGION_NAME,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)


def delete_object_from_s3(s3key: str) -> None:
    """
    Django storages is not deleting objects even when we the delete() on the file.
    """

    if settings.AWS_STORAGE_BUCKET_NAME:
        s3client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=s3key)

def get_object_from_s3(s3key: str) -> bytes:
    """
    Fetches an object from S3 and returns the bytes.
    """

    try:
        if settings.AWS_STORAGE_BUCKET_NAME:
            response = s3client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=s3key)
            return response["Body"].read()
    except s3client.exceptions.NoSuchKey:
        pass

    return None

def get_json_data_from_s3(s3key: str) -> Optional[Union[dict, list]]:
    """
    Fetches a JSON file from S3 and returns the bytes.
    """

    response = get_object_from_s3(s3key)
    if response:
        return json.loads(response.decode("utf-8"))

    return None
