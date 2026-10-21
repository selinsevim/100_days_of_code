chosen_word = "araba"
letter = "a"
placeholder = list("-----")
for i, char in enumerate(chosen_word):
    print(i)
    if char == letter:
        placeholder[i] = letter

print("".join(placeholder))