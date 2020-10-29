import time
import requests
from fake_useragent import UserAgent

# ua = UserAgent(verify_ssl=False)



headers = {
    'referer': 'https://shimo.im/login?from=home',
  #  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.38 (KHTML, like Gecko) Chrome/83.0.4103.30 Safari/537.46',
    'authority': 'shimo.im',
    'scheme': 'https',
    'origin': 'https://shimo.im',
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
    }

formdata = {
    "mobile": '+8615688888888', 
    'password': 'yourpasswd'
    }

s = requests.Session()

r = s.post('https://shimo.im/lizard-api/auth/password/login', data = formdata, headers = headers)

url2 = 'https://shimo.im/profile#setting-email'

r2 = s.get(url2,headers = headers,cookies=s.cookies)

print(r2.text)

