from bs4 import BeautifulSoup
import requests
for index in range(1,3):
    url=requests.get("https://www.listchallenges.com/complete-list-of-marvel-movies/list/" + str(index))
    soup=BeautifulSoup(url.text,"html.parser")
    file_obj = open("movies.json", "w")
    file_obj.write('[')
    movie=soup.find("div", {"class": "checklist-itemsSection"})
    marvel=movie.find_all("div",{"class":"item-click-area"})
    # marvel1=movie.find_all("div",{"class":"item-image-wrapper"})
    # marvel2=movie.find_all("div",{"class":"item-rank"})
    for div in marvel:
        image = (div.find("div",{"class":"item-image-wrapper"})).find('img')['src']
        rank = div.find("div",{"class":"item-rank"}).text
        name = div.find("div",{"class":"item-name"}).text
        file_obj.write('{')
        file_obj.write('"image": "' + image + '",')
        file_obj.write('"rank": "' + rank + '",')
        file_obj.write('"name": "' + name + '"')
        file_obj.write('},')
        print ("image => ", image, " rank => ", rank, " name => ",name)
file_obj.write(']')
file_obj.close()