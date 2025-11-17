import argparse
import os
import sys
import json
import csv
import openpyxl
from pathlib import Path
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if not Path(csv_path).exists():
        raise FileNotFoundError

    if not csv_path.lower().endswith('.csv'):
        raise ValueError

    if not xlsx_path.lower().endswith('.xlsx'):
        raise ValueError
        
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            rows = list(csv.reader(f))
    except Exception as e:
        raise ValueError

    if not rows:
        raise ValueError

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
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max_len

    wb.save(xlsx_path)
# if __name__ == "__main__":
#     csv_to_xlsx("data/samples/cities.csv", "data/cities.xlsx") 
def json_to_csv(json_path: str, csv_path: str) -> None:
    if not Path(json_path).exists():
        raise FileNotFoundError
    if not json_path.lower().endswith('.json'):
        raise ValueError(f"{json_path}")
    
    if not csv_path.lower().endswith('.csv'):
        raise ValueError(f"{csv_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not data or not isinstance(data, list):
        raise ValueError
    keys = set()
    for item in data:
        keys.update(item.keys())
    keys = sorted(keys)
    
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for item in data:
            row = {key: item.get(key, '') for key in keys}
            writer.writerow(row)
    print(f'{csv_path}')
def csv_to_json(csv_path: str, json_path: str) -> None:
    if not Path(csv_path).exists():
        raise FileNotFoundError
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    if not data:
        raise ValueError
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{json_path}')
# if __name__ == "__main__":
#     json_to_csv("data/samples/people.json", "data/output.csv")
#     csv_to_json("data/samples/people.csv", "data/output.json")
def validate_files(input_file, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError
    
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Koнвертеры данных")
    sub = parser.add_subparsers(dest='cmd')
    
    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest='input', required=True)
    p1.add_argument("--out", dest='output', required=True)
    
    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest='input', required=True)
    p2.add_argument("--out", dest='output', required=True)
    
    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest='input', required=True)
    p3.add_argument("--out", dest='output', required=True)
    
    args = parser.parse_args()
    try:
        if args.cmd == "json2csv":
            validate_files(args.input, args.output)
            json_to_csv(args.input, args.output)
            print(f"{args.input} -> {args.output}")
        elif args.cmd == "csv2json":
            validate_files(args.input, args.output)
            csv_to_json(args.input, args.output)
            print(f"{args.input} -> {args.output}")
        elif args.cmd == "csv2xlsx":
            validate_files(args.input, args.output)
            csv_to_xlsx(args.input, args.output)
            print(f"{args.input} -> {args.output}")
        else:
            parser.print_help()
            
    except FileNotFoundError as e:
        print(f"{e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"{e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()