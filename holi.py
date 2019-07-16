import requests
from bs4 import BeautifulSoup
page=requests.get("https://www.calendarlabs.com/holidays/india/2019")
soup=BeautifulSoup(page.text,"html.parser")
file_obj = open("holiday.json", "w")
file_obj.write('[')
holiday=soup.find("table", {"class": "hlist_tab"})
holiday1=holiday.find_all("tr")
for tr in holiday1:
    td=tr.find_all("td")
    if td:
        file_obj.write('{')
        file_obj.write('"DAY": "' + str((td[0])).rstrip() + '",')
        file_obj.write('"DATE": "' + str((td[1].text)).rstrip() + '",')
        file_obj.write('"HOLIDAY": "' + str((td[2].text)).rstrip() +'"')
        file_obj.write('},')
file_obj.write(']')

file_obj.close()


