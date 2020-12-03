import re

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()

# Part 1

valid_password_counter_a = 0

for line in input_lines:
    match = re.search("(\\d+)-(\\d+) (\\w): (.*)", line)
    lowest, highest, policy_char, password = match.group(1, 2, 3, 4)
    lowest = int(lowest)
    highest = int(highest)
    if lowest <= password.count(policy_char) <= highest:
        valid_password_counter_a += 1

print(valid_password_counter_a)

# Part 2

valid_password_counter_b = 0

for line in input_lines:
    match = re.search("(\\d+)-(\\d+) (\\w): (.*)", line)
    position_a, position_b, policy_char, password = match.group(1, 2, 3, 4)
    position_a = int(position_a)
    position_b = int(position_b)

    if (password[position_a-1] == policy_char) != (password[position_b-1] == policy_char):
        valid_password_counter_b += 1
        print(line)

print(valid_password_counter_b)
