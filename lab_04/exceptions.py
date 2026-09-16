class ComputerStoreError(Exception):
    pass


class ComputerNotFoundError(ComputerStoreError):
    def __init__(self, name: str):
        super().__init__(f"Компьютер с названием '{name}' не найден в каталоге.")
        self.name = name


class ComputerAlreadyExistsError(ComputerStoreError):
    def __init__(self, name: str):
        super().__init__(f"Компьютер с названием '{name}' уже существует в каталоге.")
        self.name = name


class InvalidComputerDataError(ComputerStoreError):
    pass