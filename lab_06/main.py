from services import ClinicService
from ui import ConsoleUI

def main():
    service = ClinicService()
    
    ui = ConsoleUI(service)
    
    ui.run()

if __name__ == "__main__":
    main()