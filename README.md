# TerrariaServerUpdater

This Python program will check if your vanilla Terraria server needs updating, and if so, will automatically download the new Terraria server version and copy over any config files to the new one.

#TODO
* Copy over config files for windows and mac too, and test it works on windows
* include config.json and any others
* Change file permissions of server files once they are downloaded so they don't have to be changed manually.

## Requirements

* Python >= 3.7 (As code uses data classes)

Make sure to install the requirements in requirements.txt
```bash
pip3 install -r requirements.txt
```

## Installation

Clone this repository into your folder which also contains the Terraria server folder.


```
.
├── 1403
│   ├── Linux
│   ├── Mac
│   └── Windows
└── TerrariaServerUpdater
    ├── __pycache__
    ├── terrariaServerUpdater
    └── venv

```

## Usage

Run from inside the TerrariaServerUpdater directory.
Make sure the parent directory of TerrariaServerUpdater contains the server folder.

```
cd TerrariaServerUpdater
python3 -m terrariaServerUpdater
```

* Currently only copies over exact file named 'serverconfig.txt' to new download
* This tool won't work for Terraria servers that are older than 1.3.5.3 as the directory naming convention is different.
## License
[MIT](https://choosealicense.com/licenses/mit/)
