import argparse

from .. import database, minio

COMMAND_HELP = "Give a user read access to a mount."


def give_read_access(username, mount_id):
    access_key, secret_key = minio.give_access(username, mount_id, write_access=False)

    connection = database.connect_to_postgres(mount_id)
    database.give_access(connection, username, mount_id, write_access=False)
    connection.close()

    user_database_name = username
    connection = database.connect_to_postgres(user_database_name)
    read_access = False
    database.save_keys(connection, mount_id, read_access, access_key, secret_key)
    connection.close()


def populate_arg_parser(parser: argparse.ArgumentParser):
    parser.add_argument("username", help="Name of user to give read access.")
    parser.add_argument("mount_id", help="Mount ID to give read access.")


def run(args: argparse.Namespace):
    give_read_access(**vars(args))


def main():
    parser = argparse.ArgumentParser()
    populate_arg_parser(parser)
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
