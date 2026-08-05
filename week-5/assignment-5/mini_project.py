numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        smallest = numbers[0]
        for number in numbers:
            if number < smallest:
                smallest = number
        print(f'Minimum: {smallest}')

    elif choice == "2":
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        print(f'Maximum: {largest}')

    elif choice == "3":
        target = int(input("Enter a number to search for: "))
        found_index = -1
        for i in range(len(numbers)):
            if numbers[i] == target:
                found_index = i
                break

        if found_index == -1:
            print(f'{target} was not found in the list.')
        else:
            print(f'Found {target} at index {found_index}.')

    elif choice == "4":
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True
        print(f'Sorted list: {numbers}')

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("That's not a valid option. Try again.")

    print()
