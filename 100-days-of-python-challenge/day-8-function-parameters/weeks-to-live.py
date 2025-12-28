#weeks to live assuming you live to 90 years
def weeks_to_live(age):
    weeks_in_a_year = 52
    total_weeks = 90 * weeks_in_a_year
    weeks_lived = age * weeks_in_a_year
    weeks_left = total_weeks - weeks_lived
    return weeks_left

age = int(input("Enter your age as a number in years: "))
weeks_left = weeks_to_live(age)
print(f"You have {weeks_left} weeks left to live.")