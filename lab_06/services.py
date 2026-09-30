from typing import List
from models import Patient, Doctor, Appointment, Status
from exceptions import EntityNotFoundError
from decorators import log_call, measure_time, require_status

class ClinicService:
    def __init__(self):
        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []
        self.appointments: List[Appointment] = []

    # Реализация протокола Reportable
    def get_report_data(self) -> str:
        return f"Отчет: пациентов {len(self.patients)}, приемов {len(self.appointments)}"

    @log_call
    def add_patient(self, p: Patient) -> None:
        self.patients.append(p)

    @log_call
    def add_doctor(self, d: Doctor) -> None:
        self.doctors.append(d)

    @log_call
    def add_appointment(self, app: Appointment) -> None:
        self.appointments.append(app)

    def find_appointment(self, app_id: int) -> Appointment:
        for app in self.appointments:
            if app.id == app_id:
                return app
        raise EntityNotFoundError(f"Прием с ID {app_id} не найден.")

    @require_status(Status.PLANNED)
    def confirm_appointment(self, app_id: int) -> None:
        app = self.find_appointment(app_id)
        app.status = Status.CONFIRMED

    #операция 1: подсчет приемов врача
    @measure_time
    def count_doctor_appointments(self, doc_id: int) -> int:
        return sum(1 for app in self.appointments if app.doctor.id == doc_id)

    #операция 2: средняя продолжительность приема
    @measure_time
    def avg_duration(self) -> float:
        if not self.appointments:
            return 0.0
        total = sum(app.duration for app in self.appointments)
        return total / len(self.appointments)

    def get_statistics(self) -> dict:
        completed = len([a for a in self.appointments if a.status == Status.COMPLETED])
        return {
            "Всего приемов": len(self.appointments),
            "Завершено": completed,
            "Средняя длительность": self.avg_duration()
        }


def inspect_object(obj):
    """Функция интроспекции."""
    print("\n--- ИНТРОСПЕКЦИЯ ---")
    print("1. Тип (type):", type(obj))
    print("2. Является ли пациентом (isinstance):", isinstance(obj, Patient))
    print("3. Атрибуты (dir):", dir(obj))
    print("4. Есть ли атрибут 'name' (hasattr):", hasattr(obj, 'name'))
    print("--------------------\n")