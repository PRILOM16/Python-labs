from interfaces import Notifier

class ConsoleNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[УВЕДОМЛЕНИЕ В СИСТЕМУ]: {message}")