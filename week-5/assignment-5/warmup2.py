while True:
    user_input = input("Enter a positive integer: ")

    if user_input.isdigit() and int(user_input) > 0:
        print(f'Got it: {int(user_input)}')
        break

    print("That's not a positive integer. Try again.")
