import csv
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    with open(csv_path, 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)
    for col in ws.columns:
        max_len = 0
        for cell in col:
            if cell.value:
                max_len = max(max_len, len(str(cell.value)))
        col_letter=col[0].column_letter
        ws.column_dimensions[col[0].column_letter].width = max(max_len + 2, 8)
    
    wb.save(xlsx_path)

if __name__ == "__main__":
    csv_to_xlsx("data/samples/cities.csv", "data/cities.xlsx")

    
    