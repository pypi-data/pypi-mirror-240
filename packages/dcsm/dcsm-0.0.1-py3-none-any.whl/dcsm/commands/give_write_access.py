import argparse

import psycopg2

from .. import config, database, minio

COMMAND_HELP = "Give a user write access to a mount"


def give_write_access(username=None, mount_id=None, use_minio=False, **kwargs):
    psql_config = config.psql_config(**kwargs)
    connection = database.connect_to_postgres(psql_config)

    if use_minio:
        minio_config = config.minio_config()
        s3_config = config.s3_config()
        access_key, secret_key = minio.give_access(username, mount_id, minio_config, s3_config, write_access=True)
    else:
        access_key, secret_key = database.get_access_keys(connection, mount_id)
    print(access_key, secret_key)
    mount_id = "juicefs-" + mount_id

    database.give_access(connection, username, psql_config, schema=mount_id)
    write_access = True
    try:
        database.save_keys(connection, username, mount_id, write_access, access_key, secret_key)
    except psycopg2.errors.UniqueViolation as e:
        print(f"Failed_to_save_keys: apparently this step was already done: {e}")
    connection.close()


def populate_arg_parser(parser: argparse.ArgumentParser):
    parser.add_argument("username", help="Name of user to give write access.")
    parser.add_argument("mount_id", help="Mount ID to give write access.")
    parser.add_argument("--use_minio", action="store_true", help="Request to use minio")


def run(args: argparse.Namespace):
    give_write_access(**vars(args))


def main():
    parser = argparse.ArgumentParser()
    populate_arg_parser(parser)
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
