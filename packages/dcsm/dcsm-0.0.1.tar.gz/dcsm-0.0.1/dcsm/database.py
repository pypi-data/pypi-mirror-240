import psycopg2
from psycopg2 import sql

from . import config

################################################################


def connect_to_postgres(psql_config):
    database_name = psql_config.database
    HOST = psql_config.host
    PORT = psql_config.port
    ADMIN_USERNAME = psql_config.username
    ADMIN_PASSWORD = psql_config.password

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=ADMIN_USERNAME,
            password=ADMIN_PASSWORD,
            database=database_name,
        )
        connection.autocommit = True

    except Exception as e:
        message = f"Error connecting to Postgres: {e}"
        raise RuntimeError(message).with_traceback(e.__traceback__)

    return connection


################################################################


def create_storage_table(connection):
    # Columns: username, mount_id, write_access, access_key, secret_key
    try:
        cursor = connection.cursor()
        create_table_query = sql.SQL(
            (
                "CREATE TABLE storage ("
                "mount_id VARCHAR(256) NOT NULL UNIQUE PRIMARY KEY,"
                "type VARCHAR(256) NOT NULL,"
                "s3_url VARCHAR(1024) NOT NULL,"
                "s3_bucket VARCHAR(1024) NOT NULL,"
                f"access_key VARCHAR({config.ACCESS_KEY_LENGTH}) NOT NULL,"
                f"secret_key VARCHAR({config.SECRET_KEY_LENGTH}) NOT NULL"
                ")"
            )
        )
        cursor.execute(create_table_query)
        cursor.close()
    except psycopg2.errors.DuplicateTable as e:
        message = f"Cannot create table storage as it already exists\n\tpsql => {e}"
        print(message)
    except Exception as e:
        message = f"Error creating table storage: {e}"
        raise RuntimeError(message).with_traceback(e.__traceback__)


################################################################


def create_users_info_table(connection):
    # Columns: username, mount_id, write_access, access_key, secret_key
    try:
        cursor = connection.cursor()
        create_table_query = sql.SQL(
            (
                "CREATE TABLE users_info ("
                "username VARCHAR(256) NOT NULL,"
                "property VARCHAR(256) NOT NULL,"
                "value VARCHAR(256) NOT NULL, "
                "UNIQUE(username, property))"
            )
        )
        cursor.execute(create_table_query)
        cursor.close()
    except psycopg2.errors.DuplicateTable as e:
        message = f"Cannot create table users as it already exists\n\tpsql => {e}"
        print(message)
    except Exception as e:
        message = f"Error creating table users: {e}"
        raise RuntimeError(message).with_traceback(e.__traceback__)


################################################################


def save_minio_user_credentials(connection, username, password):
    cursor = connection.cursor()

    update_query = sql.SQL(
        ("INSERT INTO users_info " "VALUES ({username}, {prop}, {password})")
    ).format(
        username=sql.Literal(username),
        password=sql.Literal(password),
        prop=sql.Literal("minio_credential"),
    )
    cursor.execute(update_query)
    cursor.close()
    print(f"Saved minio credential for user {username} : {password}")


################################################################


def create_user(connection, name, password):
    cursor = connection.cursor()
    create_user_query = sql.SQL("CREATE USER {name} WITH PASSWORD {password}").format(
        name=sql.Identifier(name),
        password=sql.Literal(password),
    )
    cursor.execute(create_user_query)
    cursor.close()
    print(f"Created Postgres user {name} with password {password}")


################################################################


def create_user_mounts_table(username, connection):
    cursor = connection.cursor()
    create_table_query = sql.SQL(
        (
            "CREATE TABLE {schema}.user_mounts ("
            "mount_id VARCHAR(36) NOT NULL UNIQUE PRIMARY KEY,"
            "write_access BOOLEAN NOT NULL,"
            f"access_key VARCHAR({config.ACCESS_KEY_LENGTH}) NOT NULL,"
            f"secret_key VARCHAR({config.SECRET_KEY_LENGTH}) NOT NULL"
            ")"
        )
    ).format(
        schema=sql.Identifier(username),
    )
    cursor.execute(create_table_query)
    cursor.close()


################################################################


def delete_user(connection, name, psql_config):
    cursor = connection.cursor()
    delete_user_query = sql.SQL(
        "DELETE FROM users_info WHERE username = {name}"
    ).format(
        name=sql.Literal(name),
    )
    cursor.execute(delete_user_query)

    delete_user_query = sql.SQL(
        "REVOKE CONNECT ON DATABASE {database} FROM {name}"
    ).format(
        name=sql.Identifier(name),
        database=sql.Identifier(psql_config.database),
    )
    cursor.execute(delete_user_query)
    delete_user_query = sql.SQL("DROP OWNED BY {name}").format(
        name=sql.Identifier(name),
    )
    cursor.execute(delete_user_query)

    delete_user_query = sql.SQL("DROP USER {name}").format(
        name=sql.Identifier(name),
    )
    cursor.execute(delete_user_query)

    cursor.close()
    print(f"Deleted Postgres user {name}")


