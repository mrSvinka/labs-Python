import json

try:

    with open("ex_2.json", "r") as f:
        raw_data = f.read()
        fixed_data = f"[{raw_data}]"  # Добавляем квадратные скобки
        users = json.loads(fixed_data)

    # Создание словаря: имя → телефон
    user_phones = {}
    for user in users:
        name = user.get("name", "Unknown")
        phone = user.get("phoneNumber", "N/A")
        user_phones[name] = phone

    # Вывод результата
    print("Словарь пользователей (имя → телефон):")
    for name, phone in user_phones.items():
        print(f"- {name}: {phone}")

except json.JSONDecodeError:
    print("Ошибка: Некорректный JSON-файл.")
except KeyError as e:
    print(f"Ошибка: Отсутствует ключ {e}.")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")