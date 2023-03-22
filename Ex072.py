#Challenge number 072: Write numbers in full
list = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
'nineteen', 'twenty')
while True:
    while True:
        num = int(input("Say a number between 0 and 20: "))
        if 0 <= num <= 20:
            break
        print('Try again!')
    print(f"You said the number {list[num]}")
    #while True:
    quest = str(input('Do you want to ask again? Y or N? ')).strip().upper()[0]
    if quest == "N":
         break
