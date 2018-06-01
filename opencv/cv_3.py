import cv2
import json
import requests

# ######获取面孔face_token
url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
files = {"image_file":open("face1.jpg","rb")}
payload = {
    "api_key": "ERB7wTkKTDx8mEvQgcAiJA3zjAjEpK7Q",
    "api_secret": "oUI3uI77OK0oaVmz5VO3zUWxC9LIsD75",
    "return_landmark": 0,
    "return_attributes": "gender,age,beauty"
}
r = requests.post(url,files=files,data=payload)     #请求ul
data = json.loads(r.text)       #返回json
print(data)
print(data["faces"][0]["face_token"])

# #####创建人脸集合，并加入face_token
# url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"
# payload = {
#     "api_key": "ERB7wTkKTDx8mEvQgcAiJA3zjAjEpK7Q",
#     "api_secret": "oUI3uI77OK0oaVmz5VO3zUWxC9LIsD75",
#     "display_name": "photoes",
#     "outer_id": "photo",
#     "force_merge": 1,
#     "face_tokens": "e1030db3c9777f422bf1c4f34ad5f6f7"
# }
# r = requests.post(url,data=payload)
# data = json.loads(r.text)
# print(data["faceset_token"])
