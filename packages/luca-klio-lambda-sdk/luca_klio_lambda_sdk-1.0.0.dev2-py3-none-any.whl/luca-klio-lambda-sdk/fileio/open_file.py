import ByteIO

def open_file(file_path: str) -> ByteIO:

    with open(filepath, 'rb') as fh:
        return BytesIO(fh.read())