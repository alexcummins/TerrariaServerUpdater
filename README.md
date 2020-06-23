# TerrariaServerUpdater

Checks if your vanilla Terraria server needs updating and if so will download and copy over server config

## Requirements

* Python >= 3.7 (As code uses data classes)

Make sure to install the requirements in requirements.txt
```bash
pip install -r requirements.txt
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

This tool won't work for Terraria servers that are older than 1.3.5.3 as the directory naming convention is different.
## License
[MIT](https://choosealicense.com/licenses/mit/)