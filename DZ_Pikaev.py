
with open('webinartest.txt', mode='r', encoding='utf8') as op_fl:
    numbers = []
    num = ''
    for elem in op_fl:
        for char in elem:
            if char.isdigit():
                num += char

            else:
                if len(num) != 0:
                    numbers.append(int(num))
                    num = ''


with open('new_list.txt', mode='w', encoding='utf8') as new_file:
    new_file.write(str(numbers))
