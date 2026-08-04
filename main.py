import os
import json
import requests

# 깃허브 Secrets에서 토큰 불러오기
ACCESS_TOKEN = os.environ.get("KAKAO_ACCESS_TOKEN")

def send_kakao_message(text):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # 카카오 규격에 맞는 안전한 JSON 템플릿 생성
    template_payload = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://naver.com",
            "mobile_web_url": "https://naver.com"
        }
    }
    
    data = {
        "template_object": json.dumps(template_payload)
    }
    
    res = requests.post(url, headers=headers, data=data)
    return res.json()

if __name__ == "__main__":
    msg = "☀️ 좋은 아침입니다!\n오늘도 멋진 하루 보내세요!"
    result = send_kakao_message(msg)
    print("발송 결과:", result)
