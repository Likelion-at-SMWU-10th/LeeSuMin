'''
from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('a','link_favorsch')

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1
    '''

from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "http://www.naver.com/"
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

file = open("naver.html","w", encoding="UTF-8")
file.write(response.text)
file.close()

# print(soup.title)
# print(soup.title.string)
# print(soup.span)
# print(soup.findAll('span'))

# html 문서에서 모든 a태그를 가져오는 코드
#results = soup.findAll("a","link_favorsch")
#search_rank_file = open("rankresult.txt","w")

#print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

#for result in results:
#    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
#    print(rank,"위 : ",result.get_text(),"\n")
#    rank += 1