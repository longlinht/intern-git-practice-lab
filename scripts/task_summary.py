#!/usr/bin/env python3

"""Print a short summary of the completed intern Git practice tasks."""


def main():
    intern_name = "Wadha Msaiqer"
    current_focus = "Git workflow practice for robotics development documentation"
    completed_tasks = [
        "Updated the project introduction",
        "Added personalized intern role and interests",
        "Documented robot startup checks",
        "Added professional robot safety rules",
        "Updated daily work log and ignore rules",
    ]

    print("Robot task summary loaded successfully")
    print(f"Intern: {intern_name}")
    print(f"Current focus: {current_focus}")
    print("Completed tasks:")
    for task in completed_tasks:
        print(f"- {task}")


if __name__ == "__main__":
    main()
