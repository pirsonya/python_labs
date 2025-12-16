import csv
from pathlib import Path
from datetime import datetime, date
from typing import List, Dict, Any 

class Student:
    def __init__(self, fio: str, birthdate: date, group: str, gpa: float):
        self.fio = fio
        self.birthdate = birthdate  
        self.group = group
        self.gpa = gpa
    
    def __repr__(self):
        return f"Student({self.fio}, {self.birthdate}, {self.group}, {self.gpa})"

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
    
    def _read_all(self) -> List[dict]:
        if not self.path.exists():
            return []
        
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    
    def _write_all(self, rows: List[dict]) -> None:
        with open(self.path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self) -> List[Student]:
        rows = self._read_all()
        students = []
        
        for row in rows:
            try:
                birthdate = datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
                gpa = float(row['gpa'])
                
                student = Student(
                    fio=row['fio'],
                    birthdate=birthdate,
                    group=row['group'],
                    gpa=gpa
                )
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при чтении студента: {e}")
                continue
        
        return students
    
    def add(self, student: Student):
        rows = self._read_all()
        
        for row in rows:
            if row['fio'] == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        new_row = {
            'fio': student.fio,
            'birthdate': student.birthdate.isoformat(),
            'group': student.group,
            'gpa': str(student.gpa)
        }
        rows.append(new_row)
        self._write_all(rows)

    def count(self) -> int:
        rows = self._read_all()
        return len(rows)
    
    
    def find(self, substr: str) -> List[Student]:
        all_students = self.list()
        return [student for student in all_students if substr.lower() in student.fio.lower()]
    
    def remove(self, fio: str) -> bool:
        rows = self._read_all()
        original_count = len(rows)
        rows = [row for row in rows if row['fio'] != fio]
        
        if len(rows) < original_count:
            self._write_all(rows)
            return True
        return False
    
    def update(self, fio: str, **fields) -> bool:
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                for field, value in fields.items():
                    if field in ['fio', 'birthdate', 'group', 'gpa']:
                        if field == 'birthdate' and isinstance(value, date):
                            row[field] = value.isoformat()
                        elif field == 'gpa':
                            row[field] = str(value)
                        else:
                            row[field] = value
                updated = True
        
        if updated:
            self._write_all(rows)
        
        return updated


