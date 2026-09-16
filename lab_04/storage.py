import csv
import json
from models import Computer


def load_json(file_path):
    """Загрузка по разделу 2.24 и 9 методички. Если файла нет, возвращаем пустой список."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Десериализация объектов через @classmethod from_dict (раздел 10)
            return [Computer.from_dict(item) for item in data]
    except FileNotFoundError:
        return []


def save_json(file_path, computers):
    """Сохранение объектов в JSON по разделу 2.23 и 10 методички."""
    # Сериализация: преобразуем каждый объект в словарь
    data = [comp.to_dict() for comp in computers]
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def export_csv(file_path, computers):
    """Экспорт данных в формат CSV по разделу 2.19 и 7 методички."""
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Заголовок таблицы
        writer.writerow(["name", "cpu", "ram", "storage", "price"])
        # Запись строк данных
        for comp in computers:
            writer.writerow([comp.name, comp.cpu, comp.ram, comp.storage, comp.price])