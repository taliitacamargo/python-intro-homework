# not true becomes false first. then we have false and false, 
# an and expression can only be true if both sides are true
# therefore this prints false.
print(not True and False)

# false and false becomes false because both values need to be true. 
# true or false and or is true if one side is true, so the command prints true
print(True or False and False)

# first it runs the expression inside the parenthesis, which would print true, however
# the not flips the result to false, therefore it prints false
print(not (5 > 3))

# for the first half of the expression it would print true, however
# the fact that 4 does = 4, flips the result to false, because both 
# need to be true for the final result to be true
print(10 == 10 and 4 != 4)

# not false would print true, and not true would print false because the first half
# prints true, for the final result to be true, we need at least one side to be true
# therefore this prints true
print(not False or not True)
