# Challenge number 097. Creat a program that show anything the user wants, centralized between frames above and under.
def wright(msg):
    msg_len = len(msg) + 4
    print('~' * msg_len)
    print(f'  {msg}')
    print('~' * msg_len)


# Main Program
wright('Vou ter que aprender Python, html, css and JS')
