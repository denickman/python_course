def get_feet():
    """Запрашивает feet с подсказкой"""
    while True:
        try:
            feet = float(input('Enter feet (positive number): '))
            if feet < 0:
                print("❌ Feet must be positive, try again\n")
                continue
            return feet
        except ValueError:
            print("❌ Please enter a valid number\n")


def get_inches():
    """Запрашивает inches с подсказкой и проверкой"""
    while True:
        try:
            inches = float(input('Enter inches (0-11): '))

            if inches < 0:
                print("❌ Inches must be positive, try again\n")
                continue

            if inches >= 12:
                print(f"❌ Inches must be between 0 and 11 (you entered {inches})")
                print("   Remember: 12 inches = 1 foot\n")
                continue

            return inches
        except ValueError:
            print("❌ Please enter a valid number\n")
