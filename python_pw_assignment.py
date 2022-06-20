##### Question 1 #####
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.


# I'm not ~trying~ to be pedantic, but the instructions were slightly on the ambiguous side, when considering that every case matters with coding. It can be read two ways, so I'll just do them both.

# I'm going to follow them according the "spirit of the law" first:

def hello_name(user_name):
    """Prints a greeting based on input."""
    print(f"Hi {user_name.title()}!")

hello_name('sydney')

# The below is if I'm following instructions to the "letter of the law":

def hello_name(user_name):
    """Prints 'hello_' and the upper of the input."""
    print(f"hello_{user_name.upper()}!")

hello_name('sydney')


print('\n') # I've added these breaks just to help readability on the output

##### Question 2 #####
# Write a Python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    """Prints only the odd numbers from 1-100."""
    for value in range(1,101,2):
        print(value, end=" ")
    return 'nothing' # again, just following the instructions specifically

print(first_odds())


print('\n')

##### Question 3 #####
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """Prints the max number of a given list."""
    print(max(a_list))

max_num_in_list([5, 83, 41, 0, 2389, 617])


print('\n')

##### Question 4 #####
# Write a funtion to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
# The return should be boolean type.

def is_leap_year(year):
    """Confirms if the given year is a leap year."""

    if (year % 400 == 0) and (year % 100 == 0):
        print(f"The year {str(year)} is a leap year.")
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"The year {str(year)} is a leap year.")
        return True
    else:
        print(f"The year {str(year)} is not a leap year.")
        return False

print(is_leap_year(2000))
print(is_leap_year(2020))
print(is_leap_year(2022))
print(is_leap_year(2100))


print('\n')

##### Question 5 #####
# Write a function to check to see if all numbers in a list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean type.

def is_consecutive(a_list):
    """Confirms whether numbers in the list are consecutive."""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

print(is_consecutive(a_list = [9,7,5,3,1,2,4,6,8]))
print(is_consecutive(a_list = [9,7,3,1,2,4,6]))