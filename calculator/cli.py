#!/usr/bin/env python3

"""
Command line::
calculator -- Runs function to calculate salaries based on arguments provided by cli

Usage:
    calculator process 
        [--filename=PATH]
        [--employee-schedules=VAL]...


Options:
    --filename=PATH                         A txt file path with the set of employees data related to their schedules 
                                            [default: data/employee_schedules.txt]
    --employee-schedules=VAL                The line with the employee information to be processed independently
                                            i.e LUCY=MO09:00-12:00,WE18:00-20:00,FR09:00-12:00.
    --version                               Show version.

Help:
    For help using this module, please open an issue on the repository:
    https://github.com/jmtovarf/salary_calculator
"""

import argparse
import logging
from calculator import __about__
from calculator.src.main import process_employee, read_employee_schedules

logging.basicConfig(
    format="%(asctime)s (%(levelname)s) %(message)s", level=logging.DEBUG
)


parser = argparse.ArgumentParser()
parser.add_argument(
    "process",
    help="Runs function to calculate salaries based on arguments provided by cli",
)
parser.add_argument(
    "--filename",
    "-f",
    type=str,
    help="A txt file path with the set of employees data related to their schedules",
    default="data/employee_schedules.txt",
)

parser.add_argument(
    "--employee-schedules",
    "-es",
    type=str,
    help="The line with the employee information to be processed independently ie LUCY=MO09:00-12:00,WE18:00-20:00,FR09:00-12:00.",
)

parser.add_argument(
    "-v",
    "--version",
    help="Show version",
    action="version",
    version="%(prog)s " + __about__.__version__,
)


def main():
    """Main CLI entrypoint."""

    args = parser.parse_args()

    # Process salary only by cli argument provided
    if args.employee_schedules:
        process_employee(args.employee_schedules)
        return SystemExit()

    # Process salary calculator based on file provided
    read_employee_schedules(args.filename)


if __name__ == "__main__":
    main()
