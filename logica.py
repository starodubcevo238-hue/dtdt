import json
import os

FILE_NAME = "data.json"

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:

            return {}
    return {}

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_category(params):

    if not params:
        print("Ошибка: Вы не указали название категории.")
        return
        
    category = params[0].lower()
    data = load_data()
    

    if category in data:
        print(f"Ошибка: Категория '{category}' уже существует.")
        return
        
    data[category] = []
    save_data(data)
    print(f"Успех: Категория '{category}' создана.")

def add_expense(params):

    if len(params) < 3:
        print("Ошибка: Мало данных. Формат: add <цена> <категория> <название>")
        return
        

    try:
        price = float(params[0])
        if price <= 0:
            print("Ошибка: Цена должна быть больше нуля.")
            return
    except ValueError:
        print("Ошибка: Цена должна быть числом (например, 150 или 150.5).")
        return
        
    category = params[1].lower()
    name = " ".join(params[2:])
    data = load_data()
    

    if category not in data:
        print(f"Ошибка: Категории '{category}' нет. Сначала создайте её (add-category).")
        return
        
    data[category].append({"name": name, "price": price})
    save_data(data)
    print(f"Успех: Расход '{name}' на сумму {price} добавлен.")

def list_expenses(params):
    data = load_data()
    if not data:
        print("База данных пуста.")
        return
        
    category = params[0].lower() if params else None
    
    if category:

        if category in data:
            print(f"--- Расходы в категории '{category}' ---")
            for item in data[category]:
                print(f"- {item['name']}: {item['price']}")
        else:
            print(f"Ошибка: Категория '{category}' не найдена.")
    else:
        for cat_name, items in data.items():
            print(f"[{cat_name}]: сумма {sum(i['price'] for i in items)}")

def show_total(params):
    data = load_data()
    if not data:
        print("Нет данных для подсчета.")
        return
        
    category = params[0].lower() if params else None
    
    if category:
        if category in data:
            total = sum(i['price'] for i in data[category])
            print(f"Итого по категории '{category}': {total}")
        else:
            print(f"Ошибка: Категория '{category}' не найдена.")
    else:
        total = sum(sum(i["price"] for i in items) for items in data.values())
        print(f"Всего потрачено: {total}")