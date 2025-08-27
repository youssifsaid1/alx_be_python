<<<<<<< HEAD
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
=======
# Personal Daily Reminder

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Provide customized reminder based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an undefined priority"

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("Reminder:", reminder)
>>>>>>> 222d8d36cd6a00ca7f79f9e8cc7508987894d8e5
