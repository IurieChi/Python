
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
	

# year_type()
test()
