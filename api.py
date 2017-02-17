#coding=utf-8

import requests
import json
import time
HistoryList = []

def welcome():
    print('''
    Hello!Here are the Local Weather Forecast.
    Enter the city you want to search in Chinese or English.
    Enter "help" to get more help.
    Enter "history" to get the search history records.
    Enter "quit" to quit the program.
    ''')
welcome()

def fetchAPI(city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    payload = {'APPID':'90cb9d98ac5f5c13cc6c2ab80ab5a024','q':city, 'lang':'zh_cn'}
    r = requests.get(url, params=payload)
    data = json.loads(r.text)

    if r.status_code != requests.codes.ok:
        return 'sorry,please try again.'
    else:
        weather = data['weather'][0]['description'] # to fetch the 'weather' data from a dict in a list,sounds terrible.
        temp = str(data['main']['temp'])+'℉'
        wind = str(data['wind']['speed']) + 'miles/hour'
        onlinetime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        result = onlinetime, city, weather, temp, wind
        HistoryList.append(result)
        print(result)# here
    return onlinetime, city, weather, temp, wind


def main():


    while True:
        cityname = input('You can enter city name in Chinese or English:')
        if cityname == 'help':
            print('''
            Enter city name to get the weather conditions,
            Enter help,to get more help,
            Enter history,to get the Historical search data,
            Enter quit or exit to quit.
            ''')
        elif cityname == "history":
            if len(HistoryList) == 0:
                print("No history records.")
            else:
                for i in HistoryList:
                    print(i, HistoryList[0])
                print

        elif cityname == "quit":
            print('Goodbye!')
            quit()

        else:
            fetchAPI(cityname)



if __name__ == '__main__':
    main()
