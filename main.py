import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977#.X10KwmgzZPY')

soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_="tombstone-container")



#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp temp-high').get_text())

period_names = [ item.find(class_='period-name').get_text() for item in items ]
short_desc =  [ item.find(class_='short-desc').get_text() for item in items ]

temprature =  [ item.find(class_='temp temp-high') for item in items ]


weather_data = pd.DataFrame({

    'Week_days':period_names,
    'Report':short_desc,
    'tempratre':temprature,
})

print(weather_data)

weather_data.to_csv('weather.csv')

