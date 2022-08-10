import datetime  # Importing the datetime module which allows us to access today's date

if datetime.date.today().day < 15:
    print("It's the beginning of the month still!")
else:
    print("It's not the beginning of the month anymore :(")

