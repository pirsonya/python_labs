from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("неккоректный формат даты")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("неккоректный формат gpa")
        
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        if birth_date > date.today():
            raise ValueError("некорректная дата рождения")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def to_dict(self) -> Dict[str, Any]:
        if not self.fio or not isinstance(self.fio, str):
            raise ValueError
        
        if not self.birthdate or not isinstance(self.birthdate, str):
            raise ValueError
        
        if not self.group or not isinstance(self.group, str):
            raise ValueError
        
        if not isinstance(self.gpa, (int, float)):
            raise ValueError
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        required_fields = ["fio", "birthdate", "group", "gpa"]
        for field in required_fields:
            if field not in data:
                raise ValueError("отсутствует поле")
        
        if not isinstance(data["fio"], str):
            raise ValueError("некорректный формат фио")
        
        if not isinstance(data["birthdate"], str):
            raise ValueError("некорректный формат даты")
        
        if not isinstance(data["group"], str):
            raise ValueError("некорректный формат группы")
        
        try:
            gpa = float(data["gpa"])
        except (ValueError, TypeError):
            raise ValueError("некорректное значение gpa")
        
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=gpa
        )
    def __str__(self) -> str:
        return (f"{self.fio}, группа: {self.group}, "
                f"GPA: {self.gpa:.2f}, возраст: {self.age()} лет, "
                f"дата рождения: {self.birthdate}")

    def __repr__(self) -> str:
        return (f"Student(fio='{self.fio}', "
                f"birthdate='{self.birthdate}', "
                f"group='{self.group}', "
                f"gpa={self.gpa})")

if __name__ == "__main__":
    import json
    from pathlib import Path
    
    base_dir = Path(__file__).parent.parent.parent
    input_file = base_dir / "data" / "lab08" / "students_input.json"
    output_file = base_dir / "data" / "lab08" / "students_output.json"
    if not input_file.exists():
        print("файл не найден")
        exit(1)
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and "students" in data:
            students_data = data["students"]
        elif isinstance(data, list):
            students_data = data
        else:
            print("некорректный формат данных")
            exit(1)
        
        students = []
        for student_dict in students_data:
            try:
                student = Student.from_dict(student_dict)
                students.append(student)
            except ValueError as e:
                print("пропущен студент")
                continue
        output_data = [student.to_dict() for student in students]
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка: {e}")
 