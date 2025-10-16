import json
import csv
import os
import sys


def json_to_csv(json_file):
    if not os.path.exists(json_file):
        raise FileNotFoundError(f"Файл {json_file} не найден.")

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, dict) or len(data) != 1:
        raise ValueError("Некорректная структура JSON. Ожидается один ключ верхнего уровня.")

    main_key = list(data.keys())[0]
    records = data[main_key]

    if not isinstance(records, list) or not all(isinstance(item, dict) for item in records):
        raise ValueError("Основная запись должна быть списком словарей.")

    csv_filename = f"{main_key}.csv"
    csv_path = os.path.join(os.path.dirname(json_file), csv_filename)

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

    print(f"CSV-файл сохранен: {csv_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python json2csv.py <имя_файла.json>")
        sys.exit(1)

    try:
        json_to_csv(sys.argv[1])
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)