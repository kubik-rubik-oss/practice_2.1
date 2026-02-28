from datetime import datetime

def calculator():
    while True:
        try:
            num_1 = float(input("Введите первое число: "))
            break
        except ValueError:
            print("Ошибка: введите число!")
    while True:
        try:
            num_2 = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Ошибка: введите число!")

    operation = input("Введите операцию (+, -, *, /): ")

    if operation not in ['+', '-', '*', '/']:
        print("Ошибка: неверная операция!")
        return None
    if operation == '/' and num_2 == 0:
        print("Ошибка: деление на ноль невозможно!")
        return None
    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "*":
        result = num_1 * num_2
    else:
        result = num_1 / num_2

    operation_str = f"{num_1} {operation} {num_2} = {result}"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{current_time}] {operation_str}"

    return {
        'operation': operation_str,
        'log_entry': log_entry,
        'result': result
    }

def show_last_operations():
    with open("resource/calculator.log", "r") as file:
        all_logs = file.readlines()
        if all_logs:
            print("Последние операции:")
            for i in all_logs[-5:]:
                print(i.strip())

show_last_operations()
calculation_data = calculator()

with open("resource/calculator.log", "a") as file:
    file.write(calculation_data['log_entry'] + "\n")

print(f"\nРезультат: {calculation_data['operation']}")
print(f"Запись добавлена в calculator.log")

while True:
    choice = input("Хотите очистить содержимое файла calculator.log? да/нет: ").lower()

    if choice == "да":
        with open('resource/calculator.log', 'w') as f:
            pass
        break
    elif choice == "нет":
        print("Программа завершена")
        break
    else:
        print("Ошибка: введите да или нет!")
        continue
