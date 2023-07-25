#Challenge number 102: create a function that calculate the factorial of a number and show, or not, the calculation
#memory. Besides this, insert the docstirngs for the funcition.
def factorial(num, show=False):
    """
    -> Return the factorial of a number
    :param num: it is the number you want to see the factorial;
    :param show: it is able to show, or not, the calculation memory;
    :return: returns the factorial number's final result.
    """
    fac = 1
    for i in range(num, 0, -1):
        fac *= i
        if show == True:
            print(i, end="")
            if i > 1:
                print(f' X ', end="")
            else:
                print(f' = ', end="")
    return fac


n = int(input(f'What is the number you want to see its factorial? '))
print(factorial(n, show=True))
help(factorial)
