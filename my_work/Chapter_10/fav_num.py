# --- Ex 10.11 10.12

from pathlib import Path
import json


def guess_user_num():
    path = Path("my_work\Chapter_10/fav_num.json")
    user_num = get_stored_num(path)
    if user_num:
        print(f"Your fav num is: {user_num}")
    else:
        user_num = get_user_new_num(path)
        print(f"Your fav num has been saved as: {user_num}")


def get_user_new_num(path):
    user_num = input("Enter your favorite number: ")
    content = json.dumps(user_num)
    path.write_text(content)
    return user_num


def get_stored_num(path):
    if path.exists():
        content = path.read_text()
        fav_num = json.loads(content)
        return fav_num
    else:
        return None


guess_user_num()
