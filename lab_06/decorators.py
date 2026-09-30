import time
from functools import wraps
from models import Status

def log_call(func):
    """Декоратор 1: Журналирование."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Вызвана функция: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    """Декоратор 2: Замер времени."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"[PERFORMANCE] {func.__name__} выполнена за {t2 - t1:.5f} сек.")
        return result
    return wrapper

def require_status(required_status: Status):
    """Декоратор 3 (с параметром): Проверка статуса."""
    def decorator(func):
        @wraps(func)
        def wrapper(service, app_id: int):
            app = service.find_appointment(app_id)
            if app.status != required_status:
                raise ValueError(f"Недопустимый статус! Ожидается: {required_status.value}")
            return func(service, app_id)
        return wrapper
    return decorator