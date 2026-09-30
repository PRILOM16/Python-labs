class ClinicContext:
    def __enter__(self):
        print(">>> Открытие системы клиники...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f">>> Произошла ошибка: {exc_val}")
        print(">>> Закрытие системы клиники...\n")