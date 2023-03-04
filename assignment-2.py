names = ['Mohamed', 'Nader', 'Eman', 'Belal', 'Rola', 'Amr',
         'Sahar', 'Ahmed', 'Morsy', 'Rahma', 'Hossam', 'Hassan', 'Hasan']

for index in range(len(names)):
    name_len = len(names[index])
    if name_len > 5:
        for character in names[index]:
            if character == 'n' or character == 'N':
                print(name_len)

while names != []:
    print(names.pop())
