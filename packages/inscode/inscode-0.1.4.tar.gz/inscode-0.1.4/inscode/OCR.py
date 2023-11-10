import os
import requests
import base64
import sys

API_URL = "https://inscode-api.csdn.net/api/openapi/ocr"
INSCODE_API_KEY = os.getenv("INSCODE_API_KEY")
default_type = ["image", "url", "pdf_file", "ofd_file"]


def ocr(type, path):
    body = {
        "apikey": INSCODE_API_KEY,
    }

    if type not in default_type:
        raise ValueError("parameter 'type' is not supported")
    else:
        if type != 'url':
            if get_file_size(path) > 10:
                raise ValueError("parameter 'path' > 10MB", )
            body.update({type: file2base64(path)})
        else:
            body.update({type: path})

    response = requests.post(API_URL, json=body)
    if response.status_code == 200:
        resp = response.json()
        if resp["code"] == 200:
            full_response = ""
            if response.json():
                words_result = response.json()["data"]["words_result"]
                for word in words_result:
                    full_response = full_response + "\n" +word["words"]
                return full_response
            else:
                print("The API did not return any results.")
                return None
        print("Error:", resp["code"], resp["msg"])
        return None
    else:
        print("Error:", response.status_code, response.text)
        return None


def file2base64(file_path):
    if isinstance(file_path, bytes):
        data = file_path
    else:
        with open(file_path, "rb") as f:
            data = f.read()
    encoded_data = base64.b64encode(data).decode()
    return encoded_data


def get_file_size(file_path):
    if isinstance(file_path, bytes):
        size = sys.getsizeof(file_path)
    else:
        size = os.path.getsize(file_path)  # 获取文件大小，单位是字节
    size = size / (1024 * 1024)  # 将文件大小转换为兆字节(MB)
    return size
