import csv
import json
from models import Computer


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            return [Computer.from_dict(item) for item in data]
    except FileNotFoundError:
        return []


def save_json(file_path, computers):
    data = [comp.to_dict() for comp in computers]
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def export_csv(file_path, computers):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Заголовок таблицы
        writer.writerow(["name", "cpu", "ram", "storage", "price"])
        for comp in computers:
            writer.writerow([comp.name, comp.cpu, comp.ram, comp.storage, comp.price])