#!/usr/bin/env python3

import unittest
import os

import calculator.src.main as calculator


class TestPayCalculator(unittest.TestCase):
    def setUp(self):
        # make sure the state is defined at test start
        calculator.raise_exception = True

    def test_read_employee_schedules_exceptions(self):
        # Test case for file not found
        with self.assertRaises(FileNotFoundError):
            calculator.read_employee_schedules("non_existent_file.txt")

        # Test case for invalid format
        with open("invalid_format.txt", "w") as f:
            f.write("INVALID_FORMAT")
        with self.assertRaises(ValueError):
            calculator.read_employee_schedules("invalid_format.txt")
        os.remove("invalid_format.txt")

        # Test invalid extensionm
        with self.assertRaises(ValueError):
            calculator.read_employee_schedules("employee_schedules.csv")

        # Test case for valid input
        schedule1 = (
            "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        )
        schedule2 = "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
        with open("valid_input.txt", "w") as f:
            f.write("RENE=" + schedule1 + "\n")
            f.write("ASTRID=" + schedule2 + "\n")
        calculator.read_employee_schedules("valid_input.txt")
        os.remove("valid_input.txt")

    def test_calculate_pay_exceptions(self):
        # Test case for invalid day
        schedule = ["XO10:00-12:00", "TH12:00-14:00", "SU20:00-21:00"]
        with self.assertRaises(KeyError):
            calculator.calculate_pay(schedule)

        # Test case for invalid time format HH:MM:SS
        schedule = ["MO10:00-12:00", "TH12:00-14:00", "SU20:00-21:00:00"]
        with self.assertRaises(ValueError):
            calculator.calculate_pay(schedule)

        # Test case for invalid time format without - sepparator
        schedule = ["MO10:0012:00", "WE12:0014:00", "FR16:0018:00"]
        with self.assertRaises(ValueError):
            calculator.calculate_pay(schedule)

        # Test case for valid input
        schedule1 = [
            "MO10:00-12:00",
            "TU10:00-12:00",
            "TH01:00-03:00",
            "SA14:00-18:00",
            "SU20:00-21:00",
        ]
        schedule2 = ["MO10:00-12:00", "TH12:00-14:00", "SU20:00-21:00"]
        self.assertEqual(calculator.calculate_pay(schedule1), 215)
        self.assertEqual(calculator.calculate_pay(schedule2), 85)

    def test_calculate_pay(self):
        # Test cases for valid imputs
        schedule1 = [
            "MO10:00-12:00",
            "TU10:00-12:00",
            "TH01:00-03:00",
            "SA14:00-18:00",
            "SU20:00-21:00",
        ]
        schedule2 = ["MO10:00-12:00", "TH12:00-14:00", "SU20:00-21:00"]
        schedule3 = ["MO10:00-12:00", "WE12:00-14:00", "FR16:00-18:00"]
        schedule4 = ["MO09:00-12:00", "WE18:00-20:00", "FR09:00-12:00"]
        schedule5 = [
            "TU09:00-12:00",
            "TH09:00-12:00",
            "FR09:00-12:00",
            "SA09:00-12:00",
            "SU09:00-12:00",
        ]

        self.assertEqual(calculator.calculate_pay(schedule1), 215)
        self.assertEqual(calculator.calculate_pay(schedule2), 85)
        self.assertEqual(calculator.calculate_pay(schedule3), 90)
        self.assertEqual(calculator.calculate_pay(schedule4), 130)
        self.assertEqual(calculator.calculate_pay(schedule5), 255)

    def test_process_employee_by_line(self):
        # Test case of line information with bad format
        schedule_line = "RENE=MO10:00-12"

        with self.assertRaises(ValueError):
            calculator.process_employee(line=schedule_line)

        # Test case for valid input
        schedule_line = (
            "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        )
        pay = calculator.process_employee(line=schedule_line, return_value=True)
        self.assertEqual(pay, 215)


if __name__ == "__main__":
    unittest.main()
