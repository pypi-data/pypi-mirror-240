import argparse

from .. import database, juicefs

################################################################

COMMAND_HELP = "Mount a JuiceFS directory to a local path"


def mount(
    host=None,
    port=None,
    mount_id=None,
    local_path=None,
    username=None,
    postgres_password=None,
    read_only=None,
    database_name="dcsm",
):
    psql_config = argparse.Namespace(
        database=database_name,
        host=host,
        port=port,
        username=username,
        password=postgres_password,
    )
    print(psql_config)
    connection = database.connect_to_postgres(psql_config)
    write_access = not read_only

    mount_id = "juicefs-" + mount_id
    access_key, secret_key = database.get_user_mount_info(connection, mount_id, psql_config)
    juicefs.mount(mount_id, local_path, access_key, secret_key, write_access, psql_config)

    write_access_message = "with write access" if write_access else "with read-only access"
    print(f"Mounted {mount_id} to {local_path} {write_access_message}")


################################################################


def populate_arg_parser(parser: argparse.ArgumentParser):
    parser.add_argument(
        "database_host_port",
        help="Host and port of database, formatted as host.com or host.com:5432.",
    )
    parser.add_argument("mount_id", help="ID of mount directory")
    parser.add_argument("local_path", help="Local path to mount to")
    parser.add_argument("--username", help="Username")
    parser.add_argument("--postgres_password", help="Postgres password")
    parser.add_argument("--read-only", action="store_true", help="Mount without write access")


def run(args: argparse.Namespace):
    print(args.database_host_port.split(":"))
    args.host, args.port = args.database_host_port.split(":")
    del args.database_host_port

    if not args.read_only:
        try:
            mount(**vars(args))
            return

        except Exception as e:
            print(e)
            print("Could not mount with write access. Trying read-only access.")
            raise e

    try:
        mount(
            args.database_host_port,
            args.mount_id,
            args.local_path,
            args.username,
            args.postgres_password,
        )
    except Exception as e:
        print(e)


def main():
    parser = argparse.ArgumentParser()
    populate_arg_parser(parser)
    args = parser.parse_args()
    run(args)


################################################################
if __name__ == "__main__":
    main()
