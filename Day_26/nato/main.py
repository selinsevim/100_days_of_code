import pandas as pd

# Example Code
student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for key, value in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pd.read_csv(
    "/Users/selinsevim/Documents/100_days_of_code/Day_26/nato/nato_phonetic_alphabet.csv"
)

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_answer = input("Enter a word: ").upper()
word_list = [nato_dict[letter] for letter in user_answer]
print(word_list)
