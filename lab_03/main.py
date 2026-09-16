class Server:
    def __init__(self, name, ip, ram):
        self.name = name
        self.ip = ip
        self.ram = ram  
        self.is_active = True

    @property
    def ram(self):
        return  self._ram

    @ram.setter
    def ram(self, value):
        if value <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным")
        self._ram = value

    def start(self):
        self.is_active = True

    def stop(self):
        self.is_active = False

    def get_load(self):
        return 0.0

    def __str__(self):
        status = "В сети" if self.is_active else "Отключен"
        return f"Сервер {self.name} ({self.ip}), RAM: {self.ram} ГБ, статус: {status}"

class WebServer(Server):
    def __init__(self, name, ip, ram, requests_per_sec, max_rps = 1000):
        super().__init__(name, ip, ram)
        self.requests_per_sec = requests_per_sec
        self.max_rps = max_rps

    def get_load(self):
        if not self.is_active:
            return 0.0
        load = (self.requests_per_sec / self.max_rps) * 100
        return min(100.0, round(load, 2))

    def __str__(self):
        base_info = super().__str__()
        return f"[WEB] {base_info} | Нагрузка RPS: {self.requests_per_sec}/{self.max_rps} ({self.get_load()}%)"

class DatabaseServer(Server):

    def __init__(self, name, ip, ram, connections, max_connections=200):
        super().__init__(name, ip, ram)
        self.connections = connections
        self.max_connections = max_connections

    def get_load(self):
        if not self.is_active:
            return 0.0
        load = (self.connections / self.max_connections) * 100
        return min(100.0, round(load, 2))

    def __str__(self):
        base_info = super().__str__()
        return f"[DB]  {base_info} | Подключения: {self.connections}/{self.max_connections} ({self.get_load()}%)"


class DataCenter:

    def __init__(self, location: str):
        self.location = location
        self.servers = []

    def add_server(self, server: Server):
        self.servers.append(server)
        print(f"Сервер '{server.name}' успешно добавлен в {self.location}.")

    def remove_server(self, name: str) -> bool:
        for srv in self.servers:
            if srv.name == name:
                self.servers.remove(srv)
                print(f"Сервер '{name}' удален.")
                return True
        print(f"Сервер с именем '{name}' не найден.")
        return False

    def show_all_servers(self):
        if not self.servers:
            print("В дата-центре пока нет серверов.")
            return

        print(f"\n--- Список серверов ({self.location}) ---")
        for srv in self.servers:
            print(srv)

    def get_average_load(self) -> float:
        if not self.servers:
            return 0.0

        total_load = sum(srv.get_load() for srv in self.servers)
        return round(total_load / len(self.servers), 2)    
    

def main():
    dc = DataCenter("DC-North")

    while True:
        print("\n===== МЕНЮ ДАТА-ЦЕНТРА =====")
        print("1. Добавить сервер")
        print("2. Показать список серверов")
        print("3. Рассчитать общую нагрузку (полиморфизм)")
        print("4. Изменить нагрузку сервера")
        print("5. Удалить сервер")
        print("0. Выход")

        choice = input("Выберите действие (0-5): ").strip()

        match choice:
            case "1":
                print("\nТип сервера:")
                print("1. Web-сервер")
                print("2. Сервер баз данных")
                type_choice = input("Выберите тип: ").strip()

                name = input("Имя сервера: ").strip()
                ip = input("IP-адрес: ").strip()

                try:
                    ram = int(input("Объем RAM (ГБ): "))

                    match type_choice:
                        case "1":
                            rps = int(input("Текущий RPS (запросов/сек): "))
                            max_rps = int(
                                input("Максимальный RPS (по умолчанию 1000): ")
                                or 1000
                            )
                            server = WebServer(name, ip, ram, rps, max_rps)
                            dc.add_server(server)

                        case "2":
                            conns = int(input("Текущие подключения: "))
                            max_conns = int(
                                input(
                                    "Максимум подключений (по умолчанию 200): "
                                )
                                or 200
                            )
                            server = DatabaseServer(
                                name, ip, ram, conns, max_conns
                            )
                            dc.add_server(server)

                        case _:
                            print("Неверный тип сервера.")

                except ValueError as e:
                    print(f"Ошибка ввода данных: {e}")

            case "2":
                dc.show_all_servers()

            case "3":
                print(
                    f"\nСредняя загрузка мощностей {dc.location}: {dc.get_average_load()}%"
                )

            case "4":
                name = input("Введите имя сервера для обновления: ").strip()
                target = next((s for s in dc.servers if s.name == name), None)

                if not target:
                    print("Сервер не найден.")
                    continue

                try:
                    match target:
                        case WebServer():
                            new_rps = int(
                                input(
                                    f"Новый RPS (текущий {target.requests_per_sec}): "
                                )
                            )
                            target.requests_per_sec = new_rps
                            print("Метрики Web-сервера обновлены.")

                        case DatabaseServer():
                            new_conns = int(
                                input(
                                    f"Новое число подключений (текущее {target.connections}): "
                                )
                            )
                            target.connections = new_conns
                            print("Метрики DB-сервера обновлены.")

                except ValueError as e:
                    print(f"Ошибка ввода: {e}")

            case "5":
                name = input("Введите имя сервера для удаления: ").strip()
                dc.remove_server(name)

            case "0":
                print("Работа программы завершена.")
                break

            case _:
                print("Некорректный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main()