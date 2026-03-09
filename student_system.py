# student_system.py
# Day 9 AM - Lists Deep Dive
# Student Management System

records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Sneha", "Chemistry", 83],
    ["Karan", "Physics", 67],
    ["Divya", "Math", 95],
    ["Rohan", "Chemistry", 72],
    ["Anita", "Physics", 85],
    ["Vikram", "Math", 60],
    ["Meena", "Chemistry", 90],
    ["Arjun", "Physics", 78],
    ["Pooja", "Math", 88],
]


def add_student(name, subject, marks):
    # Check for duplicate name + subject combo
    for r in records:
        if r[0] == name and r[1] == subject:
            print(f"  {name} already exists in {subject}. Skipping.")
            return
    records.append([name, subject, marks])
    print(f"  Added: {name}, {subject}, {marks}")


def get_toppers(subject):
    subject_records = [r for r in records if r[1] == subject]
    if not subject_records:
        print(f"  No records found for {subject}.")
        return []
    top3 = sorted(subject_records, key=lambda x: x[2], reverse=True)[:3]
    return top3


def class_average(subject):
    marks_list = [m[2] for m in records if m[1] == subject]
    if not marks_list:
        return 0
    return sum(marks_list) / len(marks_list)


def above_average_students():
    all_marks = [r[2] for r in records]
    overall_avg = sum(all_marks) / len(all_marks)
    above = [r for r in records if r[2] > overall_avg]
    return above, overall_avg


def remove_student(name):
    global records
    # Using list comprehension - NOT remove() inside loop
    before = len(records)
    records = [r for r in records if r[0] != name]
    after = len(records)
    removed = before - after
    if removed:
        print(f"  Removed {removed} record(s) for '{name}'.")
    else:
        print(f"  No records found for '{name}'.")


def save_to_file():
    with open("students.txt", "w") as f:
        for r in records:
            f.write(f"{r[0]},{r[1]},{r[2]}\n")
    print("  Records saved to students.txt")


def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Toppers (by Subject)")
    print("3. Show Class Average (by Subject)")
    print("4. Show Above-Average Students")
    print("5. Remove Student")
    print("6. Exit")
    print("=====================================")


def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("  Name: ").strip()
            subject = input("  Subject: ").strip()
            try:
                marks = int(input("  Marks: ").strip())
            except ValueError:
                print("  Invalid marks. Please enter a number.")
                continue
            add_student(name, subject, marks)

        elif choice == "2":
            subject = input("  Enter subject: ").strip()
            toppers = get_toppers(subject)
            if toppers:
                print(f"\n  Top 3 in {subject}:")
                for i, t in enumerate(toppers, 1):
                    print(f"    {i}. {t[0]} - {t[2]}")

        elif choice == "3":
            subject = input("  Enter subject: ").strip()
            avg = class_average(subject)
            if avg:
                print(f"  Average marks in {subject}: {avg:.2f}")
            else:
                print(f"  No data for {subject}.")

        elif choice == "4":
            above, avg = above_average_students()
            print(f"\n  Overall average: {avg:.2f}")
            print(f"  Students above average ({len(above)}):")
            for s in above:
                print(f"    {s[0]} | {s[1]} | {s[2]}")

        elif choice == "5":
            name = input("  Enter student name to remove: ").strip()
            remove_student(name)

        elif choice == "6":
            save_to_file()
            print("  Goodbye!")
            break

        else:
            print("  Invalid choice. Try again.")


if __name__ == "__main__":
    main()
