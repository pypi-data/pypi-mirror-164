import os


def file_name(fileURL: str) -> str:
    """
    returns file name if url or local

    """
    if os.path.isfile(fileURL):             #is local to hard drive
        return os.path.basename(fileURL)
    else:
        if fileURL.find('/'):
            return fileURL.rsplit('/', 1)[1] # gives the last element of url
        else:
            return ""