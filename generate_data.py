import csv
import random
import numpy as np

num_samples = 200

with open("student_marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Hours_Studied",
        "Attendance",
        "Avg",
        "Max",
        "Min",
        "Var",
        "Final_Marks"
    ])

    for _ in range(num_samples):

        num_subjects = random.randint(3, 6)
        marks = [random.randint(5, 30) for _ in range(num_subjects)]

        avg = np.mean(marks)
        max_m = np.max(marks)
        min_m = np.min(marks)
        var = np.var(marks)

        hours = random.randint(1, 10)
        attendance = random.randint(40, 100)

        # smarter formula
        base = (
            0.5 * avg +
            0.3 * attendance +
            0.2 * hours * 10
        )

        if min_m < 10:
            base -= 10

        base -= var * 0.5

        noise = random.uniform(-5, 5)

        final = base + noise
        final = max(0, min(final, 100))

        writer.writerow([
            hours, attendance, avg, max_m, min_m, var, int(final)
        ])

print("Dataset created!")