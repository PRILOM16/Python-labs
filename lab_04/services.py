from exceptions import ComputerAlreadyExistsError, ComputerNotFoundError
from models import Computer


class ComputerStoreService:

    def __init__(self):
        self.computers = []

    def get_all(self):
        return self.computers

    def add_computer(self, name, cpu, ram, storage, price):
        for comp in self.computers:
            if comp.name.lower() == name.lower():
                raise ComputerAlreadyExistsError(name)

        new_computer = Computer(name, cpu, ram, storage, price)
        self.computers.append(new_computer)
        return new_computer

    def find_by_name(self, name):
        for comp in self.computers:
            if comp.name.lower() == name.lower():
                return comp
        raise ComputerNotFoundError(name)

    def update_computer(self, name, new_price=None, new_ram=None):
        comp = self.find_by_name(name)

        if new_price is not None:
            comp.price = new_price 
        if new_ram is not None:
            comp.ram = new_ram 

        return comp

    def filter_by_ram(self, min_ram):
        result = []
        for comp in self.computers:
            if comp.ram >= min_ram:
                result.append(comp)
        return result

    def sort_by_price(self, reverse=False):
        return sorted(self.computers, key=lambda comp: comp.price, reverse=reverse)