class Computer:
    """Базовый класс компьютера."""

    def __init__(self, name, cpu, ram, storage, price):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.price = price

    def get_info(self):
        return f"ПК '{self.name}' | CPU: {self.cpu} | RAM: {self.ram} ГБ | Диск: {self.storage} | Цена: {self.price} руб."

    def __str__(self):
        return self.get_info()

    @staticmethod
    def from_dict(data):
        """Создает DesktopComputer или Laptop в зависимости от поля 'type'."""
        comp_type = data.get("type")
        if comp_type == "desktop":
            return DesktopComputer(
                name=data["name"],
                cpu=data["cpu"],
                ram=data["ram"],
                storage=data["storage"],
                price=data["price"],
                form_factor=data.get("form_factor", "ATX")
            )
        elif comp_type == "laptop":
            return Laptop(
                name=data["name"],
                cpu=data["cpu"],
                ram=data["ram"],
                storage=data["storage"],
                price=data["price"],
                screen_size=data.get("screen_size", 15.6)
            )
        else:
            return Computer(
                name=data["name"],
                cpu=data["cpu"],
                ram=data["ram"],
                storage=data["storage"],
                price=data["price"]
            )


class DesktopComputer(Computer):

    def __init__(self, name, cpu, ram, storage, price, form_factor="ATX"):
        super().__init__(name, cpu, ram, storage, price)
        self.form_factor = form_factor

    def get_info(self):
        base_info = super().get_info()
        return f"[Desktop] {base_info} | Корпус: {self.form_factor}"


class Laptop(Computer):

    def __init__(self, name, cpu, ram, storage, price, screen_size=15.6):
        super().__init__(name, cpu, ram, storage, price)
        self.screen_size = screen_size

    def get_info(self):
        base_info = super().get_info()
        return f"[Laptop]  {base_info} | Экран: {self.screen_size}\""