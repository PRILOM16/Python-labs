from models import Patient, Doctor, Appointment, Status
from services import ClinicService
from exceptions import EntityNotFoundError

class ConsoleUI:
    def __init__(self, service: ClinicService):
        self.service = service
        self.test_patient = Patient(1, "Иванов И.И.", "Простуда")
        self.test_doctor = Doctor(1, "Петров П.П.", "Терапевт")
        self._preload()

    def _preload(self):
        self.service.add_patient(self.test_patient)
        self.service.add_appointment(Appointment(1, self.test_patient, self.test_doctor, 30))

    def run(self):
        while True:
            print("\n=== МЕНЮ КЛИНИКИ (SOLID) ===")
            print("1. Добавить прием")
            print("2. Найти прием")
            print("3. Подтвердить прием")
            print("4. Показать все приемы")
            print("5. Приемы врача (спец. операция 1)")
            print("6. Статистика (спец. операция 2)")
            print("0. Выход")
            
            choice = input("Выберите пункт: ")

            try:
                if choice == "1":
                    a_id = int(input("ID приема: "))
                    dur = int(input("Длительность (мин): "))
                    self.service.add_appointment(Appointment(a_id, self.test_patient, self.test_doctor, dur))
                    print("Прием добавлен.")

                elif choice == "2":
                    a_id = int(input("ID приема: "))
                    app = self.service.find_appointment(a_id)
                    print(f"Найден: {app.patient.name} у {app.doctor.name} [{app.status.value}]")

                elif choice == "3":
                    a_id = int(input("ID приема для подтверждения: "))
                    self.service.confirm_appointment(a_id)
                    print("Статус изменен.")

                elif choice == "4":
                    for a in self.service.appointment_repo.get_all():
                        print(f"[{a.id}] {a.patient.name} -> {a.doctor.name} ({a.status.value})")

                elif choice == "5":
                    doc_id = int(input("ID врача (тестовый = 1): "))
                    print("Количество приемов:", self.service.count_doctor_appointments(doc_id))

                elif choice == "6":
                    for k, v in self.service.get_statistics().items():
                        print(f"{k}: {v}")

                elif choice == "0":
                    break
                else:
                    print("Неверный ввод.")

            except EntityNotFoundError as e:
                print(f"[ОШИБКА ДАННЫХ]: {e}")
            except ValueError as e:
                print(f"[ОШИБКА ВВОДА]: {e}")