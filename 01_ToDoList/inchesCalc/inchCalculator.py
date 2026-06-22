from inchCalculatorFunctions import *

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