import datetime


todays_date = str(datetime.date.today().strftime('%d-%m-%Y')).split("-")


entered_date = input("Enter a date in the format dd-mm-yyyy: ").split("-")

age = int(todays_date[2]) - int(entered_date[2])


if (int(entered_date[1]) > int(todays_date[1])):
    age -= 1
elif (int(entered_date[1]) == int(todays_date[1]) and int(entered_date[0]) > int(todays_date[0])):
    age -= 1

print(f"The age of someone born on the day that you entered is {age}")
