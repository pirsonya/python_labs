import sys
from pathlib import Path
from datetime import date
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.lab08.models import Student
from src.lab09.group import Group

def test_group():
    test_csv = "data/lab09/students.csv"
    group = Group(test_csv)
    try:
        students = group.list()
        print(f"Количество студентов: {len(students)}")
    except Exception as e:
        print(f"Ошибка: {e}")
        students = []
        print(f"Количество студентов: 0")
    print()
    
    if students:
        print("1. Все студенты:")
        for i, student in enumerate(students, 1):
            print(f"  {i}. {student.fio}, {student.group}, GPA: {student.gpa}")
    else:
        print("1. В списке нет студентов")
    print()
    
    print("2. Добавление новых студентов:")
    try:
        new_student = Student(
            fio="Петров Дмитрий Алексеевич",
            birthdate="2004-01-20",  
            group="БИВТ-22-1",
            gpa=4.0
        )
        group.add(new_student)
        print(f"  Добавлен: {new_student.fio}")
    except Exception as e:
        print(f"  Ошибка при добавлении: {e}")
    print()
    
    print("3. Поиск 'Иванов':")
    found = group.find("Иванов")
    for i, student in enumerate(found, 1):
        print(f"  {i}. {student.fio}, {student.group}")
    print()
    
    print("4. Обновление группы, gpa студента 'Иванов Иван Иванович':")
    updated = group.update(
        "Иванов Иван Иванович",
        gpa=4.5,
        group="БИВТ-25-5"
    )
    if updated:
        print("  Данные обновлены")
        student = group.find("Иванов")[0]
        print(f"  Новые данные: {student.group}, GPA: {student.gpa}")
    else:
        print("  Студент не найден")
    print()
    
    print("5. Удаление студента 'Петров Петр Петрович':")
    removed = group.remove("Петров Петр Петрович")
    if removed:
        print("  Студент удален")
    else:
        print("  Студент не найден")
    print()
    
    print("6. Финальный список:")
    students = group.list()
    for i, student in enumerate(students, 1):
        print(f"  {i}. {student.fio}, {student.group}, GPA: {student.gpa}")
    print(f"  Всего: {group.count()} студент(ов)")
    

if __name__=="__main__":
    test_group()