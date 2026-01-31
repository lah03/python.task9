# error_handling.py

import logging

# 6. Setup logging to save errors to a file
logging.basicConfig(
    filename='error_log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide_numbers(a, b):
    """Function to divide two numbers with error handling."""
    try:
        # 8. Simulate runtime error (ZeroDivisionError)
        result = a / b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero!")
        logging.error("ZeroDivisionError: %s", e)
    except TypeError as e:
        print("Error: Invalid data type! Numbers expected.")
        logging.error("TypeError: %s", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
        logging.error("Exception: %s", e)
    else:
        print(f"Division successful: {a} / {b} = {result}")
    finally:
        print("Execution of divide_numbers() completed.\n")

def read_file(filename):
    """Function to read a file with exception handling."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"File '{filename}' contents:\n{content}")
    except FileNotFoundError as e:
        print(f"Error: File '{filename}' not found!")
        logging.error("FileNotFoundError: %s", e)
    except IOError as e:
        print(f"Error: Could not read file '{filename}'")
        logging.error("IOError: %s", e)
    finally:
        print(f"Attempted to read '{filename}'.\n")

# 7. Custom exception example
class NegativeValueError(Exception):
    """Custom error for negative values"""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value error: {value} is not allowed!")

def square_root(number):
    """Calculate square root with custom exception"""
    try:
        if number < 0:
            raise NegativeValueError(number)
        result = number ** 0.5
    except NegativeValueError as e:
        print(e)
        logging.error("NegativeValueError: %s", e)
    else:
        print(f"Square root of {number} is {result}")
    finally:
        print("square_root() execution completed.\n")

# ---------- Test the functions ----------

# Multiple exception handling
divide_numbers(10, 2)       # valid
divide_numbers(5, 0)        # ZeroDivisionError
divide_numbers("5", 2)      # TypeError

# File handling with exceptions
read_file("existing_file.txt")   # file exists
read_file("missing_file.txt")    # file does not exist

# Custom exception
square_root(16)     # valid
square_root(-9)     # triggers custom error
