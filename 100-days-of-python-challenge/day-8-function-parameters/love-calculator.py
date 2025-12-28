# Love Calculator
# This program calculates the "love score" between two people based on their names.

def love_calculator(name1, name2):
    combined_names = (name1 + name2).lower()
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    love_score = int(f"{true_count}{love_count}")
    
    if love_score > 90:
        return f"Your love score is {love_score}, you are made for each other."
    elif 40 <= love_score <= 50:
        return f"Your love score is {love_score}, you are alright together."
    else:
        return f"Your love score is {love_score}."

name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")

result = love_calculator(name1, name2)
print(result)