[](https://github.com/Procybit/Ky3M)

[![GitHub Repo stars](https://img.shields.io/github/stars/Procybit/Ky3M?style=social)](https://github.com/Procybit/Ky3M)

[![PyPI - Downloads](https://img.shields.io/pypi/dm/ky3m?style=for-the-badge)](https://pypi.org/project/ky3m/)

[![GitHub](https://img.shields.io/github/license/Procybit/Ky3M?style=for-the-badge)](https://github.com/Procybit/Ky3M/blob/master/LICENSE)

[![GitHub contributors](https://img.shields.io/github/contributors/Procybit/Ky3M?style=for-the-badge)](https://github.com/Procybit/Ky3M/blob/master/CONTRIBUTORS.md) [![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Procybit/Ky3M?style=for-the-badge)](https://github.com/Procybit/Ky3M/commits/) [![GitHub issues](https://img.shields.io/github/issues-raw/Procybit/Ky3M?style=for-the-badge)](https://github.com/Procybit/Ky3M/issues)

# Ky3M

Minecraft Mod Manager by Leon "Procybit" Shepelev

## Installing

Via pip:

```
pip install ky3m
```

You can also update to the latest version:

```
pip install ky3m --upgrade
```

**Make sure you have Python 3.10 or above installed!**

## Program launch

Via terminal:

```
python -m ky3m
```

## Using the CLI

If the program is run correctly, this should be in the terminal:
```
Ky3M :>
```
At the moment, the only thing that can be entered into the CLI is methods.

Methods are simple commands that work directly with Ky3M internals.

The name of the method is written in CAPITAL LETTERS, the specification fields of the method are written with spaces:

```
Ky3M :> METHOD Field_1 Field_2 ANoTheR--fiEld00;[-+^ 4thFIELD
Something happened...
```

If the method name starts with the "adv" prefix, then the associated log will be displayed:

```
Ky3M :> advMETHOD Field_1 Field_2 ANoTheR--fiEld00;[-+^ 4thFIELD
Something happened...

Log intercepted!
[ky3m.methods] METHOD started!
[ky3m.something] Something happened! (something: True)
[ky3m.methods] METHOD ended!
```

## Methods

### INSPECT

Outputs all .jar files names from Minecraft mods folder.

ASSIGNS A UNIQUE ID TO EACH NEWLY OUTPUT FILE.

### PEER `id`

Outputs information about certain .jar file in Minecraft mods folder.

Uses `id`  assigned by *INSPECT*.

### EXPEL `id`

Permanently deletes certain .jar file from Minecraft mods folder.

Uses `id` assigned by *INSPECT*.

### ADOPT `saved_id`

Copies certain .jar file from Minecraft mods folder to local library.

Uses `saved_id` assigned by *INSPECT*.

CAN INTERRUPT CLI AND REQUEST NAME OF SAVED FILE IF NEEDED.

DOESN'T DELETE CERTAIN FILE.

ASSIGNS A UNIQUE SAVED ID TO EACH SAVED FILE.

### ADOPTS

Outputs all saved .jar files names from local library.

### RELEASE `saved_id`

Copies certain .jar file from local library to Minecraft mods folder.

Uses `saved_id` assigned by *ADOPT*.

### PUNISH `saved_id`

Permanently deletes certain .jar file from local library.

Uses `saved_id` assigned by *ADOPT*.

### BUNDLE `name` | `bundle_id`

*Note that | separates an alternates.*

If `name` not found, creates new bundle (Ky3M modpack) and outputs created bundle's ID.

Uses `name` that is any string.

ASSIGNS A UNIQUE ID TO EACH CREATED BUNDLE.

**ALTERNATE**

If found bundle with specified `bundle_id`, outputs the bundle info.

Uses `bundle_id` that is valid UUID (in any form).

### BUNDLES

Outputs all created bundles' IDs and names.

### BURST `bundle_id`

Permanently deletes certain bundle.

Uses `bundle_id` assigned by *BUNDLE*.

### BIND `bundle_id` `saved_id`

Binds certain .jar to a certain bundle.

Uses `bundle_id` assigned by *BUNDLE*.

Uses `saved_id` assigned by *ADOPT*.

ASSIGNS A BIND ID (BUNDLE LOCAL) BASED ON SAVED ID.

### DETACH `bundle_id` `bind_id`

Detached certain .jar from a certain bundle.

Uses `bundle_id` assigned by *BUNDLE*.

Uses `bind_id` assigned by *BIND*.

### APPLY `bundle_id`

Releases all binded to certain bundle .jar files (see *RELEASE*).

Uses `bundle_id` assigned by *BUNDLE*.

DOESN'T DELETE ANY FILES.

## License
This project follows MIT license (see [LICENSE](LICENSE)).
