from generators import computer_type_generator
from models import DesktopComputer, Laptop, Computer
import operations
import os
import json


def get_initial_data():
    """Загружает список компьютеров из файла computers_init.json в текущей папке."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "computers_init.json")

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            raw_data = json.load(file)
            # Преобразуем словари из JSON в объекты классов
            return [Computer.from_dict(item) for item in raw_data]
    except FileNotFoundError:
        print(f"Внимание: Файл '{json_path}' не найден. Каталог будет пуст.")
        return []
    except json.JSONDecodeError:
        print(f"Внимание: Ошибка чтения JSON в файле '{json_path}'. Каталог будет пуст.")
        return []


def main():
    computers = get_initial_data()

    while True:
        print("\n===== ЛАБОРАТОРНАЯ 5: КОМПЬЮТЕРЫ =====")
        print("1. Показать все компьютеры")
        print("2. Получить список названий")
        print("3. Отфильтровать по объему RAM")
        print("4. Отсортировать по цене")
        print("5. Найти самый дорогой компьютер")
        print("6. Проверить наличие ПК с заданным RAM")
        print("7. Запустить генераторы по типам устройств")
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
                print("\n--- Генератор стационарных ПК (DesktopComputer) ---")
                desktop_gen = computer_type_generator(computers, DesktopComputer)
                for item in desktop_gen:
                    print(item.name)

                print("\n--- Генератор ноутбуков (Laptop) ---")
                laptop_gen = computer_type_generator(computers, Laptop)
                for item in laptop_gen:
                    print(item.name)

            case "0":
                print("Выход из программы.")
                break

            case _:
                print("Неизвестный пункт меню.")


if __name__ == "__main__":
    main()