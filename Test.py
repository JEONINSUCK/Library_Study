import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

tag = soup.findAll('div', attrs={'class': 'form_search'})

print('-' * 30)
print(tag)

print("|n 영화 제목만 뽑아내기")
print('-' * 30)

for tags in tag:
    print(tags.text)

print("\n 앵커의 href 속성")
url_header = 'https://movie.naver.com'