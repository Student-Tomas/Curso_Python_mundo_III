# Challenge number 077: create a program that reads a tuple with many words and say the vowels of each word
words_list = ('course', 'free', 'python', 'programing', 'learn', 'study', 'future', 'market', 'job')
#vowels_list = ('a', 'e', 'i', 'o', 'u')
for word in words_list:
    print(f'\nIn the word "{word}" we have:',end=' ')
    for letter in word:
        if letter in "aeiou":
            print(letter, end=' ')




