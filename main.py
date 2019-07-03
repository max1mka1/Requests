import csv
import requests


def getOfficeFeed():
    apiKey = {'apiKey': Key, 'cmd': 'OFFICEFEED'}
    r = requests.get(url, params=apiKey)
    return r.text


def getOfficeFeed():
    apiKey = {'apiKey': Key, 'cmd': 'OFFICEFEED'}
    r = requests.get(url, params=apiKey)
    return r.text


# Функция запроса на получение списков всех сотрудников агентства
def getUsersFeed(cmd):
    apiKey = {'apiKey': Key, 'cmd': 'USERSFEED'}
    r = requests.get(url, params=apiKey)
    return r.text


url = 'http://api.lotinfo.ru'
Key = '61049ca-0382c4a-59b6389-58ec74e-7a8196e'
apiKey = {'apiKey': Key, 'cmd': 'OFFICEFEED'}
csvFile = 'catalog-2019-07-02.csv'
xmlFile = 'myData.xml'



r = requests.get(url, params=apiKey)
print('type of r is', type(r), r.__doc__)
print('URL of GET request = ', r.url)
#r = requests.post(url, '61049ca-0382c4a-59b6389-58ec74e-7a8196e')
print('Answer of POST request:', r.text)

#csvData = csv.reader(open(csvFile))
#xmlData = open(xmlFile, 'w')
#xmlData.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
# there must be only one top-level tag 
#xmlData.write('<OBJECTS>' + "\n")
#xmlData.write('</OBJECTS>' + "\n")
#xmlData.close()
