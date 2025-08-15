# Personal Daily Reminder

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Provide customized reminder based on priority and time sensitivity
match priority.lower():
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority"

# Modify message if task is time-bound
if time_bound.lower() == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print("Reminder:", message)
