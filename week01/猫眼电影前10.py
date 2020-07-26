import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('movie10.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['电影名称','类型','上映时间'])

url = "https://maoyan.com/films?showType=3"
headers = {'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (Khtml, likeGecko) Chrome//77.0.3865.90 safari/537.36'}
res = requests.get(url,headers = headers)
print(res.status_code)
movielist = BeautifulSoup(res.text,'html.parser')

movies = movielist.find_all('div',class_='movie-hover-info')
#print(len(movies))
for movie in movies[:10]:
    movie_name = movie.find('span',class_="name").text
    movie_type = movie.find('span',class_="hover-tag").text
    movie_time = movie.find('div',class_="movie-hover-title movie-hover-brief").text
    writer.writerow([movie_name,movie_type,movie_time])

csv_file.close()