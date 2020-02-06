from datetime import datetime

def check_birthdate(year, month, day):
    birthdate = datetime(year, month, day)
    today = datetime.now()
    if birthdate > today:
        return False
    else:
        return True

def calculate_age(year, month, day):
    birthdate = datetime(year, month, day)
    today = datetime.now()
    days = (today-birthdate).days

    print("You are %d years old." % (int(days)/365))

def main():
    year = int(input("Enter year of birth: "))
    month = int(input("Enter month of birth: "))
    day = int(input("Enter day of birth: "))

    if check_birthdate(year, month, day):
        calculate_age(year, month, day)
    else:
        print("Invalid birthdate. Please try again.")

if __name__ == '__main__':
    main()


if __name__ == '__main__':
	main()
