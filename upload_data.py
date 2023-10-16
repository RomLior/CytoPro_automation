# This module contains all the data upload related functions.
# Last update: 24.1.2023 by Rom Lior.

from support_functions import *
from constants import *

# This function makes all the preparations for data upload: it gets the data general path, and makes sure
# that the data types the user passed are supported by the automation.
# If everything is fine - calls the upload all data types function.
def upload_data_manager():
    # get the path which contains all the data
    all_data_path = sys.argv[PATH_INDEX]

    # get all supported data types
    supported_data_types = []
    for dt in DataTypes:
        supported_data_types.append(dt.name)

    # get the data types the user want to check
    required_data_types = get_data_types()

    # check that all given data types are supported
    for dt in required_data_types:
        if not dt in supported_data_types:
            assert print("One (or more) of the required data types isn't supported by CytoPro.")

    # all good, let's continue
    upload_all_data_types(all_data_path, required_data_types)


# Gets the data general path and finds the specific path for each data type required.
# Then checks if there are experiments to upload, and if there are - calls the upload specific data function.
# all_data_path & data_types are given by the user.
def upload_all_data_types(all_data_path, required_data_types):

    for dt in DataTypes:
        # check if this data type is required
        if dt.name in required_data_types:
            data_type_path = get_path_by_type(all_data_path, dt.name)
            data_type_experiments_names = os.listdir(data_type_path)

            # upload experiments
            if len(data_type_experiments_names) > 0:
                upload_specific_data_type(data_type_experiments_names, data_type_path, dt.name)
                # print("upload: " + str(data_type_experiments_names))               # XXX - for debugging


# Uploads the data of a specific data type to CytoPro.
# Data type can be raw, cpm or tpm.
def upload_specific_data_type(one_type_experiments_list, one_type_experiments_path, data_type):

    for experiment_name in one_type_experiments_list:
        experiment_path = one_type_experiments_path + "/" + experiment_name
        os.chdir(UPLOAD_PATH)

        # set the right upload command
        if data_type == DataTypes.raw.name:
            cmd = "node crupload -d " + experiment_path + " -i " + experiment_name                        # default command
        else:
            cmd = "node crupload -d " + experiment_path + " -i " + experiment_name + " " + data_type      # specific command

        # upload!
        os.system(cmd)


# Gets an input data type and returns the path contains experiments with this type of data
def get_path_by_type(all_data_path, data_type):
    return all_data_path + r"/" + data_type


