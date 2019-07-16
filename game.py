from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.gamesradar.com/gta-5-cheats/")
soup=BeautifulSoup(url.text,"html.parser")
new=open("game.json","w") 
new.write("[")
for para in soup.find_all("p"):
        print(para.text)
        new.write("{")
        new.write("paragraph":"")
        new.write("}")
new.write("]")
new.close()                       
                        
