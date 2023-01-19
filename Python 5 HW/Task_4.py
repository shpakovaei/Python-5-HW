# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open ('file1.txt' , 'r', encoding='utf-8') as file:
    some_list = file.read().split()
    print (some_list)


def encode(s):
    encoding = '' 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding

print(encode(some_list))

with open ('file2.txt' , 'r', encoding='utf-8') as file:
    some_lisst = file.read().split()
    print (some_lisst)

def decode(s): 
    decode = '' 
    count = ''
    for char in s:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

print(decode (some_lisst))

