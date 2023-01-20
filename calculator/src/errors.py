#!/usr/bin/env python3
from enum import Enum


class CalculatorError(Enum):
    INVALID_DAY = "Invalid day, please use the abbreviation of the day."
    INVALID_TIME_FORMAT = "Invalid time format, please use the format HH:MM-HH:MM."
    INVALID_LINE_FORMAT = "Invalid format, please use the format EMPLOYEE_NAME=MO10:00-12:00,TU10:00-12:00,..."
    INVALID_FILE_TYPE = "Invalid file type, only .txt files are allowed."

    def __str__(self):
        return f"{self.value}"
