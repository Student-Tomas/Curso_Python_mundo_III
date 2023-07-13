# Challenge number 101: create a function that returns the right's vote status of a citizen.
def vote(born):
    from datetime import date
    current_year = date.today().year
    age = current_year - born
    if age < 16:
        return f'Being {age} years old: CAN NOT VOTE!'
    elif 16 <= age < 18 or age > 65:
        return f'Being {age} years old: OPTIONAL VOTE!'
    else:
        return f'Being {age} years old: COMPULSORY VOTE!'


# Main program
year = int(input('What is your year of born? '))
print(vote(year))
