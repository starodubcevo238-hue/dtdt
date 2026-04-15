import json
import os
import sys
DATA_FILE = "my_notes.json"





def load_d():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return{}
        

def save_d(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_entry(data):
    name = input("введите имя:").strip()
    Value = input("введите описание:").strip()
    category = input("введите категорию:").strip().lower()

    if category not in data:
        data[category] = {}
    data[category][name] = Value
    save_d(data)
    print("добавлено!")
    
def show_all(data):
    if not  data:
        print("пусто")
        return
    for cat,items in data.items():
        print(f"\n  {cat}")
        for name,desc in items.items():
            print(f"\n  {name}:{desc}")    



def main():
    data = load_d()
    while True:
        print("\n--- МЕНЮ ---")
        print("python expenses.py add. Добавить запись")
        print("python expenses.py all list. Показать всё")
        print("python expenses.py list. Показать по категории")
        print("python expenses.py exit. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "python expenses.py add":
            add_entry(data)
        elif choice == "python expenses.py all list":
            show_all(data)
        elif choice == "python expenses.py exit":
            print("До свидания!")            
            break
        else:
            print(" Неверный выбор.")


if __name__ == "__main__":
    main()
