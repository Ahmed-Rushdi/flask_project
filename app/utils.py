import base64


def bytes_to_base64(blob: bytes) -> str:
    return base64.b64encode(blob).decode()
