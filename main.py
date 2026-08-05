import os
import json
import requests

REST_API_KEY = os.environ.get("KAKAO_REST_API_KEY")
REFRESH_TOKEN = os.environ.get("KAKAO_REFRESH_TOKEN")
ACCESS_TOKEN = os.environ.get("KAKAO_ACCESS_TOKEN")

def get_new_access_token():
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": REST_API_KEY,
        "refresh_token": REFRESH_TOKEN
    }
    response = requests.post(url, data=data).json()
    return response.get("access_token")

def send_kakao_message(text, token):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    template_payload = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://naver.com",
            "mobile_web_url": "https://naver.com"
        }
    }
    data = {"template_object": json.dumps(template_payload)}
    res = requests.post(url, headers=headers, data=data)
    return res.json()

if __name__ == "__main__":
    token_to_use = ACCESS_TOKEN
    if REFRESH_TOKEN and REST_API_KEY:
        new_token = get_new_access_token()
        if new_token:
            token_to_use = new_token
            print("새 액세스 토큰 자동 발급 완료!")

    msg = "☀️ 좋은 아침입니다!\n오늘도 멋진 하루 보내세요!"
    result = send_kakao_message(msg, token_to_use)
    print("발송 결과:", result)
