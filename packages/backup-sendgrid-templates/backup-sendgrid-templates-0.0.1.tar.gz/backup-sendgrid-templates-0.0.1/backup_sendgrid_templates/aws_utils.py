import logging

import boto3


def create_file_on_s3(bucket_name, object_key, file_content):
    session = boto3.Session()
    # Creating S3 Resource From the Session.
    s3 = session.resource("s3")
    s3_object = s3.Object(bucket_name, object_key)
    result = s3_object.put(Body=bytearray(file_content, encoding="utf-8"))
    res = result.get("ResponseMetadata")
    if res.get("HTTPStatusCode") == 200:
        logging.info(f"File {object_key} uploaded successfully")
        return True
    logging.info(f"File {object_key} not uploaded.")
    return False
