from bs4 import BeautifulSoup
import urllib.request

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"


req = urllib.request.urlopen(url)


BeautiObject = BeautifulSoup(req,'html.parser')
parsing = BeautiObject.findAll('div',attrs={"class":"form_search"})

for par in parsing:
    print(par.text)