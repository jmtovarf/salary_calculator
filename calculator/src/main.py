#!/usr/bin/env python3

from datetime import datetime
import logging

from calculator.src.errors import CalculatorError

raise_exception = False

logging.basicConfig(
    format="%(asctime)s (%(levelname)s) %(message)s", level=logging.DEBUG
)

# Define payment structure
pay_schedule = {
    "MO": {"00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20},
    "TU": {"00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20},
    "WE": {"00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20},
    "TH": {"00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20},
    "FR": {"00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20},
    "SA": {"00:01-09:00": 30, "09:01-18:00": 20, "18:01-00:00": 25},
    "SU": {"00:01-09:00": 30, "09:01-18:00": 20, "18:01-00:00": 25},
}


def calculate_pay(schedule: list) -> float:
    """Calculate the payment value based on the list of days worked

    Args:
        schedule: List of days with the hours worked by the employee
    Returns:
        float Value to pay
    """
    try:
        total_pay = 0
        for shift in schedule:
            # Split the time information (MO)(09:00-12:00)
            day = shift[:2]
            time = shift[2:]
            if "-" not in time:
                raise ValueError

            start_time = datetime.strptime(time[:5], "%H:%M")
            end_time = datetime.strptime(time[6:], "%H:%M")
            start = datetime.combine(datetime.now(), start_time.time())
            end = datetime.combine(datetime.now(), end_time.time())
            # Total hours worked in the range of time
            duration = (end - start).total_seconds() / 3600

            # Validate times in the range
            if start_time.hour < 9 and end_time.hour <= 9:
                total_pay += pay_schedule[day]["00:01-09:00"] * duration
            elif start_time.hour < 18 and end_time.hour <= 18:
                total_pay += pay_schedule[day]["09:01-18:00"] * duration
            else:
                total_pay += pay_schedule[day]["18:01-00:00"] * duration
        return total_pay
    except KeyError as e:
        if raise_exception:
            raise e
        logging.error(CalculatorError.INVALID_DAY)
    except ValueError as e:
        if raise_exception:
            raise e
        logging.error(CalculatorError.INVALID_TIME_FORMAT)


def process_employee(line: str, return_value: bool = False) -> None:
    """Process the employee worked time information one by one

    Args:
        line: line read from file with the days and hours worked by employee
        return_value: Defines if the function wants to return the value once it is called (Currently on testing mode)
    Returns:
        float payment value
    """
    try:
        employee_name, schedule = line.strip().split("=")
        logging.debug(f"Calculating {employee_name} salary ...")
        schedule = schedule.split(",")
        pay = calculate_pay(schedule)
        if pay:
            logging.info(f"The amount to pay {employee_name} is: {pay} USD")
        return pay if return_value else None
    except ValueError as e:
        if raise_exception:
            raise e
        logging.error(CalculatorError.INVALID_LINE_FORMAT)


def read_employee_schedules(file_path: str) -> None:
    """Read the txt file from a path where the employees information is located

    Args:
        file_path: Path of file
    Returns:
        None
    """

    # Validate file with acepted exten
    if file_path.endswith(".txt"):
        # Read the file provided
        try:
            with open(file_path) as f:
                for line in f:
                    process_employee(line=line)
        except FileNotFoundError as e:
            if raise_exception:
                raise e
            logging.error(f"File {file_path} not found.")
        except ValueError as e:
            if raise_exception:
                raise e
            logging.error(CalculatorError.INVALID_LINE_FORMAT)
    else:
        if raise_exception:
            raise ValueError

        logging.error(CalculatorError.INVALID_FILE_TYPE)


if __name__ == "__main__":
    read_employee_schedules("data/employee_schedules.txt")
