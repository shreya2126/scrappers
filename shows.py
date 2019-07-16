import requests
from bs4 import BeautifulSoup
url=requests.get("https://en.wikipedia.org/wiki/List_of_best-selling_books")
soup=BeautifulSoup(url.text,"html.parser")
file_obj = open("shows.json", "w")
file_obj.write('[')
showlists=soup.find_all("table",{"class":"wikitable sortable"})
for showlist in showlists:
        showlist1=showlist.find_all("tr")
        for tr in showlist1:
                td = tr.find_all('td')
                if len(td):
                        file_obj.write('{')
                        file_obj.write('"book": "' + str(((td[0].text)).rstrip().encode("utf-8")) + '",')
                        file_obj.write('"author": "' + str(((td[1].text)).rstrip().encode("utf-8")) + '",')
                        file_obj.write('"Language": "' + str((td[2].text).rstrip() + '"'))
                        file_obj.write('},')
file_obj.write(']')
file_obj.close()

        



