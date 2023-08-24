def increase(n, p):
    result = n * (1+(p/100))
    return result


def decrease(n, p):
    result = n * (1-(p/100))
    return result


def half(n):
    result = n / 2
    return result

def double(n):
    result = n * 2
    return result

def currency(n, currency='US$'):
    return f'{currency}{n:.2f}'.replace(".", ",")
