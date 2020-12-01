input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_numbers = {int(i) for i in input_lines}

for i in input_numbers:
    # what do I add to i to get 2020?
    expected = 2020-i
    if expected in input_numbers:
        print(i * expected)
