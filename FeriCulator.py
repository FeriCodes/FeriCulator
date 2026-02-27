import math


def show_menu():
    print("\n--- Main Menu ---")
    print("1. Standard Calculator")
    print("2. View History")
    print("3. Clear History")
    print("4. Help")
    print("5. Exit")
    choice = input("Select an option (1-5): ")
    return choice


def get_history():
    try:
        open("CalHistory.txt", "a").close()
        with open("CalHistory.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []  # if don't have a file return an empty list.


def clear_history_file():
    open("CalHistory.txt", "w").close()


def calculate(num1, operator, num2=None):
    if operator == "sqrt":
        if num1 < 0:
            return "ERROR!"
        return math.sqrt(num1)

    if num2 is None:
        return "error (missing second number)"

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "%":
        return num1 % num2 if num2 != 0 else "DIVISION_BY_ZERO!"
    elif operator == "//":
        return num1 // num2 if num2 != 0 else "DIVISION_BY_ZERO!"
    elif operator == "**":
        return num1 ** num2
    elif operator == "/":
        return num1 / num2 if num2 != 0 else "DIVISION_BY_ZERO!"


def handle_exit():  # 5 exit the fericulate!
    print("Thank you for using Fericulator. Goodbye!")


def view_help():  # 4 calculator help in the menu
    print("\n" + "*"*30)
    print("      FERICULTOR HELP")
    print("*"*30)
    print("- Standard: 10 + 20 =")
    print("- Square Root: sqrt 144 =")
    print("- Supported: +, -, *, /, //, %, **, sqrt")
    print("- Type 'back' inside calculator to return to menu.")
    print("*"*30)
    input("\nPress Enter to return...")


def get_clear_history():  # choice 3 in main manu for getting clear history.
    print("do you want to clear calculation history? (y/n): ")
    confirm = input().strip().lower()
    if confirm != "y":
        print("Operation cancelled. History not cleared.")
        return
    else:
        print("\nClearing calculation history...")
        clear_history_file()
        print("History cleared.")


def view_history():  # 2 view history (if choice 1 in main menu)
    print("\n--- Calculation History ---")
    history = get_history()
    if not history:
        print("No history found.")
    else:
        for item in history:
            print(f"- {item}")


def run_standard_calculation():  # 1- Standard Calculator

    while True:  # bug fix:# stay in calculator mode until the user returns to the main menu

        print("\n(Example: '5 + 3 =' or 'sqrt 16 =') - Type 'back' to return")
        user_expr = input("Enter your calculation: ").strip().lower()

        if user_expr.lower() == "back":  # return to main menu
            break

        user_expr = user_expr.replace("=", " ").strip()

        if not user_expr:
            print("Error: please enter a calculation.")
            continue

        operators = ["**", "//", "sqrt", "+", "-", "*", "/", "%"]

        for op in operators:  # bug fix: add spaces around operators to ensure correct splitting
            user_expr = user_expr.replace(op, f" {op} ")

        user_expr = " ".join(user_expr.split())

        parts = user_expr.split()

        try:
            if not parts:
                print("Error: Please enter something!")
                continue

            if parts[0].lower() == "sqrt" and len(parts) == 2:
                n1 = float(parts[1])
                result = calculate(n1, "sqrt")
                full_record = f"sqrt {n1} = {result}"
                print(f"sqrt {n1} = {result}")

            elif len(parts) == 3:
                n1 = float(parts[0])
                op = parts[1]
                n2 = float(parts[2])
                result = calculate(n1, op, n2)
                full_record = f"{n1} {op} {n2} = {result}"

            else:
                print("Error: Invalid format. Use 'num1 op num2' or 'sqrt num'")
                continue

            print(f"\n Full: {full_record}")

            with open("CalHistory.txt", "a") as file:
                file.write(full_record + "\n")

        except (ValueError, IndexError):
            print("Error: Please follow the format 'num1 op num2' or 'sqrt num'.")


def main():
    print("wellocme to the FeriCulator")

    while True:
        choice = show_menu()
        if choice == "1":
            run_standard_calculation()
        elif choice == "2":
            view_history()
        elif choice == "3":
            get_clear_history()
        elif choice == "4":
            view_help()
        elif choice == "5":
            handle_exit()
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()
