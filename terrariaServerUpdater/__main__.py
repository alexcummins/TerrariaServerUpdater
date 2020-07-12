#!/usr/bin/env python3

from .webUtils import *
from .fileUtils import *

URL = 'https://terraria.org/'
ZIPNAME = 'NewTerrariaServer.zip'
CONFIG_FILE = 'serverconfig.txt'


def main():
    (server_download_href, new_version_num) = check_for_update(URL)

    current_version_folder = get_current_version_number()

    if current_version_folder is None:
        update: bool = input(
            "No current server detected, would you like to download the latest Terraria server?"
            " (y/n)\n").lower().startswith("y")
        if update:
            download_unzip_server(server_download_href)
            print("Successfully downloaded Terraria Server")
            return

    if new_version_num > current_version_folder.version_num:

        print("New server version available online.")
        update: bool = input(f"Would you like to update your server version from {current_version_folder.name} to"
                             f" {str(new_version_num)}? (y/n)\n").lower().startswith("y")

        if update:
            download_unzip_server(server_download_href)

            print("Attempting to copy over server config file...")
            was_copied = copy_config(f"{current_version_folder.name}/Linux/{CONFIG_FILE}",
                                     f"{str(new_version_num)}/Linux/{CONFIG_FILE}")

            if was_copied:
                print("Server config file copied over.")
            else:
                print(f"No server config file to copy over (looking for '{CONFIG_FILE}').")

            print("Successfully updated Terraria server.")

    elif new_version_num == current_version_folder.version_num:
        print("Current server version up to date.")
        return


def download_unzip_server(server_download_href):
    print("Downloading new server zip...")
    download_url(server_download_href, save_path=f'../{ZIPNAME}')
    print("Unzipping file...")
    unzip_server(f"../{ZIPNAME}")


if __name__ == '__main__':
    main()
