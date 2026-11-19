import random
import pandas as pd

# LIST COMPREHENSION - 1
numbers = [1, 2, 3]
new_list = [number + 1 for number in numbers]
# print(new_list)

# LIST COMPREHENSION - 2
name = "Noah"
new_list = [letter for letter in name]
# print(new_list)

# LIST COMPREHENSION - 3
range_seq = range(1, 5)
new_range = [num * 2 for num in range_seq]
# print(new_range)

# LIST COMPREHENSION - 4
names = ["Selin", "Noah", "Matthias", "Ataberk", "Osman", "Ebru"]
short_names = [name for name in names if len(name) <= 4]
upper_case_long_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)
# print(upper_case_long_names)

# DICTIONARY COMPREHENSION - 1
names = ["Selin", "Noah", "Matthias", "Ataberk", "Osman", "Ebru"]
student_scores = {student: random.randint(1, 100) for student in names}

# student_scores = {}
# for name in names:
#     score = random.randint(1, 100)
#     student_scores[name] = score

# print(student_scores)

# DICTIONARY COMPREHENSION - 2
passed_students = {
    student: score
    for (student, score) in student_scores.items()
    if student_scores[student] > 60
}
# print(passed_students)


# PANDAS
student_dict = {"student": ["Selin", "Matthias", "Noah"], "scores": ["80", "90", "100"]}

dataframe = pd.DataFrame(student_dict)
print(dataframe)

for student, score in dataframe.items():
    print(student)
    print(score)

# Looping through rows
for index, row in dataframe.iterrows():
    # Each of these rows are panda series object
    print(row.student)
