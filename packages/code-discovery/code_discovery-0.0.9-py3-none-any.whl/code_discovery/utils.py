import platform


def print_user_versions():
    print(
        f"--- System Info: {platform.platform()}, Python Version: {platform.python_version()} --- \n")
