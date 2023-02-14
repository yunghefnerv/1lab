groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]
def print_students(students, ball):
    for student in students:
        if ball_student(student) >= ball:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
                  str(student["marks"]).ljust(20))
def ball_student(student):
    sum = 0
    n = 0
    for i in student["marks"]:
        sum += i
        n += 1
    return  sum/n
print_students(groupmates, 4.5)


