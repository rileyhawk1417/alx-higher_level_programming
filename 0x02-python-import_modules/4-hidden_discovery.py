#!/usr/bin/python3


if __name__ == "__main__":
    import importlib

    importedModule = importlib.import_module("hidden_4")
    names = dir(importedModule)
    name_list = [name for name in names if not name.startswith("__")]
    sorted_list = sorted(name_list)
    for name in sorted_list:
        print(name)
