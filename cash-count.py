    print("Расход успешно добавлен!")


def add_cat(data, args):
    if not args:
        print("Ошибка: введите название категории!")
        return
    category = args[0].strip().lower()

    if category not in data:
        data[category] = []
        save_d(data)
        print(f"Категория '{category}' добавлена!")
    else:
        print(f"Категория '{category}' уже существует.")


def show_list(data, args):
    if not data:
        print("Список пуст.")
        return
    if args:
        category_filter = args[0].lower()
        if category_filter in data:
            print(f"\n--- {category_filter} ---")
            if not data[category_filter]:
                print("  (пусто)")
            for item in data[category_filter]:
                print(f"  {item['name']}: {item['cost']}")
        else:
            print("Ошибка: такой категории нет.")
    else:
        for cat, items in data.items():
            print(f"\n--- {cat} ---")
            if not items:
                print("  (пусто)")
            for item in items:
                print(f"  {item['name']}: {item['cost']}")


def calc_total(data, args):
    total = 0.0
    if args:
        category_filter = args[0].lower()
        if category_filter in data:
            for item in data[category_filter]:
                total += item['cost']
            print(f"Сумма расходов в категории '{category_filter}': {total}")
        else:
            print("Ошибка: такой категории нет.")
    else:
        for items in data.values():
            for item in items:
                total += item['cost']
        print(f"Общая сумма всех расходов: {total}")


def execute_command(data, command, args):
    if command == "add":
        add_entry(data, args)
    elif command == "add-category":
        add_cat(data, args)
    elif command == "list":
        show_list(data, args)
    elif command == "total":
        calc_total(data, args)
    else:
        print("Неверная команда.")


def main():
    data = load_d()

    if len(sys.argv) > 1:
        args_list = sys.argv[1:]

        if args_list[0].endswith('.py'):
            args_list = args_list[1:]

        if args_list:
            command = args_list[0].lower()
            args = args_list[1:]
            execute_command(data, command, args)
        return

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить расход: add <стоимость> <категория> <название>")
        print("2. Добавить категорию: add-category <категория>")
        print("3. Показать всё или по категории: list [категория]")
        print("4. Сумма всех или по категории: total [категория]")
        print("5. Выход: exit")

        choice = input("\nВведите команду: ").strip()

        if not choice:
            continue
        parts = choice.split()
        while parts and (parts[0] == "python" or parts[0].endswith(".py")):
            parts = parts[1:]
        if not parts:
            continue
        command = parts[0].lower()
        args = parts[1:]
        if command == "exit":
            print("До свидания!")
            break

        execute_command(data, command, args)


if __name__ == "__main__":
    main()
