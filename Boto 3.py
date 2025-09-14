import boto3

client = boto3.client('s3')

response = client.get_bucket_acl(
    Bucket='demo-boto3-yr-2025', 
)

print(response) 