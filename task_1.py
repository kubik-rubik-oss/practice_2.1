def count_lines(filename):
    count = 0
    with open(filename) as file:
        for i in file:
            count += 1
    return count

def count_words(filename):
    count = 0
    with open(filename) as file:
        for i in file:
            words = line.strip().split()
            count += len(words)
    return count

def max_line(filename):
    with open(filename) as file:
        longest = max(file, key = len)
    return longest

lines = [
    "Максим Черницов",
    "Юлия Кубрина",
    "Вадим Откуянов",
    "Алина_____Ревина",
    "Роман Сурнин"
]

with open("resource/text.txt", "w") as file:
    for i in lines:
        file.write(i + "\n")

print("Файл text.txt создан с 5 строками текста:\n")

with open("resource/text.txt", "r") as file:
    for line in file:
        print(line, end="")

print(f"\nКоличество строк в файле: {count_lines("resource/text.txt")}")
print(f"Количество слов в файле: {count_words("resource/text.txt")}")
print(f"Самая длинная строка: {max_line("resource/text.txt")}")