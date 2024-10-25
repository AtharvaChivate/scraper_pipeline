import boto3
import pandas as pd
from io import StringIO
import logging

def combine_and_clean():
    bucket_name = "my-hackathon-data-bucket"  # Replace with your bucket name
    devpost_key = 'devpost.csv'
    mlh_key = 'mlh.csv'
    combined_key = 'combined.csv'

    # Create an S3 client
    s3_client = boto3.client('s3')

    # Fetch Devpost CSV from S3
    devpost_obj = s3_client.get_object(Bucket=bucket_name, Key=devpost_key)
    devpost_csv = devpost_obj['Body'].read().decode('utf-8')
    df_devpost = pd.read_csv(StringIO(devpost_csv))

    # Fetch MLH CSV from S3
    mlh_obj = s3_client.get_object(Bucket=bucket_name, Key=mlh_key)
    mlh_csv = mlh_obj['Body'].read().decode('utf-8')
    df_mlh = pd.read_csv(StringIO(mlh_csv))

    # Perform your combination and cleaning
    df_combined = pd.concat([df_devpost, df_mlh])
    df_cleaned = df_combined.drop_duplicates().reset_index(drop=True)

    # Save the cleaned CSV file back to S3
    csv_buffer = StringIO()
    df_cleaned.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=bucket_name, Key=combined_key, Body=csv_buffer.getvalue())
    logging.info(f"Successfully saved combined CSV to S3: {bucket_name}/{combined_key}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    combine_and_clean()
