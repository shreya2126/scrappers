from bs4 import BeautifulSoup
import requests
file_obj = open("quotes.json", "w", encoding="utf-8")
file_obj.write('[')
for index in range(1,100):
    url=requests.get("https://www.goodreads.com/quotes/tag/inspirational?page=" + str(index))
    print ('page = ' + str(index) +'parsing...')
    soup=BeautifulSoup(url.text,"html.parser")
    quote=soup.find_all("div", {"class": "quote mediumText"})
    for div in quote:
        saying=div.find("div",{"class":"quoteText"}).find(text = True)
        author=div.find("span",{"class":"authorOrTitle"}).text
        try:
            image = (div.find("a",{"class":"leftAlignedImage"})).find('img')['src']
        except Exception as e:
            image = 'Not Found'
        file_obj.write('{')
        file_obj.write('"image": "' + image.rstrip() + '",')
        file_obj.write('"say": "' + str(saying.rstrip().lstrip().replace('\n', ''))  + '",')
        file_obj.write('"author": "' + author.rstrip().lstrip() + '"')
        file_obj.write('},')
file_obj.write(']')
file_obj.close()