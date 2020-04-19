import requests as req
from bs4 import BeautifulSoup

city = input("Podaj miasto\n")
url = 'https://www.pracuj.pl/praca/python;kw/'+city+';wp?rd=0'
page = req.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.title)
element = (soup.find('span',class_='results-header__offer-count-text-number'))

print(element.text)
