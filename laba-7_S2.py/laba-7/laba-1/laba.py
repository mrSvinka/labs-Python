import json
from jsonschema import validate, ValidationError

# Загрузка схемы
with open("schema_ex1.json", "r") as f:
    schema = json.load(f)

# Загрузка данных из ex_1_error.json
with open("ex_1_error.json", "r") as f:
    data_error = json.load(f)

# Валидация
try:
    validate(instance=data_error, schema=schema)
    print("Файл корректен.")
except ValidationError as e:
    print(f"Ошибка валидации: {e.message}")