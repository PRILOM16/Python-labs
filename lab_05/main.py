import sys
from generators import ComputerIterator, computer_type_generator
from models import DesktopComputer, Laptop
import operations


def get_initial_data():
    return [
        DesktopComputer("Office-Base", "Intel Core i3", 8, "512GB SSD", 35000, "Micro-ATX"),
        DesktopComputer("Pro-Gaming", "Intel Core i5", 32, "2TB SSD", 120000, "ATX"),
        DesktopComputer("Workstation", "AMD Ryzen 9", 64, "4TB NVMe", 210000, "E-ATX"),
        Laptop("ThinkBook", "AMD Ryzen 5", 16, "512GB SSD", 65000, 14.0),
        Laptop("Legion Pro", "Intel Core i7", 32, "1TB SSD", 150000, 16.0),
        Laptop("Air-Light", "Intel Core i3", 8, "256GB SSD", 42000, 13.3),
    ]


def main():
    computers = get_initial_data()

    while True:
        print("\n===== ЛАБОРАТОРНАЯ 5: КОМПЬЮТЕРЫ=====")
        print("1. Показать все компьютеры")
        print("2. Получить список названий")
        print("3. Отфильтровать по объему RAM")
        print("4. Отсортировать по цене")
        print("5. Найти самый дорогой компьютер")
        print("6. Проверить наличие ПК с заданным RAM")
        print("7. Запустить генератор ноутбуков")
        print("8. Демонстрация собственного итератора)")
        print("9. Сравнение памяти: список vs генератор)")
        print("0. Выход")

        choice = input("Выберите пункт: ").strip()

        match choice:
            case "1":
                print("\n--- Каталог компьютеров ---")
                for comp in computers:
                    print(comp)

            case "2":
                names = operations.get_computer_names(computers)
                print(f"\nСписок названий (map): {names}")

            case "3":
                try:
                    limit = int(input("Введите минимальный объем RAM (ГБ): "))
                    filtered = operations.filter_by_min_ram(computers, limit)
                    print(f"\n--- Компьютеры с RAM >= {limit} ГБ (filter) ---")
                    for comp in filtered:
                        print(comp)
                except ValueError:
                    print("Ошибка: введите целое число.")

            case "4":
                order = input("1 - по возрастанию, 2 - по убыванию: ").strip()
                sorted_list = operations.sort_by_price(computers, reverse=(order == "2"))
                print("\n--- Отсортированные компьютеры ---")
                for comp in sorted_list:
                    print(comp)

            case "5":
                expensive = operations.find_most_expensive(computers)
                print(f"\nСамый дорогой компьютер: {expensive}")

            case "6":
                try:
                    target = int(input("Какой объем RAM проверить: "))
                    found = operations.check_ram_availability(computers, target)
                    if found:
                        print(f"Да, в наличии есть компьютеры с {target} ГБ RAM.")
                    else:
                        print(f"Нет, компьютеров с {target} ГБ RAM не найдено.")
                except ValueError:
                    print("Ошибка: введите целое число.")

            case "7":
                print("\n--- Запуск генератора (только ноутбуки) ---")
                laptop_gen = computer_type_generator(computers, Laptop)

                try:
                    first = next(laptop_gen)
                    print(f"Первый полученный элемент через next(): {first.name}")
                except StopIteration:
                    print("Ноутбуки не найдены.")

                print("\nОстальные элементы генератора через for:")
                for item in laptop_gen:
                    print(item)

            case "8":
                print("\n--- Работа собственного итератора ---")
                iterator = ComputerIterator(computers)
                print(f"Первый элемент: {next(iterator).name}")
                print(f"Второй элемент: {next(iterator).name}")

                print("\nПроход по оставшимся элементам:")
                for comp in iterator:
                    print(f"-> {comp.name}")

            case "9":
                list_data = [comp.price for comp in computers * 1000]
                gen_data = (comp.price for comp in computers * 1000)

                print("\n--- Сравнение потребления памяти (sys.getsizeof) ---")
                print(f"Размер обычного списка в памяти: {sys.getsizeof(list_data)} байт")
                print(f"Размер генераторного выражения:    {sys.getsizeof(gen_data)} байт")

            case "0":
                print("Выход из программы.")
                break

            case _:
                print("Неизвестный пункт меню.")


if __name__ == "__main__":
    main()