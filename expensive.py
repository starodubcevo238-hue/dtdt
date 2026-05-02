import cli
import logica

def main():

    command, params = cli.get_args_args()
    

    if not command:
        print("Ошибка: Команда не указана.")
        print("Использование: python main.py <команда> [аргументы]")
        print("Команды: add, add-category, list, total")
        return

    if command == "add-category":
        logica.add_category(params)
    elif command == "add":
        logica.add_expense(params)
    elif command == "list":
        logica.list_expenses(params)
    elif command == "total":
        logica.show_total(params)
    else:

        print(f"Ошибка: Неизвестная команда '{command}'.")

if __name__=="__main__":
    main()