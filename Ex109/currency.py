def increase(n, p, style=False):
    result = n * (1+(p/100))
    return result if not style else currency(result)


def decrease(n, p, style=False):
    result = n * (1-(p/100))
    return result if style is False else currency(result)


def half(n, style=False):
    result = n / 2
    return result if not style else currency(result)

def double(n, style=False):
    result = n * 2
    return result if not style else currency(result)

def currency(n, currency='US$'):
    return f'{currency}{n:.2f}'.replace(".", ",")
