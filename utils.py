from base64 import b64decode, b64encode


def byte_to_string(bytes):
    return b64encode(bytes).decode("utf-8")


def string_to_bytes(string):
    return b64decode(string)
