from exceptions import ComputerStoreError
from services import ComputerStoreService
import storage

# Имена файлов для хранения данных
DATA_FILE_JSON = "data.json"
DATA_FILE_CSV = "data.csv"


def main():
    service = ComputerStoreService()

    service.computers = storage.load_json(DATA_FILE_JSON)
    print(f"Загружено конфигураций из файла: {len(service.computers)}")

    while True:
        print("\n===== МЕНЮ: КОМПЬЮТЕРНЫЙ МАГАЗИН =====")
        print("1. Показать все конфигурации")
        print("2. Добавить новый компьютер")
        print("3. Найти компьютер по названию")
        print("4. Изменить конфигурацию (цену/RAM)")
        print("5. Фильтровать по объему RAM")
        print("6. Сортировать по цене")
        print("7. Экспортировать данные в CSV")
        print("0. Сохранить и выйти")

        choice = input("Выберите пункт меню: ").strip()

        match choice:
            case "1":
                computers = service.get_all()
                if not computers:
                    print("Каталог пуст.")
                else:
                    print("\n--- Список компьютеров ---")
                    for comp in computers:
                        print(comp)

            case "2":
                try:
                    name = input("Название модели: ").strip()
                    cpu = input("Процессор: ").strip()
                    ram = int(input("Объем RAM (ГБ): "))
                    hdd = input("Накопитель (например, 1TB SSD): ").strip()
                    price = float(input("Цена (руб.): "))

                    service.add_computer(name, cpu, ram, hdd, price)
                    print(f"Компьютер '{name}' успешно добавлен!")

                except ValueError:
                    print("Ошибка: объем RAM и цена должны быть числами!")
                except ComputerStoreError as error:
                    print(f"Ошибка магазина: {error}")

            case "3":
                name = input("Введите название для поиска: ").strip()
                try:
                    comp = service.find_by_name(name)
                    print(f"Найден: {comp}")
                except ComputerStoreError as error:
                    print(f"Ошибка: {error}")

            case "4":
                name = input("Введите название компьютера для изменения: ").strip()
                try:
                    comp = service.find_by_name(name)
                    print(f"Текущая конфигурация: {comp}")

                    new_price_input = input("Новая цена (Enter, чтобы не менять): ").strip()
                    new_ram_input = input("Новый объем RAM (Enter, чтобы не менять): ").strip()

                    new_price = float(new_price_input) if new_price_input else None
                    new_ram = int(new_ram_input) if new_ram_input else None

                    service.update_computer(name, new_price=new_price, new_ram=new_ram)
                    print("Конфигурация успешно обновлена!")

                except ValueError:
                    print("Ошибка: введены некорректные числовые данные!")
                except ComputerStoreError as error:
                    print(f"Ошибка: {error}")

            case "5":
                try:
                    min_ram = int(input("Введите минимальный объем RAM (ГБ): "))
                    filtered = service.filter_by_ram(min_ram)
                    if not filtered:
                        print("Компьютеры с такими параметрами не найдены.")
                    else:
                        print(f"\n--- Компьютеры с RAM >= {min_ram} ГБ ---")
                        for comp in filtered:
                            print(comp)
                except ValueError:
                    print("Ошибка: объем RAM должен быть целым числом!")

            case "6":
                print("1. По возрастанию цены")
                print("2. По убыванию цены")
                sort_order = input("Выберите порядок: ").strip()

                is_reverse = sort_order == "2"
                sorted_list = service.sort_by_price(reverse=is_reverse)

                print("\n--- Отсортированный каталог ---")
                for comp in sorted_list:
                    print(comp)

            case "7":
                try:
                    storage.export_csv(DATA_FILE_CSV, service.get_all())
                    print(f"Данные успешно экспортированы в файл '{DATA_FILE_CSV}'!")
                except Exception as error:
                    print(f"Ошибка при экспорте в CSV: {error}")

            case "0":
                storage.save_json(DATA_FILE_JSON, service.get_all())
                print(f"Данные сохранены в '{DATA_FILE_JSON}'. До свидания!")
                break

            case _:
                print("Неизвестный пункт меню. Пожалуйста, повторите ввод.")


if __name__ == "__main__":
    main()