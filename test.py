import  requests
import json

url= "http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=058472d2f4b90357247484b19919d8b7"

headers = {
    "user-Agent":.0.3325."zilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65181 Safari/537.36"Mo,
    "Referer":"http://music.163.com/song?id=551816010",
    "Origin":"http://music.163.com",
    "Host":"music.163.com"
}

# 加密数据
user_data ={
    "params":"8pZF%2B6kirAjyWq2JRBd6uiNIvtouSzX8CJpkO4tkUVwhkOvKpWXiiYIJJk72CKkvbR9PKajKmXX3GOSjvvP6pEVkyOqgeFy5H82TF%2Bel5afxQ8vGfMb0aRBEOLoPy4eNXOAlM4f9tv0O6C3lfxN01yLLPBSkFFIVnA9QHCiJaxopyfrEDTcIQAHF199fGkHriQqvs2uROmoei9arZTw7adT11rgmCAi9n02dksNSusI%3D",
    "encSecKey":"22324155b1cf03c50516f39f950b80aa8a898d6cb1cafd6ab6ad9853c33ad1988baa55c3eb40bfc38ea71b9d26748ddf7315e9a22be638572ec6d0acb56cefe64bed2f87c1e0350e3fcef1c34d2e35bbc96a8ffc9e4fdd43b376f1d22e2e0874fc3f32c6e3a4c0459b27243cafa4473464a9e779cda790f986413c887e504270"
}

response = requests.post(url,headers=headers,data=user_data)

data = json.loads(response.text)
hotcomments =[]
for hotcomment in data["hotComments"]:
    item ={
        "nickname":hotcomment["user"]["nickname"],
        "content":hotcomment["content"],
        "likedCount":hotcomment["likedCount"]
    }
    hotcomments.append(item)

#获取评论用户名，内容，获赞数
content_list =[content["content"]for content in hotcomments]
nickname =[content["nickname"]for content in hotcomments]
likedCount =[content["likedCount"]for content in hotcomments]