################################################################


def create_schemas(connection, name, username="admin"):
    """Create new database.

    Args:
        connection (psycopg2.connection): Connection to Postgres.
        name (str): Name of the new database.

    Returns:
        database_url (str): URL for the database.
    """

    cursor = connection.cursor()
    create_schemas_query = sql.SQL(
        "CREATE SCHEMA {name} AUTHORIZATION {username}"
    ).format(username=sql.Identifier(username), name=sql.Identifier(name))
    cursor.execute(create_schemas_query)
    cursor.close()
    print(f"Created schemas {username}")


################################################################


def delete_schemas(connection, name):
    cursor = connection.cursor()
    delete_database_query = sql.SQL("DROP SCHEMA {name} CASCADE").format(
        name=sql.Identifier(name),
    )
    cursor.execute(delete_database_query)
    cursor.close()
    print(f"Deleted schemas {name}")


################################################################


def get_access_keys(connection, mount_id):
    """Return the global access to a mount point

    Connection must be initiated on the relevant database.
    """
    mount_id = "juicefs-" + mount_id

    access_key_query = sql.SQL(
        "SELECT access_key, secret_key from storage where mount_id = {mount_id}"
    ).format(
        mount_id=sql.Literal(mount_id),
    )
    print(access_key_query)
    cursor = connection.cursor()
    cursor.execute(access_key_query)
    access_key, secret_key = [e for e in cursor][0]
    return access_key, secret_key


################################################################


def get_mount_info(connection, mount_id, psql_config):
    """Return the global access to a mount point

    Connection must be initiated on the relevant database.
    """
    mount_id = "juicefs-" + mount_id

    access_key_query = sql.SQL(
        "SELECT access_key, secret_key from storage where mount_id = {mount_id}"
    ).format(
        mount_id=sql.Literal(mount_id),
    )
    print(access_key_query)
    cursor = connection.cursor()
    cursor.execute(access_key_query)
    access_key, secret_key = [e for e in cursor][0]
    return access_key, secret_key


################################################################


def get_user_mount_info(connection, mount_id, psql_config):
    """Return the global access to a mount point

    Connection must be initiated on the relevant database.
    """

    access_key_query = sql.SQL(
        "SELECT access_key, secret_key from {username}.user_mounts where mount_id = {mount_id}"
    ).format(
        username=sql.Identifier(psql_config.username),
        mount_id=sql.Literal(mount_id),
    )
    print(access_key_query)
    cursor = connection.cursor()
    cursor.execute(access_key_query)
    access_key, secret_key = [e for e in cursor][0]
    return access_key, secret_key


################################################################


def give_access(connection, username, psql_config, schema=None, write_access=True):
    """Give user write access to database.

    Connection must be initiated on the relevant database.
    """

    if schema is None:
        schema = username
    privileges = "SELECT, INSERT, UPDATE, DELETE" if write_access else "SELECT"
    grant_table_privileges_query = sql.SQL(
        "GRANT {privileges} ON ALL TABLES IN SCHEMA {schema} TO {username}"
    ).format(
        privileges=sql.SQL(privileges),
        schema=sql.Identifier(schema),
        username=sql.Identifier(username),
    )
    cursor = connection.cursor()
    cursor.execute(grant_table_privileges_query)

    grant_sequence_privileges_query = sql.SQL(
        "GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA {schema} TO {username}"
    ).format(
        schema=sql.Identifier(schema),
        username=sql.Identifier(username),
    )
    cursor.execute(grant_sequence_privileges_query)

    grant_table_privileges_query = sql.SQL(
        "GRANT USAGE ON SCHEMA {schema} TO {username}"
    ).format(
        schema=sql.Identifier(schema),
        username=sql.Identifier(username),
    )
    cursor.execute(grant_table_privileges_query)

    cursor.close()
    print(f"Gave write access to schema {psql_config.database}.{schema}")


################################################################


def save_keys(connection, username, mount_id, write_access, access_key, secret_key):
    """Save user's access and secret keys to database.

    If entry already exists for mount_id + write_access, update it.
    """

    cursor = connection.cursor()
    update_query = sql.SQL(
        (
            "INSERT INTO {username}.user_mounts "
            "VALUES ({mount_id}, {write_access}, {access_key}, {secret_key})"
        )
    ).format(
        username=sql.Identifier(username),
        mount_id=sql.Literal(mount_id),
        write_access=sql.Literal(write_access),
        access_key=sql.Literal(access_key),
        secret_key=sql.Literal(secret_key),
    )
    print(update_query)
    cursor.execute(update_query)
    cursor.close()
    print(f"Saved keys for mount {mount_id}")
