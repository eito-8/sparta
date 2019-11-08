import requests
import pprint
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

tmusic = soup.select('td.info > a')

print(tmusic)

"""
rank = 1
for music in tmusic:
    a_tag = music.select_one('td.info > a')
    if not a_tag == None:
        title = a_tag.text
        artist = music.select_one('td.point').text
        print(rank, title, artist)
        rank += 1
"""