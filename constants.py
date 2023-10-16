# This module contains all the constants the automation should have.
# Last update: 24.1.2023 by Rom Lior.

PATH_INDEX = 1
DATA_TYPE_INDEX = 2
UPLOAD_PATH = r"C:\Users\RomLior\PycharmProjects\pythonProject\CytoPro_Automation\uploader\cytopro-apps-uploader-2.0.2"

# NOTICE: the name of a data type in DataTypes class MUST be the same as in the local data folder
from enum import Enum
class DataTypes(Enum):
    raw = 0
    cpm = 1
    tpm = 2





