import pytest
import json
import csv
import sys
import os
from pathlib import Path

from src.lab05.json_csv import json_to_csv, csv_to_json


# корректная конвертанция json->csv
def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Ivan", "age": 25},
        {"name": "Maria", "age": 30},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())
    assert rows[0]["name"] == "Ivan"
    assert rows[0]["age"] == "25"
    assert rows[1]["name"] == "Maria"
    assert rows[1]["age"] == "30"


# корректная конвертанция csv->json
def test_csv_to_json_roundtrip(tmp_path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    csv_data = """name,age,city
Ivan,25,Moscow
Maria,30,SPb"""
    src.write_text(csv_data, encoding="utf-8")

    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Ivan"
    assert data[0]["age"] == "25"
    assert data[0]["city"] == "Moscow"
    assert data[1]["name"] == "Maria"
    assert data[1]["age"] == "30"


# пустой лист
def test_json_to_csv_empty_list(tmp_path):
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"
    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


# несуществ файл
def test_json_to_csv_not_list(tmp_path):
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"
    src.write_text('{"name": "Ivan"}', encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")


# пустой лист
def test_csv_to_json_empty_file(tmp_path):
    src = tmp_path / "test.csv"
    dst = tmp_path / "test.json"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_csv_to_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")


# неправ расширение файла
def test_json_to_csv_wrong_extension(tmp_path):
    src = tmp_path / "test.txt"
    dst = tmp_path / "test.txt"
    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_wrong_csv_extension(tmp_path):
    json_file = tmp_path / "test.json"
    csv_file = tmp_path / "test.txt"

    data = [{"name": "Ivan", "age": 25}]
    json_file.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(json_file), str(csv_file))
