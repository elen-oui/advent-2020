map_locations = []

with open('input.txt', 'r') as f:
    for line in f:
        map_locations.append(line)

def get_tree_counts(right, down, locations):
    max_row_length = len(max(map_locations, key=len))
    tree_count = 0
    column = right
    for row in range(down, len(locations), down):
        if locations[row][column] == '#':
            tree_count += 1
        column = (column + right) % (max_row_length-1)
    return tree_count

print(get_tree_counts(1, 1, map_locations) *
      get_tree_counts(3, 1, map_locations) *
      get_tree_counts(5, 1, map_locations) *
      get_tree_counts(7, 1, map_locations) *
      get_tree_counts(1, 2, map_locations))

