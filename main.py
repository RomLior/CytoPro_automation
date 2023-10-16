# Last update: 24.1.2023 by Rom Lior.

# Instructions:
# 1. Run command line "python main.py ***data path*** ***data types to check***".
# 2. NOTICE: When no "data types to check" argument is passed, the default is checking all the data types supported
#    by CytoPro.
# 3. Path argument MUST be correct.

# Requirements:
# 1. All data types that CytoPro supports MUST be in DataTypes class (in constants.py).
# 2. Inside the local general data directory, there MUST be a folder to each data type given as "data type to check" argument.
# 3. Each experiment MUST be in a subdirectory of itself (e.g. folders are: all_data -> raw -> GSE1234, GSE5678).

from upload_data import *

upload_data_manager()



# python main.py C:\Users\RomLior\PycharmProjects\pythonProject\CytoPro_Automation\uploader\data raw




