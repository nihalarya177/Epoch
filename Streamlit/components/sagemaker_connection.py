import os
import json
import boto3
import pandas as pd

# Set AWS Credentials path
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = ".\.aws\credentials"

# Directories and file names
bucket_name = "epochs-bucket"
butcket_data_dir = "datasets"
local_data_dir = "./temp"
file_name = "iris.csv"

# We shall use client over reource
s3_client = boto3.client("s3")

# Code for uploading file to the bucket
path_to_file = os.path.join(local_data_dir, file_name)
bucket_key = os.path.join(butcket_data_dir, file_name).replace('\\', '/')  # bucket uses linux directory syntax
# s3_client.upload_file(path_to_file, bucket_name, bucket_key)

# # Code for reading data from the buket
# obj = s3_client.get_object(Bucket=bucket_name, Key=bucket_key)
# df = pd.read_csv(obj['Body'])
# print(df.head())

# Code for invoking a lambda function
lambda_client = boto3.client("lambda", region_name="ap-southeast-1")
payload = {"name": "Rahul"}
response = lambda_client.invoke(
        FunctionName="epoch-lambda-2",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload)
    )
print(json.loads(response["Payload"].read().decode())['result'])