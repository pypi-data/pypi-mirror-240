import os

base_path = 'logs'

def create_dir_if_not_exist(path:str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def write_log(filename:str, content:str, reset:bool) -> None:
    mode = 'w' if reset else 'a'

    create_dir_if_not_exist(base_path)

    with open(f"{base_path}/{filename}", mode) as f:
        f.write(content)

def read_logs(filename:str) -> list[str]:
    try:
        with open(f"{base_path}/{filename}") as f:
            return f.readlines()
    except FileNotFoundError:

        create_dir_if_not_exist(base_path)

        f = open(f"{base_path}/{filename}", 'w')
        f.close()
        return []
        

