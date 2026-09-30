from typing import List
from models import Patient, Doctor, Appointment, Status
from interfaces import Repository, Notifier
from exceptions import EntityNotFoundError

class ClinicService:
    def __init__(self, patient_repo: Repository, appointment_repo: Repository, notifier: Notifier):
        self.patient_repo = patient_repo
        self.appointment_repo = appointment_repo
        self.notifier = notifier

    def add_patient(self, patient: Patient) -> None:
        self.patient_repo.add(patient)
        self.notifier.send(f"Зарегистрирован новый пациент: {patient.name}")

    def add_appointment(self, appointment: Appointment) -> None:
        self.appointment_repo.add(appointment)
        self.notifier.send(f"Создан прием №{appointment.id}")

    def find_appointment(self, app_id: int) -> Appointment:
        app = self.appointment_repo.get_by_id(app_id)
        if not app:
            raise EntityNotFoundError(f"Прием с ID {app_id} не найден.")
        return app

    def confirm_appointment(self, app_id: int) -> None:
        app = self.find_appointment(app_id)
        app.status = Status.CONFIRMED
        self.notifier.send(f"Прием №{app_id} подтвержден.")

    # Специализированные операции
    def count_doctor_appointments(self, doc_id: int) -> int:
        all_apps = self.appointment_repo.get_all()
        return sum(1 for app in all_apps if app.doctor.id == doc_id)

    def avg_duration(self) -> float:
        all_apps = self.appointment_repo.get_all()
        if not all_apps:
            return 0.0
        total = sum(app.duration for app in all_apps)
        return total / len(all_apps)

    def get_statistics(self) -> dict:
        all_apps = self.appointment_repo.get_all()
        completed = sum(1 for a in all_apps if a.status == Status.COMPLETED)
        return {
            "Всего приемов": len(all_apps),
            "Завершено": completed,
            "Средняя длительность": self.avg_duration()
        }