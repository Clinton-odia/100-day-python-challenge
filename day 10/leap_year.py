def is_leap_year(year):
    """ take a year and check if it is a leap year or not"""
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

    

answer = (is_leap_year(2001))
print(answer)
            