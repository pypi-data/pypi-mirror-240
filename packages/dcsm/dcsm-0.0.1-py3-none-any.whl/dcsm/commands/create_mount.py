import argparse
import uuid

import psycopg2
from psycopg2 import sql

from .. import config, database, juicefs

COMMAND_HELP = "Create a mount in a DCSM server"


def generate_mount_id():
    return str(uuid.uuid4())


def create_mount(username=None, use_minio=False, **kwargs):
    """Create S3 directory and Postgres database.

    Returns:
        mount_id (str): Unique identifier for the mount.
    """

    psql_config = config.psql_config(**kwargs)
    s3_config = config.s3_config()
    bucket = s3_config.bucket_name
    mount_id = kwargs.pop("mount_id")
    mount_id = "juicefs-" + mount_id

    if use_minio:
        minio_config = config.minio_config()
        access_key = minio_config.admin_username
        secret_key = minio_config.admin_password
        endpoint = minio_config.url + ":" + minio_config.port
        mount_type = "minio"

    else:
        mount_type = "s3"
        endpoint = kwargs.pop("endpoint")
        access_key = kwargs.pop("access_key")
        secret_key = kwargs.pop("secret_key")

    connection = database.connect_to_postgres(psql_config)
    cursor = connection.cursor()

    create_schemas_query = sql.SQL(
        "INSERT INTO public.storage VALUES ({mount_id}, {type}, {s3_url}, {s3_bucket}, {access_key}, {secret_key})"
    ).format(
        mount_id=sql.Literal(mount_id),
        access_key=sql.Literal(access_key),
        secret_key=sql.Literal(secret_key),
        type=sql.Literal(mount_type),
        s3_url=sql.Literal(endpoint),
        s3_bucket=sql.Literal(bucket),
    )

    try:
        cursor.execute(create_schemas_query)
    except psycopg2.errors.UniqueViolation as e:
        print(f"Cannot create mount point: \n\tpsql => {e}")
        return
    cursor.close()

    database.create_schemas(connection, mount_id)
    connection.close()

    bucket_url = f"{endpoint}/{bucket}"
    juicefs.format(bucket_url, mount_id, access_key, secret_key, psql_config)
    juicefs.fix_config(mount_id, psql_config)

    print(f"Created mount {mount_id}")

    return mount_id


def populate_arg_parser(parser: argparse.ArgumentParser):
    parser.add_argument("--mount_id", help="Give human readable id of the mount", required=True)
    parser.add_argument("--access_key", help="S3 access key")
    parser.add_argument("--secret_key", help="S3 secret access key")
    parser.add_argument("--endpoint", help="S3 endpoint")
    parser.add_argument("--use_minio", action="store_true", help="Request to use minio")


def run(args: argparse.Namespace):
    create_mount(**vars(args))


def main():
    parser = argparse.ArgumentParser()
    populate_arg_parser(parser)
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
