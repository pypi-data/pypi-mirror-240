import configparser
import getpass
import os
from argparse import Namespace
from os.path import expanduser

################################################################

ACCESS_KEY_LENGTH = 20
SECRET_KEY_LENGTH = 40
ENV_CONTEXT_VAR = "DCSM_CONTEXT"
DEFAULT_ENV_CONTEXT = "dcsm.ch"

################################################################


def load_env_from_file(env_file_path, env_context=DEFAULT_ENV_CONTEXT):
    """Expects INI-style file. Context taken from environment variable DCSM_CONTEXT.

    The default context is given by DEFAULT_ENV_CONTEXT."""

    env = {}

    if not os.path.exists(env_file_path):
        print(f"Configuration file {env_file_path} not found.")
        return env

    context = os.environ.get(ENV_CONTEXT_VAR, env_context)

    config = configparser.ConfigParser()
    config.optionxform = lambda optionstr: optionstr  # Preserve case
    config.read(env_file_path)
    if context not in config:
        print(f"Context {context} not found in {env_file_path}.")
        return env

    for k, v in config[context].items():
        env[k] = v

    return env


################################################################


def write_env_to_file(env, env_file_path, env_context=DEFAULT_ENV_CONTEXT):
    # Read all contexts
    config = configparser.ConfigParser()
    config.optionxform = lambda optionstr: optionstr  # Preserve case
    config.read(env_file_path)

    # Update context
    context = os.environ.get(ENV_CONTEXT_VAR, env_context)
    if context not in config:
        config[context] = {}
    for k, v in env.items():
        config[context][k] = str(v)

    # Write to file
    with open(env_file_path, "w") as configfile:
        config.write(configfile)

    print(f"Configuration saved to {env_file_path}.")


################################################################

home = expanduser("~")
env_file_path = os.path.join(home, ".dcsm")
env = load_env_from_file(env_file_path)

################################################################


def get_param(key, default=None, is_password=False, reset=False):
    if key in env and reset is False:
        return env[key]
    if key in env and reset is True:
        default = env[key]

    if is_password:
        val = getpass.getpass(f"{key}: ")
    else:
        prompt = f"{key}"
        if default is not None:
            prompt += f"[{default}]"
        prompt += ": "
        val = input(prompt)
    if val == "" and default is not None:
        val = default
    env[key] = val


################################################################


def s3_config(reset=False):
    get_param("BUCKET_NAME", reset=reset)

    write_env_to_file(env, env_file_path)
    return Namespace(
        bucket_name=env["BUCKET_NAME"],
    )


################################################################


def minio_config(reset=False):
    get_param("MINIO_USER", default="admin", reset=reset)
    get_param("MINIO_PASSWORD", is_password=True, reset=reset)
    get_param("MINIO_HOST", default="localhost", reset=reset)
    get_param("MINIO_PORT", default="9000", reset=reset)
    get_param("MINIO_ALIAS", default="dcsm", reset=reset)

    write_env_to_file(env, env_file_path)
    return Namespace(
        alias=env["MINIO_ALIAS"],
        url=env["MINIO_HOST"],
        port=env["MINIO_PORT"],
        admin_username=env["MINIO_USER"],
        admin_password=env["MINIO_PASSWORD"],
    )


################################################################


def psql_config(reset=False, **kwargs):
    print(env)
    get_param("POSTGRES_USER", default="admin", reset=reset)
    get_param("POSTGRES_PASSWORD", is_password=True, reset=reset)
    get_param("POSTGRES_HOST", default="localhost", reset=reset)
    get_param("POSTGRES_PORT", default=5432, reset=reset)
    get_param("DATABASE", default="dcsm", reset=reset)
    write_env_to_file(env, env_file_path)

    return Namespace(
        database=env["DATABASE"],
        host=env["POSTGRES_HOST"],
        port=env["POSTGRES_PORT"],
        username=env["POSTGRES_USER"],
        password=env["POSTGRES_PASSWORD"],
    )


################################################################
