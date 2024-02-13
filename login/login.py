from telegram.client import Telegram
import json
import os

def create_tg_client(config_path :str):
    path = os.path.abspath(config_path)
    try:
        with open(os.path.abspath(config_path)) as file:
            kw_dict = json.loads(file.read().rstrip())
            print(kw_dict)
            tg = Telegram(**kw_dict)
            print(dir(tg))
            return tg
    except:
        print("Failure while trying to read file.")
        return None
