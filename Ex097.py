# Challenge number 097. Using functions, creat a program that show anything the user wants, centralized between frames above and under.
def wright(msg):
    msg_len = len(msg) + 4
    print('~' * msg_len)
    print(f'  {msg}')
    print('~' * msg_len)


# Main Program
wright('Vou ter que aprender Python, html, css and JS')
wright('I have to be more disciplined')
wright("I'm sure it will worth it")
