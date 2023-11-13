import pandas as pd
from minio import Minio
from minio.error import S3Error


def save_data_to_minio(data, minio_endpoint, minio_access_key, minio_secret_key, minio_bucket, minio_data_path):
    """
    Save data to MinIO.

    Parameters:
    - data: Data to be saved (pd.DataFrame).
    - minio_endpoint: MinIO server endpoint (e.g., http://localhost:9000).
    - minio_access_key: MinIO access key.
    - minio_secret_key: MinIO secret key.
    - minio_bucket: MinIO bucket where the data will be stored.
    - minio_data_path: Path to save the data within the MinIO bucket.
    """
    # Initialize MinIO client
    minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False  # Set to True for secure (HTTPS) connection
    )

    try:
        # Convert DataFrame to CSV and save to MinIO
        data_csv = data.to_csv(index=False, sep=';')
        minio_client.put_object(
            bucket_name=minio_bucket,
            object_name=minio_data_path,
            data=io.BytesIO(data_csv.encode('utf-8')),
            length=len(data_csv),
            content_type='application/csv',
        )

        print(f"Data saved to MinIO: {minio_bucket}/{minio_data_path}")
    except S3Error as e:
        print(f"Error saving data to MinIO: {e}")


def load_data_from_minio(minio_endpoint, minio_access_key, minio_secret_key, minio_bucket, minio_data_path):
    """
    Load data from MinIO.

    Parameters:
    - minio_endpoint: MinIO server endpoint (e.g., localhost:9000).
    - minio_access_key: MinIO access key.
    - minio_secret_key: MinIO secret key.
    - minio_bucket: MinIO bucket where the data is stored.
    - minio_data_path: Path to the data within the MinIO bucket.

    Returns:
    - pd.DataFrame: Loaded data.
    """
    # Initialize MinIO client
    minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False  # Set to True for secure (HTTPS) connection
    )

    try:
        # Download data from MinIO
        data = minio_client.get_object(minio_bucket, minio_data_path)
        df = pd.read_csv(data, sep=';')

        return df
    except S3Error as e:
        print(f"Error loading data from MinIO: {e}")
        return None