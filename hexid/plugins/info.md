# Plugins

Plugins are an easy way to extend the file matching system by providing new definitions and methods to detect more files.

## How does it work?

Plugins are placed in the `plugins` folders. For this example, let's assume we're making a plugin for `7zip` files. The folder would be the name of the extension, in this case `7z`, and all files inside are also named this.

> [!TIP]
> This is also what users will use for the `--extension` flag, so make sure it's close enough to what a user would expect it to be.

The `7z.json` file would likely contain something like the following:

```json
{
    "id": "7z-matcher-plugin",
    "name": "7z Matcher Plugin",
    "description": "7-Zip archive file",
    "author": "AuthorsName",
    "file_types": ["7z"],
    "hex": [
        "HexStringHere"
    ],
    "website": "https://www.github.com/JamsterJava",
    "dependencies": [
        "some-dependency"
    ]
}
```

The `id` is for easy, non-changing recognision of the plugin.

The ``name``, ``description`` and ``author`` are listed if the user uses the `--show-plugins` flag. 

The ``file_types`` are used by the file type validator. 

The ``hex`` list is a list of hex values to match against. This list is optional, as a plugin file may be used for matching instead.

The ``website`` is a link to the authors website, social media, GitHub etc.

The ``dependencies`` are other plugins which this plugin relies on to operate, e.g. the ZIP plugin relies on the Office plugin so that it can check that any ZIP files aren't actually ZIP files.

> [!WARNING]
> When using Hex, make sure it's lowercase. Uppercase hex doesn't work currently. This may be fixed later.

As mentioned above, there may also be a plugin file (`7z.py` in this case). This file offers the ability to match by more than a hex value. Theoretically, anything available within python can be used to match the file.

The `7z.json` file would likely contain something like the following:

```python
from pathlib import Path

def check_file(file_path: Path) -> str:
    """
    Optional plugin check for 7-Zip files.
    """
    
    try:
        with open(file_path, "rb") as f:
            header = f.read(6)
        if header == bytes.fromhex("377abcaf271c"):
            return 1
        else:
            return 0
    except Exception:
        return 0
```

Here we can see hex matching being done. This is redundant due to the JSON files hex field, but it's an example to showcase how it works.

The function should only return the following:

- ``1``, for a positive match.
- ``2``, for a possible match.
- ``0``, for no match.
- ``-1``, if an error occurs.
