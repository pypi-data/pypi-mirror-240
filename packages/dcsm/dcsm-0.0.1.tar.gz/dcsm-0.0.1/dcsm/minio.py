import os
import shutil
import subprocess
import tempfile

################################################################
from . import config
from .utils import check_process_return, generate_password

################################################################


def check_mc():
    path = shutil.which("mc")

    if path is None:
        raise RuntimeError(
            (
                "'mc' is not install on the system: please proceed to installation by following instructions "
                "https://min.io/docs/minio/linux/reference/minio-mc.html#id2"
            )
        )


################################################################


def set_alias(minio_config):
    check_mc()
    set_alias_process = subprocess.run(
        [
            "mc",
            "alias",
            "set",
            minio_config.alias,
            minio_config.url + ":" + minio_config.port,
            minio_config.admin_username,
            minio_config.admin_password,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    check_process_return(set_alias_process, "Error setting MinIO alias local")
    print(f"Set MinIO alias {minio_config.alias}")


################################################################


def create_bucket(s3_config, minio_config):
    create_bucket_process = subprocess.run(
        [
            "mc",
            "mb",
            f"{minio_config.alias}/{s3_config.bucket_name}",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    check_process_return(
        create_bucket_process, f"Error creating MinIO bucket {s3_config.bucket_name}"
    )
    print(f"Created MinIO bucket {s3_config.bucket_name}")


################################################################


def create_user(username, password, minio_config):
    add_user_process = subprocess.run(
        [
            "mc",
            "admin",
            "user",
            "add",
            minio_config.alias,
            username,
            password,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    check_process_return(add_user_process, f"Error creating MinIO user {username}")
    print(f"Created MinIO user {username} with password {password}")


################################################################


def delete_user(username, minio_config):
    delete_user_process = subprocess.run(
        [
            "mc",
            "admin",
            "user",
            "rm",
            minio_config.alias,
            username,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    check_process_return(delete_user_process, f"Error deleting MinIO user {username}")
    print(f"Deleted MinIO user {username}")


################################################################


def give_access(username, mount_id, minio_config, s3_config, write_access=True):
    access_type = "write" if write_access else "read"
    policy_path = generate_policy(mount_id, access_type, minio_config, s3_config)
    policy_name = f"{access_type}_{mount_id}"

    create_policy_entry(policy_name, policy_path, minio_config)

    try:
        attach_policy_to_user(policy_name, username, minio_config)
    except RuntimeError as e:
        print(e)

    access_key, secret_key = generate_user_keys_for_policy(
        username, policy_path, minio_config
    )

    os.remove(policy_path)

    return access_key, secret_key


################################################################


def generate_policy(mount_id, access_type, minio_config, s3_config):
    template_path = os.path.join(
        os.path.dirname(__file__), "minio_policies", f"{access_type}_template.json"
    )

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as file:
        with open(template_path, "r") as template:
            for line in template:
                line = line.replace("{bucket_name}", s3_config.bucket_name)
                line = line.replace("{directory_name}", "juicefs-" + mount_id)
                file.write(line)

    return file.name


################################################################


def create_policy_entry(policy_name, policy_path, minio_config):
    create_policy_process = subprocess.run(
        [
            "mc",
            "admin",
            "policy",
            "create",
            minio_config.alias,
            policy_name,
            policy_path,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    check_process_return(
        create_policy_process, f"Error creating Minio policy {policy_name}"
    )
    print(f"Created Minio policy {policy_name}")


################################################################
def attach_policy_to_user(policy_name, username, minio_config):
    attach_policy_process = subprocess.run(
        [
            "mc",
            "admin",
            "policy",
            "attach",
            minio_config.alias,
            policy_name,
            "--user",
            username,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    check_process_return(
        attach_policy_process,
        f"Error attaching Minio policy {policy_name} to user {username}",
    )
    print(f"Attached Minio policy {policy_name} to user {username}")


################################################################


def generate_user_keys_for_policy(username, policy_path, minio_config):
    access_key = generate_password(config.ACCESS_KEY_LENGTH)
    secret_key = generate_password(config.SECRET_KEY_LENGTH)

    add_policy_proccess = subprocess.run(
        [
            "mc",
            "admin",
            "user",
            "svcacct",
            "add",
            "--access-key",
            access_key,
            "--secret-key",
            secret_key,
            "--policy",
            policy_path,
            minio_config.alias,
            username,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    check_process_return(
        add_policy_proccess, f"Error generating Minio keys for user {username}"
    )
    print(f"Generated Minio keys for user {username}")
    print(f"Access key: {access_key}")
    print(f"Secret key: {secret_key}")

    return access_key, secret_key
