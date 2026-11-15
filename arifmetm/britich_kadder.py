steps_in_part = 0
floor = 0
total_seconds = 0

print("\n=============\n")

print(
    "Данная программа считает на сколько секунд увеличится ваша жизнь при поднятии пешком на этаж на котором вы живёте"
)
print()

steps_in_part = int(input("Введите количество ступенек в пролёте: "))

floor = int(input("Введите этаж на котором вы живёте: "))

total_seconds = steps_in_part * 2 * floor * 10

print()

print(f"Ваша жизнь при поднятии на {floor} этаж увеличилась на {total_seconds} секунд")

print("\n=============\n")