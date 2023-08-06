# root_directory

Tired of the Python ["Importing files from different folder"](https://stackoverflow.com/q/4383571/6865804) mess?

This is a no-nonsense utility for importing relative to root. So for a directory structure like that:

```
* your_lib
  * lib.py
* your_main
  * main.py
* .root_directory
```

You can now import `lib.py` from `main.py` with the following:

```
import root_directory # This must be before imports relative to root
from your_lib import lib
```

This works as long as the root directory is a git repository or contains `.root_directory` in the root.

As a bonus, you can find out your root path with `root_directory.get_root()` (this returns a pathlib.Path object).

## Why another library?

There are several libraries that do something similar, however as far as I know, they either 1) only find the path, but don't help with importing, or 2) add many unnecessary and heavyweight dependencies.

This project has no dependencies.

## Installation

Run `pip install root_directory`, python 3.4+ is supported.
