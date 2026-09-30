from models import Patient, Doctor, Appointment, Status
from services import ClinicService, inspect_object
from protocols import Reportable
from context import ClinicContext
from exceptions import EntityNotFoundError

class ConsoleUI:
    def __init__(self, service: ClinicService):
        self.service = service
        self.test_patient = Patient(1, "Иванов И.И.", "Простуда")
        self.test_doctor = Doctor(1, "Петров П.П.", "Терапевт")
        self._preload_data()

    def _preload_data(self):
        self.service.add_patient(self.test_patient)
        self.service.add_doctor(self.test_doctor)
        self.service.add_appointment(Appointment(1, self.test_patient, self.test_doctor, 30))

    def run(self):
        # Запуск контекстного менеджера для всего сеанса работы интерфейса
        with ClinicContext():
            while True:
                print("\n=== МЕНЮ КЛИНИКИ ===")
                print("1. Добавить прием")
                print("2. Найти прием")
                print("3. Подтвердить прием (сработает декоратор статуса)")
                print("4. Вывести все приемы")
                print("5. Подсчитать приемы врача (спец. операция 1)")
                print("6. Получить статистику (спец. операция 2)")
                print("7. Выполнить интроспекцию пациента")
                print("8. Проверить Protocol")
                print("0. Выход")
                
                choice = input("Выберите пункт: ")

                try:
                    if choice == "1":
                        a_id = int(input("Введите ID приема: "))
                        dur = int(input("Введите длительность (мин): "))
                        # Для простоты используем первого пациента и врача из базы
                        self.service.add_appointment(
                            Appointment(a_id, self.test_patient, self.test_doctor, dur)
                        )
                        print("Прием добавлен.")

                    elif choice == "2":
                        a_id = int(input("Введите ID приема: "))
                        app = self.service.find_appointment(a_id)
                        print(f"Найден: {app.patient.name} к {app.doctor.name}, статус: {app.status.value}")

                    elif choice == "3":
                        a_id = int(input("Введите ID приема (должен быть 'запланирован'): "))
                        self.service.confirm_appointment(a_id)
                        print("Прием подтвержден.")

                    elif choice == "4":
                        for a in self.service.appointments:
                            print(f"[{a.id}] {a.patient.name} - {a.doctor.name} ({a.status.value})")

                    elif choice == "5":
                        doc_id = int(input("Введите ID врача (тестовый врач имеет ID 1): "))
                        print("Приемов у врача:", self.service.count_doctor_appointments(doc_id))

                    elif choice == "6":
                        stats = self.service.get_statistics()
                        for k, v in stats.items():
                            print(f"{k}: {v}")

                    elif choice == "7":
                        inspect_object(self.test_patient)

                    elif choice == "8":
                        if isinstance(self.service, Reportable):
                            print("Сервис поддерживает Protocol! Отчет:")
                            print(self.service.get_report_data())
                        else:
                            print("Protocol не поддерживается.")

                    elif choice == "0":
                        break
                    else:
                        print("Неверный ввод.")

                # Перехват наших собственных и стандартных исключений на уровне интерфейса
                except EntityNotFoundError as e:
                    print(f"[ОШИБКА ДАННЫХ] {e}")
                except ValueError as e:
                    print(f"[ОШИБКА ВВОДА/ЛОГИКИ] {e}")