import os
from dotenv import load_dotenv
import requests

# .env 파일 로드
load_dotenv()

client_id = os.environ.get("KAKAO_CLIENT_ID")
authorize_code = os.environ.get("KAKAO_AUTHORIZE_CODE")
redirect_uri = "https://example.com/oauth"

token_url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "authorization_code",
    "client_id": client_id, 
    "redirect_uri": redirect_uri, 
    "code": authorize_code
}

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)

# 