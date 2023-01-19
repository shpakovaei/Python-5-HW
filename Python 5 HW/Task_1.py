# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open ('file.txt' , 'r', encoding='utf-8') as file:
    some_list = file.read().split()
    print (some_list)

new_list = filter (lambda word: 'а' not in word and 'б' not in word and 'в' not in word, some_list)
print (list(new_list))

