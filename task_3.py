import csv

def add_product():
    new_product = input("\nВведите новый товар (название,цена,количество): ")

    try:
        name, price, quantity = new_product.split(",")
        price = int(price)
        quantity = int(quantity)
        with open("resource/products.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, price, quantity])
        print(f"Товар '{name}' добавлен")
        return True

    except ValueError:
        print("Ошибка: введите данные в формате: Название,Цена,Количество!")
        print("Пример: Фисташки,900,10")
        return False

def search_product_by_name(product_name):
    with open("resource/products.csv", "r") as file:
        reader = csv.reader(file)
        found = False
        print(f"\nРезультаты поиска по запросу '{product_name}':")
        next(reader, None)
        for i in reader:
            name, price, quantity = i
            if product_name.lower() in name.lower():
                print(f"Название: {name}, Цена: {price}, Количество: {quantity}")
                found = True
        if not found:
            print(f"Товар '{product_name}' не найден")

def sum_products():
    total = 0
    with open("resource/products.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            name, price_str, quantity_str = row
            price = int(price_str)
            quantity = int(quantity_str)
            total += price * quantity
    print(f"\nОбщая стоимость всех товаров: {total}")
    return total

products = [
    ["Яблоки", 100, 50],
    ["Бананы", 80, 30],
    ["Молоко", 120, 20],
    ["Хлеб", 40, 100]
]

with open("resource/products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "Цена", "Количество"])
    writer.writerows(products)

while True:
    print("\nВыберите действие:")
    print("1. Добавить товар")
    print("2. Найти товар")
    print("3. Общая стоимость товаров")
    print("4. Выход")

    user_choice = input("Выберите действие: ")

    if user_choice == "1":
        add_product()
    elif user_choice == "2":
        product_to_find = input("Введите название товара для поиска: ")
        search_product_by_name(product_to_find)
    elif user_choice == "3":
        sum_products()
    elif user_choice == "4":
        print("Вы вышли")
        break
    else:
        print("Ошибка: введите 1, 2, 3 или 4!")