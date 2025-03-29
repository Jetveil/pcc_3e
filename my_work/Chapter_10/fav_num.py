from pathlib import Path
import json


def get_user_num(path):
    path = Path("my_work\Chapter_10/fav_num.json")
    user_num = input("Enter your favorite number: ")
    content = json.dumps(user_num)
    path.write_text(content)

# def get_user_new_num(path):
#     path = Path("my_work\Chapter_10/fav_num.json")


def guess_user_num():
    path = Path("my_work\Chapter_10/fav_num.json")
    if path.exists():
        fav_num = path.read_text()
        print(f"I know your fav number! It is {fav_num}")
    else:
        get_user_num(path)


guess_user_num()
