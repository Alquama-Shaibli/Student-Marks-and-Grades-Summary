#Grading system for the student 

def calculate_grade(average):
    if average >= 91:
        return 'A1'
    elif average >= 81:
        return 'A2'
    elif average >= 71:
        return 'B1'
    elif average >= 61:
        return 'B2'
    elif average >= 51:
        return 'C1'
    elif average >= 41:
        return 'C2'
    elif average >= 33:
        return 'D'
    else:
        return 'E (Fail)'

def main():
    
    # Input number of students and their marks

    n = int(input("Enter the number of students: "))
    students = []

    for i in range(n):
        name = input(f"\nEnter name of student {i + 1}: ")
        marks = []
        for j in range(3):
            while True:
                try:
                    mark = float(input(f"Enter marks for Subject {j + 1} (0-100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Please enter marks between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        total = sum(marks)
        average = total / 3
        grade = calculate_grade(average)

        students.append({
            'name': name,
            'marks': marks,
            'total': total,
            'average': average,
            'grade': grade
        })

    print("\n--- Student Summary ---")
    for s in students:
        print(f"Name: {s['name']}")
        print(f"  Marks: {s['marks']}")
        print(f"  Total: {s['total']:.2f}")
        print(f"  Average: {s['average']:.2f}")
        print(f"  Grade: {s['grade']}\n")

    class_average = sum(s['average'] for s in students) / n
    print(f"Class Average: {class_average:.2f}")

    # Filter out students who failed (grade "E (Fail)") when determining topper
    passed_students = [s for s in students if s['grade'] != 'E (Fail)']

    if passed_students:
        topper = max(passed_students, key=lambda x: x['average'])
        print(f"Topper: {topper['name']} with average {topper['average']:.2f}")
    else:
        print("No topper (all students failed).")

if __name__ == "__main__":
    main()
