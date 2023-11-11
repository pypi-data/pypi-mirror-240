import random
import string
import subprocess


def generate_password(length=32):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def check_process_return(process, fail_message):
    try:
        process.check_returncode()

    except subprocess.CalledProcessError as e:
        if e.stderr:
            raise RuntimeError(f"{fail_message}: {e.stderr.decode()}")
        else:
            raise RuntimeError(fail_message)
