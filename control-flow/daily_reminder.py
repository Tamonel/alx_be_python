
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    if priority == "high":
        reminder += ". Focus on completing it soon."
    elif priority == "medium":
        reminder += ". Try to complete it when possible."
    elif priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". Plan accordingly."

    print(f"Note: {reminder}")
