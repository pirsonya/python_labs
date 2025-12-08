import json
from typing import List
from pathlib import Path

try:
    from models import Student
except ImportError:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from models import Student

def students_to_json(students: List[Student], path: str | Path) -> None:
    data = [s.to_dict() for s in students]
    path = Path(path) if isinstance(path, str) else path
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str | Path) -> List[Student]:
    path = Path(path) if isinstance(path, str) else path
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict) and "students" in data:
        students_data = data["students"]
    else:
        students_data = data
    return [Student.from_dict(d) for d in students_data]

if __name__ == "__main__":
    current_dir = Path(__file__).parent
    project_root = current_dir.parent.parent
    
    input_path = project_root / "data" / "lab08" / "students_input.json"
    output_path = project_root / "data" / "lab08" / "students_output.json"
    
    students = students_from_json(input_path)
    students_to_json(students, output_path)