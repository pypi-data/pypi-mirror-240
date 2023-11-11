import argparse

import psycopg2
from psycopg2 import sql

from .. import config, database, minio
from ..utils import generate_password

COMMAND_HELP = "Create a user in a DCSM server"


def create_user(username, use_minio=False, **kwargs):
    """Create Minio and Postgres user, along with table containing user info.

    Args:
        username (str): Username to create.

    Returns:
        password (str): Postgres password.
    """

    psql_config = config.psql_config(**kwargs)
    connection = database.connect_to_postgres(psql_config)

    if use_minio:
        minio_password = generate_password()
        minio_config = config.minio_config()
        minio.create_user(username, minio_password, minio_config)
        database.save_minio_user_credentials(connection, username, minio_password)

    postgres_user_password = generate_password()
    try:
        database.create_user(connection, username, postgres_user_password)
        database.create_schemas(connection, username)
        database.create_user_mounts_table(username, connection)

        cursor = connection.cursor()
        grant_privileges_query = sql.SQL("GRANT CONNECT ON DATABASE {database} TO {username}").format(
            database=sql.Identifier(psql_config.database),
            username=sql.Identifier(username),
        )
        cursor.execute(grant_privileges_query)
        cursor.close()
        database.give_access(connection, username, psql_config)
        connection.close()
        print(f"login: {username}\npassword: {postgres_user_password}")
    except psycopg2.errors.DuplicateObject as e:
        print(f"Cannot create user {username}: {e}")


################################################################


def populate_arg_parser(parser: argparse.ArgumentParser):
    parser.add_argument("username", help="Name of user to create.")
    parser.add_argument("--reset", action="store_true", help="Reset the configuration")
    parser.add_argument("--use_minio", action="store_true", help="Request to use minio")


def run(args: argparse.Namespace):
    create_user(**vars(args))


def main():
    parser = argparse.ArgumentParser()
    populate_arg_parser(parser)
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
