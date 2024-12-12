import requests
from bs4 import BeautifulSoup

# Функция для поиска вопросов по ключевому слову
def search_questions(keyword, pages=5):
    base_url = "https://stackoverflow.com/questions"
    questions = []

    # Перебираем страницы
    for page in range(1, pages + 1):
        print(f"Обработка страницы {page}...")
        url = f"{base_url}?page={page}&sort=newest&pagesize=15"
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Находим все вопросы на странице
        question_elements = soup.find_all("div", class_="s-post-summary")

        for question in question_elements:
            # Извлекаем заголовок вопроса
            title_element = question.find("a", class_="s-link")
            if title_element:
                title = title_element.text.strip()
                link = f"https://stackoverflow.com{title_element['href']}"

                # Проверяем, содержит ли заголовок ключевое слово
                if keyword.lower() in title.lower():
                    questions.append((title, link))

    return questions

# Ввод ключевого слова от пользователя
keyword = input("Введите ключевое слово для поиска: ")

# Указываем количество страниц для поиска
pages_to_search = 20  # Можно изменить на нужное количество страниц

# Поиск вопросов
results = search_questions(keyword, pages=pages_to_search)

# Вывод результатов
print(f"\nНайдено вопросов: {len(results)}")
for title, link in results:
    print(f"Заголовок: {title}")
    print(f"Ссылка: {link}")
    print("-" * 80)