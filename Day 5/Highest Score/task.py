student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#print(range(1, 10))

# Calculate the sum
total_sum = 0
for score in student_scores:
    total_sum += score
print(total_sum)

# Find the maximum number in the list
max_number = student_scores[0]
for score in student_scores:
    if score > max_number:
        max_number = score
print(max_number)