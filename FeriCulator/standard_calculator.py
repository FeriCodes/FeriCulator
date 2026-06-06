"""
standard calculator module for FeriCulator.
"""

import math
import operator


class Calculator:
    """
    this class for standard calculator operations, including parsing user input,
    validating it, and performing calculations.
    """

    def __init__(self):
        self.operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda num1, num2: (
                num1 / num2 if num2 != 0 else "ERROR: Division by zero"
            ),
            "//": lambda num1, num2: (
                num1 // num2 if num2 != 0 else "ERROR: Division by zero"
            ),
            "%": lambda num1, num2: (
                num1 % num2 if num2 != 0 else "ERROR: Division by zero"
            ),
            "**": operator.pow,
            "sqrt": lambda num1: (
                math.sqrt(num1) if num1 >= 0 else "ERROR: Negative number for sqrt"
            ),
        }

    def parse_and_validate(self, user_expr):
        """
        Parses the user input expression and validates it for standard calculations.
        Supports basic operations and square root.
        """
        user_expr = user_expr.strip().lower()

        if user_expr in ["back", "b"]:
            return ("back", None)

        # Replace operators with spaces for easier splitting, ensuring spaces around them.
        operators = ["**", "//", "sqrt", "+", "-", "*", "/", "%"]
        for op in operators:
            user_expr = user_expr.replace(op, f" {op} ")

        user_expr = " ".join(user_expr.split())  # Remove extra spaces
        parts = user_expr.split()

        if not parts:
            return ("error", "Error: Please enter a calculation.")

        try:
            if parts[0] == "sqrt" and len(parts) == 2:
                n1 = float(parts[1])
                return ("sqrt", n1)  # Return the number for sqrt operation

            if len(parts) == 3:
                n1 = float(parts[0])
                op = parts[1]
                # Check if the operator is valid
                if op not in ["+", "-", "*", "/", "%", "**", "//", "sqrt"]:
                    return ("error", "Error: Invalid operator.")
                n2 = float(parts[2])
                return ("calc", (n1, op, n2))

        except ValueError:
            return ("error", "Error: Invalid number format.")
        except IndexError:
            return ("error", "Error: Missing operand or operator.")

        return (
            "error",
            "Error: Invalid format. Use 'num1 op num2' or 'sqrt num'",
        )

    def calculate(self, num1, op, num2=None):
        """
        Performs the calculation based on the operator and operands provided.
        """
        if op not in self.operations:
            return "ERROR: unknown operation!"

        func = self.operations[op]

        try:
            if num2 is None:
                return "ERROR: Missing second number"

            return func(num1, num2)

        except (ValueError, TypeError, ZeroDivisionError) as e:
            return f"ERROR: {str(e)}"
        except Exception as e:
            return "ERROR: Invalid calculation"

    def calculate_sqrt(self, num1):
        """
        Helper function to calculate the square root of a number.
        """
        try:
            if num1 < 0:
                return "ERROR: Negative number for sqrt"
            return math.sqrt(num1)
        except (ValueError, TypeError) as e:
            return f"ERROR: {str(e)}"
