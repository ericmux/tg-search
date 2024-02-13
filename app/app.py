import os

from login import login


def run():
    login.create_tg_client(os.getenv("CREDENTIALS"))