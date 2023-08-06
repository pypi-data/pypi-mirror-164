import os
import requests
from typing import List

def download_file(fileURL: str, api_root: str, api_token: str) -> bool:
    """
    Downloads file
    bool if true or file is allready present
    """

    if os.path.isfile(fileURL):             #is local to hard drive
        if os.path.isfile(file_name(fileURL)): #is allready moved to local position
            return True
        else:

    else:
        try:
            rv = requests.get(os.path.join(api_root, 'api/files', fileURL + "?filter=download"),
                              headers={'Authorization': 'Bearer ' + api_token})
            rv.raise_for_status()

            with open(file_name(fileURL), "wb") as outfile:
                outfile.write(rv.content)
        except:


def download_files(filesURL: List[str], api_root: str, api_token: str) -> bool:
    """

    """
    rvalue = True
    for file in filesURL:
        results = download_file(file, api_root, api_token)
        rvalue = rvalue and results

    return rvalue