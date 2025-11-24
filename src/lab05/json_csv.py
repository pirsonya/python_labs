import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    if not Path(json_path).exists():
        raise FileNotFoundError
    if not json_path.lower().endswith(".json"):
        raise ValueError(f"{json_path}")

    if not csv_path.lower().endswith(".csv"):
        raise ValueError(f"{csv_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not data or not isinstance(data, list):
        raise ValueError
    keys = set()
    for item in data:
        keys.update(item.keys())
    keys = sorted(keys)

    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for item in data:
            row = {key: item.get(key, "") for key in keys}
            writer.writerow(row)
    print(f"{csv_path}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    if not Path(csv_path).exists():
        raise FileNotFoundError

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    if not data:
        raise ValueError
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{json_path}")


# if __name__ == "__main__":
#     json_to_csv("data/samples/people.json", "data/output.csv")
#     csv_to_json("data/samples/people.csv", "data/output.json")
