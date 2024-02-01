# date : 20240201
# file : test25_web.py
# desc : urllib 모듈 사용법

#  from urllib.request import *   # request 모듈안의 모든 내용 다 사용할때
from urllib.request import Request, urlopen # request 클래스와 urlopen만 쓰겠다

req = Request('https://www.naver.com/') # 네이버 웹주소(url)
res = urlopen(req) # url주소로 웹사이트를 열어달라고 요청

print(f'응답코드는{ res.status}') # url로 요청된 웹사이트 응답 확인

print(res.read())


# urllib.request보다 성능이 조금 더 나은 모듈, pip install requests 명령프롬프트 가서 깔아야 되긴해
import requests
res2 = requests.get('https://www.naver.com/')

print(res2.status_code)
print(res2.text)