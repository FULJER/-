import requests
from bs4 import BeautifulSoup

url = "https://py4e-data.dr-chuck.net/comments_42.html"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

comments = soup.find_all('span', class_='comments')

total_comments = sum(int(comment.text) for comment in comments)

print(f"Общее количество комментариев: {total_comments}")
