input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_numbers = {int(i) for i in input_lines}
for i in input_numbers:
    diff = 2020-i
    if diff in input_numbers:
        print(i * diff)
