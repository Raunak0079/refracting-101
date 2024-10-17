from pathlib import Path
import json
def st_info_username(path):
    path = Path("username.json")
    if path.exists():
        contents=path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def greet_users():

    path=Path('username.json')
    username = st_info_username(path)
    if username:
        print(f"welcome back,{username}")
    else:

        username = input("what is your name: ")
        contents = json.dumps(username)
        path.write_text(contents)



        print(f"hey {username} man how are u? ")
greet_users()




