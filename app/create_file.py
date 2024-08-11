from datetime import datetime
import os
import sys


def create_directory(path: list) -> None:
    os.makedirs(os.path.join(*path), exist_ok=True)


def create_file(file_path: str, content: list) -> None:
    with open(file_path, "a") as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def get_file_content() -> list:
    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)
    return content


def main() -> None:
    args = sys.argv[1:]
    print(args)
    if "-d" in args:
        dir_index = args.index("-d") + 1
        directory_path = args[dir_index:]
        if "-f" in directory_path:
            file_index = directory_path.index("-f")
            file_name = directory_path[file_index + 1]
            directory_path = directory_path[:file_index]
            create_directory(directory_path)
            file_path = os.path.join(*directory_path, file_name)
            content = get_file_content()
            create_file(file_path, content)
        else:
            create_directory(directory_path)
    elif "-f" in args:
        file_name = args[args.index("-f") + 1]
        content = get_file_content()
        create_file(file_name, content)


if __name__ == "__main__":
    main()
