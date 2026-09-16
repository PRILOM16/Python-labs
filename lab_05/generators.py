def computer_type_generator(computers, target_class):
    """Генератор (yield): по одному лениво выдает компьютеры определенного типа (класса)."""
    for comp in computers:
        if isinstance(comp, target_class):
            yield comp


class ComputerIterator:
    """Собственный итератор (раздел 12 методички).

    Реализует протокол итератора: методы __iter__ и __next__.
    """

    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            
            raise StopIteration

        item = self.collection[self.index]
        self.index += 1
        return item