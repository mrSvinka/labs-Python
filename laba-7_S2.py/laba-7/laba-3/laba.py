import json

def add_invoice():
    try:
        # Загрузка исходных данных
        with open("ex_3.json", "r") as f:
            data = json.load(f)

        # Новый объект
        new_invoice = {
            "id": 3,
            "total": 300.00,
            "items": [
                {
                    "name": "item 4",
                    "quantity": 3,
                    "price": 100.00
                }
            ]
        }

        # Добавление объекта
        data["invoices"].append(new_invoice)

        # Сохранение обновленного файла
        with open("ex_3_updated.json", "w") as f:
            json.dump(data, f, indent=2)

        print("Файл ex_3_updated.json успешно создан.")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    add_invoice()