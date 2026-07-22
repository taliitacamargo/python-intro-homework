day = input('What day is it? ').lower()
time = input('What time is it? ').lower()



weekday = ['monday', 'tuesday', 'saturday']
daylight = ['morning', 'afternoon', 'evening']


if day not in weekday and time not in daylight:
    print("I don't recognize that day or that time. "
          "Please use days like monday, tuesday, or saturday "
          "and times like morning, afternoon, or evening.")
elif day not in weekday: 
    print("I don't recognize that day. "
          "Please use days like monday, tuesday, or saturday.")
elif time not in daylight: 
    print("I don't recognize that time. "
          "Please use times like morning, afternoon, or evening.")
else: 

    if day == "monday" and time == "morning":
        print("Suggestion: Time to get some breakfast and get ready to work! " \
    "have a great and productive day")
    elif day ==  "monday" and time == "afternoon":
        print('Suggestion: Great time to review for your upcoming exams.')
    elif day == "monday" and time == "evening":
        print('Suggestion: Get some dinner and prepare for bed, good night!')


    elif day == "tuesday" and time == "morning":
        print('Suggestion: Morning class, get ready for another amazing day!')
    elif day == "tuesday" and time == "afternoon":
        print('Suggestion: Tackle another small task, finish that coding exercise.')
    elif day == "tuesday" and time == "evening":
        print("Suggestion: Wind down with a nice cup of tea and your favorite book.")

    elif day == "saturday" and time == "morning":
        print("Suggestion: It's finally the weekend, you can sleep in and take your time today")
    elif day == "saturday" and time == "afternoon":
        print("Suggestion: How about going out for a walk? maybe get some ice cream?")
    elif day == "saturday" and time == "evening":
        print("Suggestion: After an amazing day, it's time to get some rest, good night!")