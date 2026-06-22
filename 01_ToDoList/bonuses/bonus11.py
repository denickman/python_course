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


def convert(feet, inches):
    """Конвертирует в метры"""
    meters = feet * 0.3048 + inches * 0.0254
    return f'{feet} feet and {inches} inches = {meters:.2f} meters'


# Использование:
print("=== Feet to Meters Converter ===\n")
feet = get_feet()
inches = get_inches()
result = convert(feet, inches)
print(f"\n✅ {result}")