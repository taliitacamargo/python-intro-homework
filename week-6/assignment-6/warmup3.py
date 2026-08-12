# Example 1: a variable defined inside a function is local to that function
def show_local():
    local_var = "I'm local to this function"
    print(local_var)

show_local()

# print(local_var)
# NameError: name 'local_var' is not defined


# Example 2: return solves the problem
def get_value():
    local_var = "I'm local to this function"
    return local_var

outer_var = get_value()
print(f"Outer: {outer_var}")
