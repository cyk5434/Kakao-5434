import os
import requests

# 깃허브 Secrets에서 키값 불러오기
REST_API_KEY = os.environ.get("KAKAO_REST_API_KEY")
ACCESS_TOKEN = os.environ.get("KAKAO_ACCESS_TOKEN")

def send_kakao_message(text):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "template_object": f'{{"object_type": "text", "text": "{text}", "link": {{"web_url": "https://naver.com"}}}}'
    }
    res = requests.post(url, headers=headers, data=data)
    return res.json()

if __name__ == "__main__":
    msg = "☀️ 좋은 아침입니다!\n오늘도 멋진 하루 보내세요!"
    result = send_kakao_message(msg)
    print("발송 결과:", result)
