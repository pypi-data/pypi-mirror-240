import os
from typing import Optional, List, Generator


def create_dir(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except FileNotFoundError as e:
        raise ValueError(f"Invalid path '{path}': {e}")


def remove_dir(path: str) -> None:
    try:
        os.rmdir(path)
    except FileNotFoundError:
        pass  # Directory doesn't exist, nothing to remove
    except OSError as e:
        raise ValueError(f"Invalid path '{path}': {e}")


def create_file(path: str) -> None:
    try:
        with open(path, "x"):
            pass
    except FileExistsError:
        pass  # File already exists, nothing to create
    except FileNotFoundError as e:
        raise ValueError(f"Invalid path '{path}': {e}")


def remove_file(path: str) -> None:
    try:
        os.remove(path)
    except FileNotFoundError:
        pass  # File doesn't exist, nothing to remove
    except OSError as e:
        raise ValueError(f"Invalid path '{path}': {e}")


def file_exist(path: str) -> bool:
    if os.path.exists(path):
        return os.path.isfile(path)
    return False


def dir_exist(path: str) -> bool:
    if os.path.exists(path):
        return os.path.isdir(path)
    return False


def write(path: str, data: str, mode: Optional[str] = "a") -> None:
    if mode not in ["w", "a"]:
        raise ValueError(f"Invalid mode '{mode}'. it should be 'w' or 'a'.")
    with open(path, mode) as f:
        f.write(data)


def writeline(path: str, data: str, mode: Optional[str] = "a") -> None:
    if mode not in ["w", "a"]:
        raise ValueError(f"Invalid mode '{mode}'. it should be 'w' or 'a'.")
    with open(path, mode) as f:
        f.write(data + "\n")


def writelines(path: str, data_list: List[str],
               mode: Optional[str] = "a") -> None:
    if mode not in ["w", "a"]:
        raise ValueError(f"Invalid mode '{mode}'. it should be 'w' or 'a'.")
    with open(path, mode) as f:
        for item in data_list:
            f.write(item + "\n")


def read(path: str) -> str:
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except OSError as e:
        raise ValueError(f"Error reading from '{path}': {e}")


def readline(path: str, lineno: int) -> str:
    try:
        with open(path, "r") as f:
            lines = [line.rstrip("\n") for line in f.readlines()]
            return lines[lineno]
    except FileNotFoundError:
        return ""
    except OSError as e:
        raise ValueError(f"Error reading from '{path}': {e}")


def readlines(path: str) -> List[str]:
    try:
        with open(path, "r") as f:
            return [line.rstrip("\n") for line in f.readlines()]
    except FileNotFoundError:
        return []
    except OSError as e:
        raise ValueError(f"Error reading from '{path}': {e}")


def get_reader(path: str) -> Generator[str, None, None]:
    try:
        with open(path, "r") as f:
            for line in f:
                yield line.rstrip("\n")
    except FileNotFoundError:
        return
    except OSError as e:
        raise ValueError(f"Error reading from '{path}': {e}")
