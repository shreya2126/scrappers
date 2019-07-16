import requests
from bs4 import BeautifulSoup
page=requests.get("https://en.wikipedia.org/wiki/List_of_Indian_playback_singers")
soup=BeautifulSoup(page.text,"html.parser")
file_obj = open("singeres.json", "w")
file_obj.write('[')
singerList=soup.find("table", {"class": "wikitable"})
singerListbest=singerList.find_all("tr")
for tr in singerListbest:
    td=tr.find_all("td")
    if td:
        file_obj.write('{')
        file_obj.write('"Year": "' + str((td[0].text)).rstrip() + '",')
        file_obj.write('"Name": "' + str((td[1].text)).rstrip() + '",')
        file_obj.write('"Language": "' + str((td[2].text).rstrip().encode("utf-8")) + '"')
        file_obj.write('},')
file_obj.write(']')

file_obj.close()