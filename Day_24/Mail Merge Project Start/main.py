# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(
    "/Users/selinsevim/Documents/100_days_of_code/Day_24/Mail Merge Project Start/Input/Names/invited_names.txt"
) as names:
    names = names.readlines()

with open(
    "/Users/selinsevim/Documents/100_days_of_code/Day_24/Mail Merge Project Start/Input/Letters/starting_letter.txt"
) as letter:
    lines = letter.read()

for name in names:
    name = name.strip("\n")
    new_lines = lines.replace("[name]", name)
    with open(
        f"/Users/selinsevim/Documents/100_days_of_code/Day_24/Mail Merge Project Start/Output/ReadyToSend/{name}.txt",
        mode="w",
    ) as new_texts:
        new_texts.write(new_lines)
