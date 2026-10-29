
# My AI Study Planner
# Beginner-friendly Python project

def get_number(prompt, minimum, maximum, whole_number=False):
    while True:
        try:
            if whole_number:
                value = int(input(prompt))
            else:
                value = float(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a value from {minimum} to {maximum}")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("\n=== MY AI STUDY PLANNER ===\n")

    name = input("Enter your name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter your name: ").strip()

    goal = input("What is your AI learning goal? ").strip()
    while not goal:
        goal = input("Please enter your learning goal: ").strip()

    days = get_number(
        "How many days per week will you study (1-7)? ",
        1, 7, whole_number=True
    )

    hours = get_number(
        "How many hours will you study each day (1-24)? ",
        1, 24
    )

    weekly_hours = days * hours

    weekdays = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    plan = [
        "MY AI STUDY PLAN",
        "=" * 30,
        f"Student: {name}",
        f"Learning Goal: {goal}",
        f"Study Days Per Week: {days}",
        f"Daily Study Hours: {hours:g}",
        f"Total Weekly Study Hours: {weekly_hours:g}",
        "",
        "WEEKLY SCHEDULE",
        "-" * 30
    ]

    for day in weekdays[:days]:
        plan.append(f"\n{day} - {hours:g} hour(s)")
        plan.append(f"Goal: Make progress toward {goal}.")
        plan.append("Activity: Learn a new concept and take notes.")
        plan.append("Practice: Complete an exercise or small project.")

    plan.extend([
        "",
        "STUDY TIPS",
        "- Set a small goal for each session.",
        "- Take breaks when needed.",
        "- Review your notes regularly.",
        "- Check your progress every week."
    ])

    plan_text = "\n".join(plan)

    print("\n" + plan_text)

    with open("study_plan.txt", "w", encoding="utf-8") as file:
        file.write(plan_text + "\n")

    print("\nYour plan has been saved to study_plan.txt!")


if __name__ == "__main__":
    main()
