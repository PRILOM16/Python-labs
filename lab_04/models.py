class Computer:
    def __init__(self, name = str, cpu  = str, ram = int, storage = int, price = float):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.price = price

    @property
    def  ram(self) -> int:
        return self._ram

    @ram.setter
    def  ram(self, value: int):
        if value <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным числом.")
        self._ram = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = value

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "cpu": self.cpu,
            "ram": self.ram,
            "storage": self.storage,
            "price": self.price,
        }

    @classmethod
    def from_dict(cls, data:dict):
       return cls(
            name=data["name"],
            cpu=data["cpu"],
            ram=data["ram"],
            storage=data["storage"],
            price=data["price"],
        ) 


    def __str__(self) -> str:
        return (
            f"ПК '{self.name}' | CPU: {self.cpu} | RAM: {self.ram} ГБ | "
            f"Диск: {self.storage} | Цена: {self.price:,.2f} руб."
        )
