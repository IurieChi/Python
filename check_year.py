
# As you surely know, due to some astronomical reasons, years may be leap or common. 
# The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

def year_type():
	year = int (input('Enter year: '))
	if year <1582:
		print('Not within the Gregorian calendar period')
	else:
		if year % 4 !=0:
			print(f"{year} is a common year")
		elif year % 100 != 0:
			print(f"{year} is a leap year")
		elif year % 400 != 0:
			print(f"{year} is a common year")
		else:
			print(f"{year} is a leap year")

		    

# function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
def is_year_leap(year):
	if year < 1582:
			print('Not within the Gregorian calendar period')
	else:
		if year % 4 !=0:
			return False
		elif year % 100 != 0:
			return True
		elif year % 400 != 0:
			return False
		else:
			return True
	# Test data
def test():
	for i in range(len(test_data)):
		yr = test_data[i]
		print(yr,"-> ",end="")
		result = is_year_leap(yr)
		if result == test_results[i]:
			print("OK")
		else:
			print("Failed")
	
def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
def month():
	for i in range(len(test_years)):
		yr = test_years[i]
		mo = test_months[i]
		print(yr,mo,"-> ",end="")
		result = days_in_month(yr, mo)
		if result == test_results[i]:
			print(test_results[i])
		else:
			print("Failed")

def day_of_year(year, month, day):
    #function takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of 
	# the year, or returns None if any of the arguments is invalid.
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(f'Day number {day_of_year(1987, 5, 31)}')

# year_type()
# test()
month()
