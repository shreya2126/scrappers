import requests
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import json

# britannica urls for cities and states
# https://www.britannica.com/topic/list-of-cities-and-towns-in-India-2033033
# https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-Kingdom-2034188
# https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068

def getCities():
    url = 'https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068'
    data = {}
    Cities={}
    cityData = {}
    array = []
    state = ''
    citiesArray = []
    CitiesFile=open('USA Cities and States.json','w+')
    CitiesFile.write('{"Data":[\n')
    sourceCode = requests.get(url)
    htmlInit = sourceCode.text
    soupInit = BeautifulSoup(htmlInit,"html.parser")
    for section in soupInit.find_all('section',{'data-level':'1'}):
        if section.find('h2') is not None:
            state = (section.find('h2').find('a')).string
            print (state, '  being parsed...')
            data['state']= state
            for cities in ((section.find('ul')).find_all('li')):
                if (cities.find('div')).find('a') is not None:
                    cityData['name'] = ((cities.find('div')).find('a')).string
                    cityData['lat-long'] = getLatLong(((cities.find('div')).find('a')).string, state)
                    cityData['zip'] = getZip(((cities.find('div')).find('a')).string, state)
                    citiesArray.append(cityData)
                    cityData = {}
            data['cities']=citiesArray
            json.dump(data,CitiesFile)
            CitiesFile.write(',\n')
            array = []
            citiesArray = []
    CitiesFile.write(']}')
    CitiesFile.close()
    print ('DONE. (^\._|_./^)')



def getLatLong(city, state):
    url = 'https://en.wikipedia.org/wiki/'+city.replace(" ",'_')+',_'+state
    sourceCode = requests.get(url)
    htmlInit = sourceCode.text
    soupInit = BeautifulSoup(htmlInit,"html.parser")
    span=soupInit.find('span',{'class':'geo-dec'})
    if span is not None:
        coords = (span.string).replace('\u00b0N ',', -')
        coords = coords.replace('\u00b0W','')
        coords = coords.replace('\u00b0E','')
        coords = '+'+coords
        return coords
    else:
        return ''       


def getZip(city, state):
    url = 'https://en.wikipedia.org/wiki/'+city.replace(" ",'_')+',_'+state
    sourceCode = requests.get(url)
    htmlInit = sourceCode.text
    soupInit = BeautifulSoup(htmlInit,"html.parser")
    span=soupInit.find('span',{'class':'postal-code'})
    if span is not None:
        if span.string is not None:
            zip = (span.string).replace('\u2013','-')
            return zip
    else:
        return ''



getCities()
print(url)