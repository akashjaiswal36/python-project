import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='akash-boto3-example-123-sfdsfsd',
        CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
    },
)