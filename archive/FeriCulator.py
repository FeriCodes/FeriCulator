import math


def show_menu():
    print("\n--- Main Menu ---")
    print("1. Standard Calculator")
    print("2. View History")
    print("3. Clear History")
    print("4. Help")
    print("5. Exit")
    print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
    print("Type 'back' or 'b' to return to the main menu.")
    print("-" * 50)
    print()
    choice = input("Select an option (1-5): ")
    return choice


def run_standard_calculation():
    print("\n(Example: '5 + 3 =' or 'sqrt 16 =') - Type 'back' to return")

    while True:
        user_input = input("Enter your calculation: ")
        result_type, data = parse_and_validate_expression(user_input)

        if result_type == "b":
            break

        elif result_type == "error":
            print(data)
            continue

        elif result_type == "sqrt":
            n1 = data

            result = calculate(n1, "sqrt")
            full_record = f"sqrt {n1} = {result}"
            print(f"\nResult: {result}")
            save_calculation_to_history(full_record)

        elif result_type == "calc":
            n1, op, n2 = data

            result = calculate(n1, op, n2)
            full_record = f"{n1} {op} {n2} = {result}"
            print(f"\nResult: {result}")
            save_calculation_to_history(full_record)


def save_calculation_to_history(full_record):
    try:
        with open("CalHistory.txt", "a") as file:
            file.write(full_record + "\n")
    except IOError:
        print("Error: Could not write to history file.")


def parse_and_validate_expression(user_expr):
    """
    Parses and validates the user's input expression.
    Returns a tuple: (type, data)
    type can be 'back', 'error', 'sqrt', or 'calc'.
    data contains relevant info (number, operator, etc.) or an error message.
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
            return ("sqrt", n1)

        elif len(parts) == 3:
            n1 = float(parts[0])
            op = parts[1]
            # Check if the operator is valid
            if op not in ["+", "-", "*", "/", "%", "**", "//"]:
                return ("error", "Error: Invalid operator.")
            n2 = float(parts[2])
            return ("calc", (n1, op, n2))

        else:
            return ("error", "Error: Invalid format. Use 'num1 op num2' or 'sqrt num'")

    except ValueError:
        return ("error", "Error: Invalid number format.")
    except IndexError:
        return ("error", "Error: Missing operand or operator.")


def view_history():  # 2 view history
    print("\n--- Calculation History ---")
    history = get_history()
    if not history:
        print("No history found.")
    else:
        for item in history:
            print(f"- {item}")


# this function read the file and then add the new calculation on the history file.
def get_history():
    try:
        with open("CalHistory.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []  # if don't have a file return an empty list.


def clear_history():  # choice 3 in main manu for getting clear history.
    print("do you want to clear calculation history? (y/n): ")
    confirm = input().strip().lower()
    if confirm != "y":
        print("Operation cancelled. History not cleared.")
        return
    else:
        print("\nClearing calculation history...")
        clear_history_file()
        print("History cleared!")


def view_help():  # 4 calculator help in the menu
    print("\n" + "*" * 30)
    print("      FeriCulator HELP")
    print("*" * 30)
    print("- Standard: 10 + 20 =")
    print("- Square Root: sqrt 144 =")
    print("- Supported: +, -, *, /, //, %, **, sqrt")
    print("- Type 'back' inside calculator to return to menu.")
    print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
    print("Type 'back' or 'b' to return to the main menu.")
    print("*" * 30)
    input("\nPress Enter to return...")


def handle_exit():  # 5 exit the fericulate!
    print("Thank you for using Fericulator. Goodbye!")


def clear_history_file():
    open("CalHistory.txt", "w").close()


def calculate(num1, operator, num2=None):
    if operator == "sqrt":
        if num1 < 0:
            return "ERROR: Negative number for sqrt"
        return math.sqrt(num1)

    if num2 is None:
        return "ERROR: Missing second number"

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "%":
        return num1 % num2 if num2 != 0 else "ERROR: Division by zero"
    elif operator == "//":
        return num1 // num2 if num2 != 0 else "ERROR: Division by zero"
    elif operator == "**":
        return num1**num2
    elif operator == "/":
        return num1 / num2 if num2 != 0 else "ERROR: Division by zero"
    else:
        return "ERROR: unknown operation!"


def main():
    print("wellocme to the FeriCulator")

    while True:
        choice = show_menu()
        if choice == "1":
            run_standard_calculation()
        elif choice == "2":
            view_history()
        elif choice == "3":
            clear_history()
        elif choice == "4":
            view_help()
        elif choice == "5":
            handle_exit()
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()
