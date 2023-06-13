# Challenge number 098: make a program that counts from 0 to 10 with a pace of 1, from 10 to 0 with a pace of 2, and a
# personalized counting

from time import sleep
def counter(s, e, p):
# counter(start, end, pace)
    if p < 0:
        p *= -1
    if p == 0:
        p += 1
    print('-=' *20)
    if s < e:
        print(f'Counting from {s} to {e}, {p} by {p}.')
        count = s
        while count <= e:
            print(f'{count}, ', end='')
            sleep(0.5)
            count += p
        print()
        print('-=' *20)
        print(f"That's all, folks!!!!")
    else:
        print(f'Counting from {s} to {e}, {p} by {p}.')
        count = s
        while count >= e:
            print(f'{count}, ', end='')
            sleep(0.5)
            count -= p
        print()
        print('-=' * 20)
        print(f"That's all, folks!!!!")
        print('-=' * 20)
# Main program
counter(1, 10, 1)
counter(10, 1, 2)
start = int(input('Start: '))
end = int(input('End: '))
pace = int(input('Pace: '))
counter(start, end, pace)

