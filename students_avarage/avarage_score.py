"""
Task
Create a program that contains the names and scores of students.
The code should write student data in file, calculate it and write
Avarage socre in new file.
"""

# Solution
# Take data and contain it to list
# Import os(2 files will save in avarage_score folder)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STUDENTS_FILE = os.path.join(BASE_DIR, "students_data.txt")
AVERAGE_FILE = os.path.join(BASE_DIR, "avarage_score.txt")

data = ["Maks", 89, 56, 78, 90, "Anya", 67, 69, 52, 14, 88, "Jhon", 91, 14, 67, 89]


# Create a function that save it to students_data.txt
def get_data():
    try:
        with open(STUDENTS_FILE, "w", encoding="utf-8") as file:
            # write each item on its own line as string
            file.write("\n".join(str(item) for item in data))
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")


# Get gata and calculate average score
def avarage_score():
    try:
        with open(STUDENTS_FILE, encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        averages = {}
        name = None
        scores = []
        for line in lines:
            try:
                val = float(line)
                scores.append(val)
            except ValueError:
                # line is a name
                if name is not None and scores:
                    averages[name] = sum(scores) / len(scores)
                name = line
                scores = []
        if name is not None and scores:
            averages[name] = sum(scores) / len(scores)
        return averages
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
    return {}


# Write avarage score in avarage_score.txt
def write_avar_score():
    try:
        # ensure data file exists
        get_data()
        averages = avarage_score()
        with open(AVERAGE_FILE, "w", encoding="utf-8") as new_file:
            for name, avg in averages.items():
                new_file.write(f"{name}: {avg}\n")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
        return


print("Program is starting...")
write_avar_score()
print("Done. Check avarage_score.txt")
