import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
topMusic = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')

rank = 1
for music in topMusic:
        title = music.select_one('td.info > a.title.ellipsis').text.strip()
        artist = music.select_one('td.info> a.artist.ellipsis').text.strip()
        topMusicData = {'rank' : rank,'title' : title,'artist' : artist}
        db.topMusic.insert_one(topMusicData)
        rank += 1
