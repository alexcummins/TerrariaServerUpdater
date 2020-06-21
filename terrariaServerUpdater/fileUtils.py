import os
import re
from dataclasses import dataclass


@dataclass
class Folder:
    name: str
    version_num: int


def get_current_version_number() -> Folder:
    file_names: [str] = os.listdir("../../")
    latest_folder: str = None

    for file_name in file_names:
        # Matches a file whose name is 4 numbers only

        file_group = re.search(r"^\d\d\d\d$", file_name)
        latest_folder = __check_versions(file_group, latest_folder)

    if not latest_folder:
        raise FileNotFoundError("No terraria server folder found. \n"
                                "Ensure old server's folder still have default name, for example '1335'")
    return Folder(name=latest_folder, version_num=int(latest_folder))


def __check_versions(file_group, latest_folder):
    if file_group:
        if latest_folder is None:
            return file_group.group()
        else:
            if int(latest_folder) < int(file_group.group()):
                return file_group.group()
    return latest_folder

