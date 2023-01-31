import boto3
# from decouple import config
import os


dynamo_resource = boto3.resource(
    "dynamodb",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID_"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY_"),
    region_name=os.environ.get("AWS_REGION_"),
)


# dynamo_resource = boto3.resource(
#     "dynamodb",
#     aws_access_key_id="AKIAXVR7NSEJCIWZISEA",
#     aws_secret_access_key="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",
#     region_name=os.getenv("AWS_REGION"),
# )

user_tab = dynamo_resource.Table("user_table")
