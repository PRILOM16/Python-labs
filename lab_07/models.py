from dataclasses import dataclass
from enum import Enum

class Status(Enum):
    PLANNED = "запланирован"
    CONFIRMED = "подтверждён"
    COMPLETED = "завершён"
    CANCELLED = "отменен"

@dataclass
class Entity:
    id: int
    name: str

@dataclass
class Patient(Entity):
    diagnosis: str

@dataclass
class Doctor(Entity):
    specialization: str

@dataclass
class Appointment:
    id: int
    patient: Patient
    doctor: Doctor
    duration: int  
    status: Status = Status.PLANNED