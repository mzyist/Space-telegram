import os
from urllib.parse import urlparse


def get_file_extension(file_path):
    parsed = urlparse(file_path)
    path = os.path.splitext(parsed[2])
    return path[1]
