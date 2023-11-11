import os
import subprocess

from . import utils

################################################################


def db_url(mount_id, psql_config):
    url = (
        f"postgres://{psql_config.username}@{psql_config.host}"
        f"/dcsm?sslmode=disable&search_path={mount_id}"
    )
    return url


################################################################


def format(bucket_url, mount_id, access_key, secret_key, psql_config):
    database_url = db_url(mount_id, psql_config)

    cmd = [
        "juicefs",
        "format",
        "--storage",
        "s3",
        "--bucket",
        bucket_url,
        "--access-key",
        access_key,
        "--secret-key",
        secret_key,
        database_url,
        mount_id,
    ]
    print(" ".join(cmd))
    env = os.environ
    env.update({"META_PASSWORD": psql_config.password})
    format_process = subprocess.run(
        cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    utils.check_process_return(
        format_process, f"Error formatting JuiceFS mount {mount_id}"
    )
    print(f"Formatted JuiceFS mount {mount_id}")


################################################################


def fix_config(mount_id, psql_config):
    database_url = db_url(mount_id, psql_config)

    """Replace bucket url and remove keys from database"""
    cmd = [
        "juicefs",
        "config",
        database_url,
        "--access-key",
        "",
        "--secret-key",
        "",
        "--force",  # Skip keys validation
    ]
    env = os.environ
    env.update({"META_PASSWORD": psql_config.password})

    print(" ".join(cmd))
    remove_keys_process = subprocess.run(
        cmd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    utils.check_process_return(
        remove_keys_process, f"Error fixing configuration in database {database_url}"
    )
    print(f"Fixed configuration in database {database_url}")


################################################################


def mount(mount_id, local_path, access_key, secret_key, write_access, psql_config):
    env = os.environ
    env.update({"META_PASSWORD": psql_config.password})
    env.update({"AWS_ACCESS_KEY": access_key, "AWS_SECRET_ACCESS_KEY": secret_key})

    database_url = db_url(mount_id, psql_config)

    command = [
        "juicefs",
        "mount",
        "--background",
        database_url,
        local_path,
    ]

    if not write_access:
        command.append("--read-only")
        command.append("--no-bgjob")

    print(
        command,
        {"META_PASSWORD": psql_config.password},
        {"AWS_ACCESS_KEY": access_key, "AWS_SECRET_ACCESS_KEY": secret_key},
    )
    mount_process = subprocess.run(
        command,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    utils.check_process_return(
        mount_process, f"Failed to mount database {database_url}"
    )
