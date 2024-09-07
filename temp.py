def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value}°C is equivalent to {fahrenheit:.2f}°F and {kelvin:.2f}K")
    elif unit.lower() == 'f':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value}°F is equivalent to {celsius:.2f}°C and {kelvin:.2f}K")
    elif unit.lower() == 'k':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value}K is equivalent to {celsius:.2f}°C and {fahrenheit:.2f}°F")
    else:
        print("Unknown unit. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")


value = float(input("Enter the temperature value: "))
unit = input("Enter the unit of measurement (C/F/K): ")
convert_temperature(value, unit)

# Degrees Celsius - C
# Fahrenheit - F
# Kelvin - K 
# Sample input - 25
#                C
# Sample output - 25.0°C is equivalent to 77.00°F and 298.15
