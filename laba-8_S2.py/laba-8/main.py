import csv
import os
import random

def load_data(filename, separator=','):
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=separator)
        headers = next(reader)
        data = [row for row in reader]
    return headers, data

def Show(headers, data, output_type='top', n=5, separator=','):
    total = len(data)
    if total == 0:
        print("Нет данных для отображения")
        return

    n = min(n, total)
    if total < 5:
        print(f"Внимание: всего {total} строк")

    if output_type == 'top':
        selected = data[:n]
    elif output_type == 'bottom':
        selected = data[-n:]
    elif output_type == 'random':
        selected = random.sample(data, n)
    else:
        print("Неверный тип вывода. Используется 'top'")
        selected = data[:n]

    col_widths = [len(header) for header in headers]
    for row in selected:
        for i, item in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(item)))

    format_str = separator.join([f"{{:<{w}}}" for w in col_widths])

    print(format_str.format(*headers))
    print("-" * (sum(col_widths) + (len(headers)-1)*len(separator)))

    for row in selected:
        print(format_str.format(*[str(item).ljust(width) for item, width in zip(row, col_widths)]))

    print(f"\nПоказано {len(selected)} из {total} строк")

def Info(headers, data):
    rows = len(data)
    cols = len(headers)
    print(f"Данные: {rows} строк × {cols} колонок\n")

    print("Статистика по колонкам:")
    for i, header in enumerate(headers):
        non_empty = 0
        col_types = set()
        for row in data:
            if i < len(row) and row[i].strip():
                non_empty += 1
                value = row[i]
                if value.isdigit():
                    col_types.add(int)
                else:
                    try:
                        float(value)
                        col_types.add(float)
                    except:
                        col_types.add(str)
            else:
                col_types.add(type(None))

        type_str = "mixed" if len(col_types) > 1 else str(col_types.pop()).split("'")[1]
        print(f"{header.ljust(15)} {str(non_empty).ljust(5)} {type_str}")

def DelNaN(data):
    return [row for row in data if all(field.strip() != '' for field in row)]

def MakeDS(data, headers):
    random.shuffle(data)
    split = int(0.7 * len(data))

    os.makedirs("workdata/Learning", exist_ok=True)
    os.makedirs("workdata/Testing", exist_ok=True)

    with open("workdata/Learning/train.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data[:split])

    with open("workdata/Testing/test.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data[split:])

    print("Наборы успешно созданы в папке workdata")

def main():
    try:
        headers, data = load_data("data.csv")
    except FileNotFoundError:
        print("Ошибка: файл data.csv не найден")
        return

    print("\n=== Пример данных (первые 5 строк) ===")
    Show(headers, data, n=5)

    print("\n=== Информация о данных ===")
    Info(headers, data)

    print("\n=== Очистка данных ===")
    cleaned_data = DelNaN(data)
    print(f"Удалено {len(data) - len(cleaned_data)} строк")
    data = cleaned_data

    print("\n=== Создание наборов данных ===")
    MakeDS(data, headers)

if __name__ == "__main__":
    main()