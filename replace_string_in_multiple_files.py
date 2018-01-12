#!/usr/bin/python
"""
Script used to change GigabitEthernet1 to GigabitEthernet0/1 in INE configs
in order to work in EVE-NG environment
"""

import os

# Define path to config files
config_path = '/home/pl23017/Downloads/advanced.technology.labs/'

# Use os.walk method to go through all Directiories and SubDirectiories
for dirpath, dirname, filename in os.walk(config_path):

    print filename

    # Create full path to config files
    for fname in filename:
        path = os.path.join(dirpath, fname)
        # check if 'advanced.technology.labs' is in path
        if "advanced.technology.labs" in path:

            # Open each file in Read mode
            with open(path, "r") as strg_orig:

                # Create strg_new variable which holds corrected data: GigabitEthernet1 -> GigabitEthernet0/1
                strg_new = strg_orig.read().replace("GigabitEthernet1", "GigabitEthernet0/1")

            # Open each file in Write mode
            with open(path, "w") as strg_orig:

                # write content of strg_new to original files
                strg_orig.write(strg_new)
