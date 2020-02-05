from datetime import datetime

def check_birthdate(year, month, day):
	currentYear = datetime.now().year
	if year >= currentYear :
		print("the birthdate is invalid")
		return False
	else:
		calculate_age(year,month,day)
		return True

def calculate_age(year, month, day):
    # write code here
	currentYear = datetime.now().year

	age = currentYear - year
	print("You are : " + str(age) + " years old")


def main():
	# write main code here
	bYear = int(input("Enter year of birth : "))
	bMonth = int(input("Enter month of birth : "))
	bDay = int(input("Enter day of birth : "))
	check_birthdate(bYear,bMonth,bDay)



if __name__ == '__main__':
	main()
