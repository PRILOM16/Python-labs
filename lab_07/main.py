from repository import InMemoryRepository
from notifier import ConsoleNotifier
from services import ClinicService
from ui import ConsoleUI

def main():

    patient_repo = InMemoryRepository()
    appointment_repo = InMemoryRepository()
    notifier = ConsoleNotifier()

    service = ClinicService(
        patient_repo=patient_repo,
        appointment_repo=appointment_repo,
        notifier=notifier
    )
    
    ui = ConsoleUI(service)
    ui.run()

if __name__ == "__main__":
    main()