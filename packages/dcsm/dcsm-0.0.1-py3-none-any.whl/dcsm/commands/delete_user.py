import argparse

import psycopg2

from .. import config, database, minio

COMMAND_HELP = "Delete a user in a DCSM serve"


def delete_user(username=None, use_minio=False, **kwargs):
    """Delete Minio and Postgres user."""

    psql_config = config.psql_config(**kwargs)

    if use_minio:
        minio_config = config.minio_config()
        minio.delete_user(username, minio_config)

    connection = database.connect_to_postgres(psql_config)

    try:
        database.delete_schemas(connection, username)
    except psycopg2.errors.InvalidSchemaName as e:
        print(f"Cannot delete user schema: {e}")
    try:
        database.delete_user(connection, username, psql_config)
    except psycopg2.errors.UndefinedObject as e:
        print(f"Cannot delete user: {e}")
    connection.close()


def populate_arg_parser(parser: argparse.ArgumentParser):
    parser.add_argument("username", help="Name of user to delete.")
    parser.add_argument("--use_minio", action="store_true", help="Request to use minio")


def run(args: argparse.Namespace):
    delete_user(**vars(args))


def main():
    parser = argparse.ArgumentParser()
    populate_arg_parser(parser)
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
