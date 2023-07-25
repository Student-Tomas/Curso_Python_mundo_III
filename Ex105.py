# Challenge number 105: create a function with a dictionary that receives some grades from students and show
# the greatest grade, the lowest, the average grade, and the possibility of show the situation or not show.
def grade(*n, sit=False):
    """

    :param n: that is the student's grades informed
    :param sit: that is the situation related to the average grade of the group
    :return: that is the dictionary content related to the results asked
    """
    a = dict()
    a['total'] = len(n)
    a['greatest'] = max(n)
    a['lowest'] = min(n)
    a['average'] = sum(n) / len(n)
    if sit == True:
        if a['average'] >= 7:
            a['situation'] = "Good"
        elif a['average'] >= 5:
            a['situation'] = "Acceptable"
        else:
            a['situation'] = "Bad"

    return a

#Main program
answer = grade(10, 8, 8, 7, sit=True)
print(answer)
help(grade)
