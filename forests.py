from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.theearthsafari.com/forests-of-india.php")
soup=BeautifulSoup(url.text,"html.parser")
info=soup.find_all("p", {"class": "text_yellow"})
file_obj=file_obj = open("forests.json", "w")
file_obj.write('[')
for para in info():
        file_obj.write('{')
        file_obj.write('"information": "' + str(para.rstrip())  + '",'))
        file_obj.write('},')
file_obj.write(']')
file_obj.close()