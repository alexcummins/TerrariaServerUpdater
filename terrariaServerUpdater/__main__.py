#!/usr/bin/env python3

from .webUtils import *
from .fileUtils import *

URL = 'https://terraria.org/'


def main():
    (server_download_href, version_num) = check_for_update(URL)

    current_version_folder = get_current_version_number()

    if version_num > current_version_folder.version_num:
        print("New server version available online.")
        update = input("Would you like to update your version? (y/n)\n").lower().startswith("y")
        if update:
            print("Downloading new server zip...")
            download_url(server_download_href, save_path="../NewTerrariaServer.zip")
            print("Unzipping file...")
            print("Moving over server config file")

    elif version_num == current_version_folder:
        print("Current server up to date.")
        return


if __name__ == '__main__':
    main()
