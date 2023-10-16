# This module contains all the functions which not related to a specific procedure.
# Last update: 24.1.2023 by Rom Lior.

import os
import sys
import shutil

from constants import *

# Prints the current working directory, helpful for debugging.
def print_current_directory():
    print("\nCurrent working directory is:", os.getcwd())

# User can pass data types to check as a command line arguments.
# This function creates a list of all data types has to check.
# NOTICE: default option is all data types.
def get_data_types():
    data_types_to_check = []

    if len(sys.argv) == 2:                                  # check all data types
        for dt in DataTypes:
            data_types_to_check.append(dt.name)
    else:                                                   # check specific data types
        i = DATA_TYPE_INDEX
        while i < len(sys.argv):
            data_types_to_check.append(sys.argv[i])
            i += 1

    return data_types_to_check


# XXX - not sure necessary
# Before uploading data - moves an experiment from the experiments directory to the upload directory
def change_dir_before_upload(file_name, source_path):
    full_source_path =  source_path + r"/" + file_name
    full_destination_path = UPLOAD_PATH + r"/" + file_name

    shutil.move(full_source_path, full_destination_path)
    return full_destination_path     # we'll use it to return the file to its original directory


# After uploading data - moves back experiment from upload directory to the experiments directory
def change_dir_after_upload(file_name, source_path, destination_path):
    full_source_path =  source_path + r"/" + file_name
    full_destination_path = destination_path + r"/" + file_name

    shutil.move(full_source_path, full_destination_path)
