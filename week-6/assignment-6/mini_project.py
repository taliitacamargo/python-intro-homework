def find_min(numbers):
    """Return smallest value"""
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


def find_max(numbers):
    """Return largest value"""
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def search(numbers, target):
    found_index = -1

    for i in range(len(numbers)):
        if numbers[i] == target:
            found_index = i
            break

    return found_index


def bubble_sort(numbers):
    sorted_numbers = numbers.copy()
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
                swapped = True

    return sorted_numbers


def show_menu():
    """Shows menu options"""
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    return input("Choose an option (1-5): ")


numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93,
           31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            print(f"Minimum: {find_min(numbers)}")

        elif choice == "2":
            print(f"Maximum: {find_max(numbers)}")

        elif choice == "3":
            target = int(input("Enter a number to search for: "))
            index = search(numbers, target)

            if index == -1:
                print("Not found")
            else:
                print(f"Found at index {index}")

        elif choice == "4":
            print(f"Sorted list: {bubble_sort(numbers)}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("That's not a valid option. Try again.")

        print()


main()