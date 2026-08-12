def is_valid_score(score):
    if isinstance(score, int) and 0 <= score <= 100:
        return True
    else:
        return False

user_score = int(input("Please enter a score between 0 and 100: "))

if is_valid_score(user_score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")