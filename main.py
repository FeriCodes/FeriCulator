"""
FeriCulator: A scientific calculator with history management.
Main entry point of the application.
"""

from FeriCulator.standard_calculator import Calculator
from FeriCulator.history_manager import History
from FeriCulator.scientific_calculator import ScientificCalculation


def show_menu():
    """
    Displays the main menu and prompts the user for a choice.
    """
    print("\n--- Main Menu ---")
    print("1. Standard Calculator")
    print("2. Scientific Calculator")
    print("3. View History")
    print("4. Clear History")
    print("5. Help")
    print("6. Exit")
    print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
    print("Type 'back' or 'b' to return to the main menu.")
    print("-" * 50)
    print()

    choice = input("Select an option (1-6): ")
    return choice


def handle_standard_calculator(standard_calc, history_tools):
    """
    1. Handles the standard calculator operations.
    """
    while True:
        user_input = input("Enter your calculation: ")
        result_type, data = standard_calc.parse_and_validate(user_input)
        if result_type == "back":
            break

        if result_type == "error":
            print(data)
            continue

        if result_type == "sqrt":
            n1 = data
            result = standard_calc.calculate_sqrt(n1)
            print(f"\nResult: {result}")

            if "ERROR" not in str(result):
                history_tools.save_calculation_to_history(f"sqrt {n1}", result)

        elif result_type == "calc":
            n1, op, n2 = data
            result = standard_calc.calculate(n1, op, n2)
            print(f"\nResult: {result}")

            if "ERROR" not in str(result):
                history_tools.save_calculation_to_history(f"{n1} {op} {n2}", result)


def handle_scientific_calculator(scientific_calc, history_tools):
    """
    2. Handles the scientific calculator operations.
    """
    while True:
        print("\n--- Scientific Calculator ---")
        print("Available operations: fac, sin, cos, tan, cot, pi")
        print("Type 'back' or 'b' to return to the main menu.")
        print("-" * 50)

        op = input("Enter operation: ").strip().lower()
        if op in ["back", "b"]:
            break

        if op not in ["fac", "sin", "cos", "tan", "cot", "pi"]:
            print("ERROR: Invalid Operation!")
            continue

        user_num = input("Enter number: ").strip()

        if user_num == "":
            if op == "pi":
                user_num = "1"
            else:
                print("ERROR: Number cannot be empty for this operation!")
                continue

        try:
            result = scientific_calc.calculate(op, user_num)
            print(f"\nResult: {result}")

            if "ERROR" not in str(result) and result != "Invalid Operation!":
                history_tools.save_calculation_to_history(f"{op} {user_num}", result)

        except ValueError:
            print("ERROR: Please enter a valid numeric value!")
        except (ZeroDivisionError, OverflowError) as e:
            print(f"Mathematical ERROR: {e}")


def view_help():
    """
    5. Displays help information about how to use the calculator.
    """
    print("\n" + "-" * 30)
    print("      FeriCulator HELP")
    print("-" * 30)
    print("- Standard: 10 + 20 =")
    print("- Square Root: sqrt 144 =")
    print("- Supported: +, -, *, /, //, %, **, sqrt")
    print("- Type 'back' inside calculator to return to menu.")
    print("\nEnter a calculation like: '5 + 3' or 'sqrt 16'")
    print("Type 'back' or 'b' to return to the main menu.")
    print("\nScientific Operations:")
    print("- Factorial: fac 5")
    print("- Sine: sin 30")
    print("- Supported: fac, sin, cos, tan, cot, pi")
    print("- Type 'back' inside calculator to return to menu.")
    print("-" * 30)
    input("\nPress Enter to return...")


def handle_exit():
    """
    6. Exits the application gracefully.
    """
    print("Thank you for using Fericulator. Goodbye!")


def main():
    """
    Displays a welcome message and the main menu.
    Handles user input to navigate between standard, scientific,
    and history management features.
    """
    print("Welcome to the FeriCulator")
    standard_calc = Calculator()
    history_tools = History()
    scientific_calc = ScientificCalculation()
    while True:

        choice = show_menu()
        if choice == "1":
            handle_standard_calculator(standard_calc, history_tools)
        elif choice == "2":
            handle_scientific_calculator(scientific_calc, history_tools)
        elif choice == "3":
            history_tools.view_history()
        elif choice == "4":
            history_tools.clear_history()
        elif choice == "5":
            view_help()
        elif choice == "6":
            handle_exit()
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()
