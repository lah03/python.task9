# Python Error Handling and Logging Demo

This project demonstrates Python **exception handling**, including multiple exceptions, custom errors, and logging to a file.

## File Included

- `error_handling.py` – Python script demonstrating try-except blocks, else & finally, custom exceptions, and logging
- `error_log.txt` – Log file automatically generated to store error messages

## Features Demonstrated

1. Using **try-except** blocks to catch exceptions
2. Handling **multiple exceptions** (ZeroDivisionError, TypeError, IOError, etc.)
3. Using **else** and **finally** blocks
4. Logging errors using the **logging module**
5. Saving logs to a file (`error_log.txt`)
6. Creating **custom exceptions** (`NegativeValueError`)
7. Simulating runtime errors (division by zero, type mismatch, negative values)
8. Clean and readable error messages for users

## Concepts Covered

- Exception handling: `try`, `except`, `else`, `finally`
- Logging: `logging.basicConfig()`, `logging.error()`
- Custom exceptions: creating a subclass of `Exception`
- File handling with exception safety

## How to Run

Ensure Python 3 is installed.

```bash
python error_handling.py
