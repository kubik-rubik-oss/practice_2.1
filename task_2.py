def average_score(filename):
    results = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                name, grades_str = line.split(":")
                grades = [int(grade) for grade in grades_str.split(",")]
                average = sum(grades) / len(grades)
                results.append((name, average))
    return results

def higher_than_four(filename):
    results = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                name, grades_str = line.split(":")
                grades = [int(grade) for grade in grades_str.split(",")]
                average = sum(grades) / len(grades)
                if average >= 4:
                    results.append((name, average))
    return results

def highest_score(filename):
    results = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                name, grades_str = line.split(":")
                grades = [int(grade) for grade in grades_str.split(",")]
                average = sum(grades) / len(grades)
                results.append((name, average))
    return max(results)

students = [
    "Иванов Иван:5,4,3,5",
    "Петров Петр:4,3,4,4",
    "Сидорова Мария:5,5,5,5"
]

with open("resource/students.txt", "w") as file:
    for i in students:
        file.write(i + "\n")

print("Файл students.txt создан. Содержимое файла students.txt:\n")

with open("resource/students.txt", "r") as file:
    for line in file:
        print(line, end="")

with open("resource/results.txt", "w") as file_2:
    file_2.write("Студенты с баллом выше 4.0:\n\n")
    for name, avg in higher_than_four("resource/students.txt"):
        file_2.write(f"{name}: {avg}\n")

print(f"\nСредний балл студента: {average_score('resource/students.txt')}")
print(f"Наивысший балл у: {highest_score('resource/students.txt')}")
