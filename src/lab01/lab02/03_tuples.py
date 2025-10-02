def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
#проверка: фио НЕ пустое, группа НЕ пустая
    if len(str(fio).strip())<1 or len(str(group).strip())<1:
        raise ValueError
#проверка: GPA введен корректно
    if gpa<0:
        raise ValueError
#проверка: GPA должен быть вещ.
    if not isinstance(gpa, (float)):
        raise TypeError
#удаляем лишние пробелы и делим на фам,имя,отч/фам,имя
    right_fio = fio.strip()
    right_fio_part = right_fio.split()

    if len(right_fio_part)==3:
        initials = f"{right_fio_part[1][0]}.{right_fio_part[2][0]}."
        res=initials.upper()
        right_fio = f'{right_fio_part[0].title()} {res}'
    if len(right_fio_part)==2:
        initials = f'{right_fio_part[1][0]}.{right_fio_part[1][0]}.'
        res=initials.upper()
        right_fio = f'{right_fio_part[0].title()} {res}'
    return f'{right_fio}, гр. {group.strip()}, GPA {gpa:.2f}'

print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))



### Тест-кейсы (минимум)
# - `("Иванов Иван Иванович", "BIVT-25", 4.6)` → `"Иванов И.И., гр. BIVT-25, GPA 4.60"`
# - `("Петров Пётр", "IKBO-12", 5.0)` → `"Петров П.П., гр. IKBO-12, GPA 5.00"`
# - `("  сидорова  анна   сергеевна ", "ABB-01", 3.999)` → `"Сидорова А.С., гр. ABB-01, GPA 4.00"`