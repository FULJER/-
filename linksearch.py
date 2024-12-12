import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = "https://www.py4e.com/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all('a', href=True)

unique_links = set()
for link in links:
    href = link['href']
    if href.startswith("https"):
        domain = urlparse(href).netloc
        if domain != urlparse(url).netloc:  # Проверяем, что это внешние сайты
            unique_links.add(href)

print(f"Уникальных внешних ссылок: {len(unique_links)}")

