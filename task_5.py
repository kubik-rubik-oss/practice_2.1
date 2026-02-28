import json

def viewing_books():
    with open("resource/library.json", "r") as file:
        all_books = file.readlines()
        if all_books:
            print("Список всех книг:")
            for i in all_books:
                print(i.strip())

def search_book():
    with open("resource/library.json", "r") as file:
        data = file.read()

    data_fixed = "[" + data.replace("},\n{", "},{").replace("\n", "") + "]"
    books = json.loads(data_fixed)

    search_type = input("Введите тип поиска (1 - по названию. 2 - по автору): ")

    if search_type not in ["1", "2"]:
        print("Ошибка: некорректный выбор!")
        return

    word = input("Введите слово для поиска: ").lower()

    if len(word) < 2:
        print("Ошибка: для поиска нужно ввести хотя бы 2 символа!")
        return
    if not word:
        print("Не введено слово для поиска!")
        return

    results = []
    if search_type == "1":
        for book in books:
            if word in book['title'].lower():
                results.append(book)
        search_by_text = "названию"
    elif search_type == "2":
        for book in books:
            if word in book['author'].lower():
                results.append(book)
        search_by_text = "автору"
    if results:
        print(f"\nНайдено {len(results)} книг по {search_by_text} '{word}':")
        for book in results:
            status = "Доступна" if book['available'] else "Выдана"
            print(f"{book['id']} - {book['title']} - {book['author']} ({book['year']}) - {status}")
    else:
        print(f"Книг по {search_by_text} '{word}' не найдено")

def add_book():
    with open("resource/library.json", "r") as file:
        data = file.read()
    if data.strip():
        data_fixed = "[" + data.replace("},\n{", "},{").replace("\n", "") + "]"
        books = json.loads(data_fixed)
    else:
        books = []
    max_id = 0
    if books:
        max_id = max(book['id'] for book in books)
    title = input("Введите название книги: ")
    if not title:
        print("Название книги не может быть пустым!")
        return

    author = input("Введите автора книги: ")
    if not author:
        print("Автор книги не может быть пустым!")
        return
    year = input("Введите год издания: ")
    new_book = {
        "id": max_id + 1,
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(new_book)

    with open('resource/library.json', 'w') as file:
        for i, book in enumerate(books):
            json.dump(book, file, ensure_ascii=False, indent=4)
            if i != len(books) - 1:
                file.write(",\n")

    print(f"\nКнига успешно добавлена!")
    print(f"ID: {new_book['id']}")
    print(f"Название: {new_book['title']}")
    print(f"Автор: {new_book['author']}")
    print(f"Год: {new_book['year']}")
    print(f"Статус: Доступна")

def change_status():
    with open("resource/library.json", "r") as file:
        data = file.read()
    books = json.loads("[" + data.replace("},\n{", "},{").replace("\n", "") + "]")
    print("\nКниги:")
    for i in books:
        print(f"{i['id']}: {i['title']} - {'Доступна' if i['available'] else 'Выдана'}")

    book_id = int(input("ID книги: "))

    for i in books:
        if i['id'] == book_id:
            i['available'] = not i['available']
            with open('resource/library.json', 'w') as file:
                for j, book in enumerate(books):
                    json.dump(book, file, ensure_ascii=False, indent = 4)
                    if j != len(books) - 1:
                        file.write(",\n")
            print(f"Статус изменён")
            return
    print("Ошибка: книга не найдена!")

def delete_book():
    with open("resource/library.json", "r") as file:
        data = file.read()
    books = json.loads("[" + data.replace("},\n{", "},{").replace("\n", "") + "]")
    print("\nКниги:")
    for i in books:
        print(f"{i['id']}. {i['title']}")
    try:
        book_id = int(input("\nВведите ID книги для удаления: "))
    except:
        print("Ошибка: нужно ввести число!")
        return
    for i in books:
        if i['id'] == book_id:
            books = [b for b in books if b['id'] != book_id]
            with open('resource/library.json', 'w') as file:
                for j, b in enumerate(books):
                    json.dump(b, file, ensure_ascii=False, indent=4)
                    if j != len(books) - 1:
                        file.write(",\n")
            print(f"Книга с ID {book_id} удалена")
            return
    print(f"Ошибка: книга с ID {book_id} не найдена!")

def export_available_books():
    with open("resource/library.json", "r") as file:
        books = json.loads("[" + file.read().replace("},\n{", "},{").replace("\n", "") + "]")
    available = [b for b in books if b['available']]

    with open("resource/available_books.txt", "w") as file:
        for i in available:
            file.write(f"{i['id']}: {i['title']} - {'Доступна' if i['available'] else 'Выдана'}")
    print(f"Сохранено {len(available)} книг")

library =[
    {
        "id": 1,
        "title": "Мастер и Маргарита",
        "author": "Булгаков",
        "year": 1967,
        "available": True
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Достоевский",
        "year": 1866,
        "available": False
    }
]

with open('resource/library.json', 'w') as file:
    for i, book in enumerate(library):
        json.dump(book, file, ensure_ascii=False, indent=4)
        if i != len(library) - 1:
            file.write(",\n")

with open('resource/library.json', 'r') as file:
    print("Содержимое файла library.json:")
    content = file.read()
    print(content)

while True:
    print("\nВыберите действие:")
    print("1. Просмотр всех книг")
    print("2. Поиск по автору/названию")
    print("3. Добавление новой книги")
    print("4. Изменение статуса доступности (взята/возвращена)")
    print("5. Удаление книги по ID")
    print("6. Экспорт списка доступных книг в текстовый файл available_books.txt")
    print("7. Выход")

    user_choice = input("Выберите действие: ")

    if user_choice == "1":
        viewing_books()
    elif user_choice == "2":
        search_book()
    elif user_choice == "3":
        add_book()
    elif user_choice == "4":
        change_status()
    elif user_choice == "5":
        delete_book()
    elif user_choice == "6":
        export_available_books()
    elif user_choice == "7":
        print("Вы вышли")
        break
    else:
        print("Ошибка: введите 1, 2, 3, 4, 5, 6 или 7!")