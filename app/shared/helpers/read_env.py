"""
This file implements the logics to get the environment variables.
"""
from os import (
    environ,
    getcwd,
    path,
)

from dotenv import load_dotenv
from decouple import config


# load the environment variables
env_path = path.join(getcwd(), r"app/.env")
load_dotenv(dotenv_path=env_path)


def get_db_creds() -> dict[str, str]:
    """
    This function will read the environment variables
    and return the database credentials.
    input: None
    return: dict contains the database credentials as follows:
    {
        'host': str,
        'user': str,
        'password': str,
        'database': str
    }
    """
    db_creds: dict = {
        'host': config('DB_HOST'),
        'user': config('DB_USER'),
        'password': config('DB_PASSWORD'),
        'database': config('DB')
    }
    return db_creds
