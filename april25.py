# import requests
# from bs4 import BeautifulSoup
# URL="https://www.cet.ac.in/head-of-departments"

# req=requests.get(URL)
# source_code=req.content

# Soup=BeautifulSoup(source_code,'lxml')

# table=Soup.find("table")
# rows=table.find_all('tr')
# rows=rows[1:]
# for row in rows:
#     columns=row.find_all('td')
#     hod_name=columns[0]
#     department=columns[1].text
#     phone=columns[2].text
#     print(hod_name,department,phone)


# second prgrm

import requests
from bs4 import BeautifulSoup
URL="https://books.toscrape.com/catalogue/page-2.html"

req=requests.get(URL)
source_code=req.content

Soup=BeautifulSoup(source_code,'lxml')

articles=Soup.find_all("article")
for i in articles:
    h3 = i.find('h3')
    a = h3.find('a')
    print(a.text)

for j in articles:
    div=j.find('div', class_="product_price")
    p = div.find('p')
    print(p.text)