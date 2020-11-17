import requests # pip install requests
import panda as pd # pip install Pandas
from bs4 import BeautifulSoup # pip install beatifulSoup4

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09969000000007&lon=-118.33512999999999#.X4bgfNAzaM8')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

time_of_day = [items.find(class_='period-name').get_text() for item in items]
short_description = [items.find(class_='short-desc').get_text() for item in items]
temperature = [items.find(class_='temp').get_text() for item in items]

print(time_of_day)
print(short_description)
print(temperature)

weather = pd.DataFrame({
    'Time of Day': time_of_day,
    'Description': short_description,
    'Temperature': temperature,

})

print(weather)

