======================
ACME Salary Calculator
======================
Basic functions created in python to process a ``.txt`` file with a specific format used to calculates the 
salary information for company employees.


Overview
========
This module offers a solution to calculate the salary for employees based on a list of payments in time ranges, 
once the employee add the hours by each day worked, the module checks the total of hours and the pay that the
company defines in order to sum the total. 

As a ``.txt`` is created with the information of all the employees, the module has the hability to process it 
and read that information, also mostly if the possible error cases are being handled in order to fix the file if
is necessary.

A ``cli`` is exposed to users in order to set the file path with the information or include directly the user 
data instead to read a file, this helps users to run the project without modifying the code or process a lot data.


Technology
==========
This project uses native libraries and modules from python 3.9, also creates a module that can be installed
locally or uploaded to `PyPy`_ repositories,


Functions
=========
The project exposes the following functions in general:

*calculate_pay*:
    This function calculates the total of the payment by employee based in all the days worked, taking in count the time ranges and
    intervals of hours.

*process_employee*:
    This function takes the name of the employee and the working information to calculate the payment.

*read_employee_schedules*:
    This function reads a file and map its information in order to process it.


Creating the environment
========================
This project could be running into a new development environment using PyEnv, this avoid a mix with other python versions or dependencies
that project will never use.

The installation depends on the OS, so you need to check the `PyEnv`_ documentation to make the installation.

Once we have ``Pyenv`` installed we are ready to create our environment with the prefered python version and env name:

.. code-block:: console
    $ pyenv virtualenv 3.9.0 acme

Now that the environment is created we can initalizate it and start to work with the project.

.. code-block:: console
    $ pyenv activate acme


Using the service
=================
This repository contains a simple CLI that can call a local
version of the module, but initially we can run the module using the python command.

.. code-block:: console

    # Call the service with defined file in .data/employee_schedules.txt
    $ python calculator/src/main.py

This file contains some sample data for testing with a defined format.


Installation
============
The application is a python module (you will need python3) that can be installed, so install is straightforward
after cloning the repository:

.. code-block:: console
    # Installing via pip
    $ pip install -e .

You can make sure the installation was OK checking the version of the module using (``calculator --version``)


Running the module locally
==========================
Running the module is similar to running the simple command line but requires more options to be set:

.. code-block:: console

    $ calculator process --filename=$FILEPATH --employee-schedules=$EMPLOYEE_INFO

The above command line options are described in the command usage help (``calculator --help``).


Functionality
=============
*Process*:
    .. code-block:: console

        $ calculator process

    Using the CLI we can process the default employees file with this past command, it is a cli option similar to use:

    .. code-block:: console

        $ python calculator/src/main.py

    The result will be the output in console of the employees included in the default file
    ``.data/employee_schedules.txt`` and the amount to pay each one.

*Process By File*:
    .. code-block:: console

        $ calculator process --filename data/employee.txt

    Users can past a specific file with the employees information, all functionality is applied as the default file
    and the amount to pay can be calculated based on new data.

*Process By Line*
    .. code-block:: console

        $ calculator process --employee-schedules RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

    This module also allows users to past specific data from one employee in order to make sure the value to pay is correct
    or just wants to streamline the process.


Development
===========
When developing, it might be more convenient to install using the `develop` mode from
setuptools, this will create symlinks to the site-packages so you can keep changing the
code while being able to call the script entrypoints.

.. code-block:: console

    $ pip install -e .


Unit testing
------------
The project has many unittests available. The main point of the unittests is to provide a
way of checking the software integrity when new changes are introduced. Please keep the tests 
updated and write more tests for new components and when patching bugs. You can run the tests by issuing:

.. code-block:: console

    $ python -m unittest


Reporting bugs
--------------
If you find a bug please report it via GitHub and assign it to one of the 
project owners below. If you can, please write a unittest that validates the bug and
do a PR, this make things faster :-)

Who currently supports this project ? 
=====================================

* Jhon Tovar <jmtovarf@gmail.com>

.. _PyPy: https://pypi.org/
.. _PyEnv: https://github.com/pyenv/pyenv/blob/master/README.md
