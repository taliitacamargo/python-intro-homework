names = ["Aiko", "Devon", "Priya", "Marcus", "Sara", "Luis", "Mia"]

search_name = input("Enter a name to search for: ")

found_index = -1
for i in range(len(names)):
    if names[i] == search_name:
        found_index = i
        break

if found_index == -1:
    print(f'"{search_name}" was not found in the list.')
else:
    print(f'Found "{search_name}" at index {found_index}.')
