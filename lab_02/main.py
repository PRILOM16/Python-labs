def show_menu(servers_list):
    
    while True:
        print("\n==== МЕНЮ ====")
        print("1. Добавить сервер")
        print("2. Показать все серверы")
        print("3. Найти серверы по назначению")
        print("4. Фильтрация по загрузке CPU")
        print("5. Определение средней загрузки")
        print("6. Поиск наиболее загруженного сервера")
        print("7. Список назначения серверов")
        print("8. Сортировка по загрузке CPU")
        print("0. Выход")

        choice = input("Выберите операцию: ").strip()

        match choice:
            case "1":
                server = add_server()
                servers_list.append(server)
            case "2":
                show_all_servers(servers_list)
            case "3":
                find_servers_by_purpose(servers_list)
            case "4":
                filter_servers_by_cpu(servers_list)
            case "5":
                calculate_average_cpu_load(servers_list)
            case "6":
                find_most_loaded_server(servers_list)
            case "7":
                get_server_purposes(servers_list)
            case "8":
                sort_servers_by_cpu(servers_list)
            case "0":
                print("Программа завершила свою работу")
                break
            case _:
                print("Некорректный ввод!")

# Вспомогательная функция для проверки корректности ввода
def get_valid_number(prompt, num_type=float, min_val=0.0, max_val=float("inf")):
    while True:
        try:
            value = num_type(input(prompt))
            if not (min_val <= value <= max_val):
                if max_val == float("inf"):
                    print(f"Ошибка! Значение должно быть не меньше {min_val}.")
                else:
                    print(f"Ошибка! Значение должно быть в диапазоне от {min_val} до {max_val}.")
                continue
            return value
        except ValueError:
            print("Ошибка! Введено некорректное число.")
    
def add_server():
        print("\n--- Добавление нового сервера ---")
        name = input("введите название сервера: ").strip()
        ip = input("Введите IP-адрес: ").strip()
        purpose = input("Введите назначение (Web, DB и т.д.): ").strip()
        ram = get_valid_number("Введите объем RAM (ГБ): ", num_type=int, min_val=1)
        cpu = get_valid_number("Введите загрузку CPU (%): ", num_type=float, min_val=0.0, max_val=100.0)

        return {
            "name": name,
            "ip": ip,
            "purpose": purpose,
            "ram": ram,
            "cpu": cpu,
        }

def show_all_servers(servers):
    if not servers:
        print("\nСписок серверов пуст.")
        return
    print("Список серверов:")
    print("\n" + "=" * 40)
    for idx, server in enumerate(servers, start = 1):
        print(f"Сервер №{idx}, название: {server['name']}") 

def find_servers_by_purpose(servers):
    user_purpose = input("Введите назначение сервера: ").strip().lower()
    purpose_servers = [s["name"] for s in servers if s["purpose"].lower() == user_purpose]

    if purpose_servers:
        print(f"Найденные серверы: {', '.join(purpose_servers)}")
    else:
        print("Серверы с таким назначением не найдены.")

def print_filtered_result(filtered_servers):
    """Вывод результатов фильтрации."""
    if not filtered_servers:
        print("\nСерверы по заданному критерию не найдены.")
        return

    print(f"\nНайдено серверов: {len(filtered_servers)}")
    for idx, s in enumerate(filtered_servers, start=1):
        print(f"  {idx}. {s['name']} (IP: {s['ip']}) | Роль: {s['purpose']} | RAM: {s['ram']} ГБ | CPU: {s['cpu']:.1f}%")

def filter_servers_by_cpu(servers):
    if not servers:
        print("Список серверов пуст.")
        return

    
    while True:
        print("\n==== МЕНЮ ФИЛЬТРАЦИИ ====") 
        print("1. Фильтрация по минимальному значению")
        print("2. Фильтрация по максимальному значению")
        print("3. Фильтрация по минимальному и максимальному значению")
        print("4. Назад")

        choice = input("Выберите режим фильтрации:").strip()

        match choice:
            case "1":
                min_cpu = get_valid_number("Введите минимальную загрузку CPU (%): ", min_val=0.0, max_val=100.0)
                result = [s for s in servers if s["cpu"] >= min_cpu]
                print_filtered_result(result)

            case "2":
                max_cpu = get_valid_number("Введите максимальную загрузку CPU (%): ", min_val=0.0, max_val=100.0)
                result = [s for s in servers if s["cpu"] <= max_cpu]
                print_filtered_result(result)
            case "3":
                while True:
                    min_cpu = get_valid_number("Введите минимальную загрузку CPU (%): ", min_val=0.0, max_val=100.0)
                    max_cpu = get_valid_number("Введите максимальную загрузку CPU (%): ", min_val=0.0, max_val=100.0)

                    if min_cpu > max_cpu:
                        print("Ошибка: минимальное значение не может быть больше максимального!")
                        continue
                    break
                result = [s for s in servers if min_cpu <= s["cpu"] <= max_cpu]
                print_filtered_result(result)
            
            case "4":
                print("Возврат")
                break
            case _:
                print("Некорректный ввод!")
    return


def calculate_average_cpu_load(servers):
    if not servers:
        print("\nСписок серверов пуст.")
        return
    
    average = sum(s["cpu"] for s in servers)/ len(servers)
    print (f"Средняя загрузка по всем серверам составляет: {average:.1f}%")

def find_most_loaded_server(servers):
    if not servers:
        print("\nСписок серверов пуст.")
        return
    
    most_loaded = max(servers, key=lambda s: s["cpu"])
    print(f"{most_loaded['name']} — CPU: {most_loaded['cpu']:.1f}%")

def get_server_purposes(servers):
    if not servers:
            print("\nСписок серверов пуст.")
            return
    
    all_purposes = set(s["purpose"] for s in servers)

    print("\n--- Список уникальных назначений серверов ---")
    for target in all_purposes:
        print(f"• {target}")

def sort_servers_by_cpu(servers):
    sorted_servers = sorted(servers, key=lambda s: s["cpu"], reverse=True)

    print("\n--- Серверы по загрузке CPU ---")
    for idx, server in enumerate(sorted_servers, start=1):
        print(f"{idx}. {server['name']} — CPU: {server['cpu']:.1f}%")

def main():
    servers = [
        {"name": "srv-web-01", "ip": "192.168.1.10", "purpose": "Web", "ram": 16, "cpu": 45.5},
        {"name": "srv-db-main", "ip": "192.168.1.20", "purpose": "Database", "ram": 64, "cpu": 88.2},
        {"name": "srv-proxy", "ip": "192.168.1.30", "purpose": "Web", "ram": 8, "cpu": 12.0},
    ]
    show_menu(servers)

if __name__ == "__main__":
    main()