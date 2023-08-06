import requests


def upload_to_URL(URL, data):
    rv = requests.put(URL, data=data)
    rv.raise_for_status()
    return URL
