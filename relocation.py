import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs/companies"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

cities = set()
for location_element in soup.find_all("div", class_=["fc-black-500", "fs-body1"]):
    city = location_element.text.strip()
    if city:
        cities.add(city)

sorted_cities = sorted(cities)
for city in sorted_cities:
    print(city)