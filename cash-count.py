import sys

def calc_sum(nums):
    return sum(nums)

def calc_mul(nums):
    result = 1
    for n in nums:
        result *= n
    return result

def calc_avg(nums):
    return sum(nums) / len(nums)

args = sys.argv[1:]

# Значения по умолчанию
input_file = "input.txt"
output_file = None
operation = None

# Разбор аргументов командной строки
i = 0
while i < len(args):
    if args[i] == "--input":
        if i + 1 < len(args) and not args[i+1].startswith('-'):
            input_file = args[i+1]
            i += 1
    elif args[i] == "--output":
        if i + 1 < len(args) and not args[i+1].startswith('-'):
            output_file = args[i+1]
            i += 1
        else:
            output_file = "output.txt"   # имя по умолчанию, если следующего аргумента нет
    elif args[i] in ("-sum", "-mul", "-arv"):
        operation = args[i]
    i += 1

# Проверка наличия операции
if operation is None:
    print("Ошибка: не указана операция (-sum, -mul, -arv)")
    sys.exit(1)

# Чтение входного файла
try:
    with open(input_file, "r") as f:
        line = f.readline()
        numbers = list(map(int, line.split()))
except FileNotFoundError:
    print(f"Ошибка: файл '{input_file}' не найден.")
    sys.exit(1)


if operation == "-sum":
    result = calc_sum(numbers)
elif operation == "-mul":
    result = calc_mul(numbers)
else: 
    result = calc_avg(numbers)

if output_file:
    with open(output_file, "w") as f:
        f.write(str(result))
else:
    print(result)
