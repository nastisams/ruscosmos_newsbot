
from vedis import Vedis
import config


def get_current_state(user_id):
    with Vedis(config.file_bot) as fb:
        try:
            return fb[user_id].decode()
        except:
            return config.States.S_START.value


def del_state(field):
    with Vedis(config.file_bot) as fb:
        try:
            del(fb[field])
            return True
        except:
            return False


def set_state(user_id, value):
    with Vedis(config.file_bot) as fb:
        try:
            fb[user_id] = value
            return True
        except:
            return False


def set_property(id, value):
    with Vedis(config.file_bot) as fb:
        try:
            fb[id] = value
            return True
        except:
            return False
