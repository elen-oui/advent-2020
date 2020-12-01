input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
input_numbers = {int(i) for i in input_lines}

# Part A

for i in input_numbers:
    # what do I add to i to get 2020?
    expected = 2020-i
    if expected in input_numbers:
        print(i * expected)

# Part B
        
for i in input_numbers:
    for j in input_numbers:
        expected = 2020-i-j
        if expected in input_numbers:
            print(i * j * expected)
