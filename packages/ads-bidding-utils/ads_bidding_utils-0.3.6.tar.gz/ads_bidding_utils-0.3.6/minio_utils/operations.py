import base64
import io
import pandas as pd
from minio import Minio
from minio.error import S3Error
from kubernetes import client, config


def get_minio_client_and_bucket():
    """
    Load MinIO configuration data from Kubernetes secrets and configmap and create the MinIO client.

    Returns:
    Tuple: A tuple containing MinIO client, the bucket.
    """
    try:
        # Load Kubernetes in-cluster configuration
        config.load_incluster_config()

        # Create a client instance
        v1 = client.CoreV1Api()

        # Access the MinIO secret data
        secret = v1.read_namespaced_secret(name='minio-secret', namespace='kubeflow')
        minio_access_key = secret.data['AWS_ACCESS_KEY_ID']
        minio_secret_key = secret.data['AWS_SECRET_ACCESS_KEY']
        # Decode base64
        minio_access_key = base64.b64decode(minio_access_key).decode('utf-8')
        minio_secret_key = base64.b64decode(minio_secret_key).decode('utf-8')

        # Access the ConfigMap data
        config_map = v1.read_namespaced_config_map(name='ads-bidding-configmap', namespace='kubeflow')
        minio_endpoint = config_map.data['MINIO_ENDPOINT']
        minio_bucket = config_map.data['MINIO_BUCKET']

    except Exception as e:
        # Handle exceptions, e.g., Kubernetes configuration error or missing resources
        raise RuntimeError(f"Error loading MinIO data: {e}")

    # Initialize MinIO client
    minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False  # Set to True for secure (HTTPS) connection
    )

    return minio_client, minio_bucket


def save_csv_data_to_minio(data, minio_client, minio_bucket, minio_data_path, sep=';'):

    """
    Save data to MinIO.

    Parameters:
    - data: Data to be saved (pd.DataFrame).
    - minio_client: MinIO client.
    - minio_bucket: MinIO bucket where the data will be stored.
    - sep: The sep input needed for pd.read_csv.
    - minio_data_path: Path to save the data within the MinIO bucket.
    """

    try:
        # Convert DataFrame to CSV and save to MinIO
        data_csv = data.to_csv(index=False, sep=sep)
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


def load_data_from_minio(minio_client, minio_bucket, minio_data_path, sep=';', compression=None):
    """
    Load data from MinIO.

    Parameters:
    - minio_client: MinIO client.
    - minio_bucket: MinIO bucket where the data is stored.
    - minio_data_path: Path to the data within the MinIO bucket.
    - sep: The sep input needed for pd.read_csv.
    - compression: The sep input needed for pd.read_csv.

    Returns:
    - pd.DataFrame: Loaded data.
    """

    try:
        # Download data from MinIO
        data = minio_client.get_object(minio_bucket, minio_data_path)
        if compression:
            df = pd.read_csv(data, compression=compression, sep=sep)
        else:
            df = pd.read_csv(data, sep=sep)

        return df
    except S3Error as e:
        print(f"Error loading data from MinIO: {e}")
        return None


def save_model_to_minio(model, minio_client, minio_bucket, minio_data_path, temp_data_path='temp_model.h5'):
    """
    Save model to MinIO.

    Parameters:
    - model: keras model to be saved.
    - minio_client: MinIO client.
    - minio_bucket: MinIO bucket where the data will be stored.
    - minio_data_path: Path to save the data within the MinIO bucket.
    """
    model.save(temp_data_path)

    # Upload the model file to Minio
    try:
        minio_client.fput_object(
            bucket_name=minio_bucket,
            object_name=minio_data_path,
            file_path=temp_data_path
        )
        print(f"Data saved to MinIO: {minio_bucket}/{minio_data_path}")
    except S3Error as e:
        print(f"Error saving data to MinIO: {e}")


def load_model_from_minio(minio_client, minio_bucket, minio_data_path, local_model_file_path='temp_model.h5'):
    """
    Load data from MinIO.

    Parameters:
    - minio_client: MinIO client.
    - minio_bucket: MinIO bucket where the data is stored.
    - minio_data_path: Path to the keras model within the MinIO bucket.

    Returns:
    - tensorflow.keras.models.Sequential: The loaded Keras model.
    """

    try:
        # Download the Keras model from MinIO
        minio_client.fget_object(minio_bucket, minio_data_path, local_model_file_path)
        return local_model_file_path

    except S3Error as e:
        print(f"Error loading data from MinIO: {e}")
        return None
