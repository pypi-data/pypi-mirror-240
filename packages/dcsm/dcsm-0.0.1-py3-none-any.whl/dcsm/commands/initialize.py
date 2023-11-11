import argparse

################################################################
from .. import config, database, minio

################################################################

COMMAND_HELP = "Initialize DCSM server & bucket"


def create_postgres_database(reset=False):
    psql_config = config.psql_config(reset=reset)
    conn = database.connect_to_postgres(psql_config)
    database.create_storage_table(conn)
    return conn


################################################################


def initialize(reset=False, use_minio=False, **kwargs):
    conn = create_postgres_database(reset=reset)
    s3_config = config.s3_config(reset=reset)

    if use_minio:
        minio_config = config.minio_config(reset=reset)
        minio.set_alias(minio_config)
        database.create_users_info_table(conn)

        try:
            minio.create_bucket(s3_config, minio_config)
        except Exception as e:
            print(e)


################################################################


def populate_arg_parser(parser: argparse.ArgumentParser):
    parser.add_argument("--reset", action="store_true", help="Reset the configuration")
    parser.add_argument("--use_minio", action="store_true", help="Request to use minio")


def run(args: argparse.Namespace):
    initialize(**vars(args))


def main():
    parser = argparse.ArgumentParser()
    populate_arg_parser(parser)
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
