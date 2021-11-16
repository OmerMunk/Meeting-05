######################################################


# # Rock Paper Scissors Exercise

# Import the random package, which needs to be used in this program
import random

print("Welcome! Lets see you beat me in Rock Paper Scissors.")

# Setting the possible choices
# each number represent a choice: (for the program to be user friendly)
# 1 = rock, 2 = paper, 3 = scissors
choices = ["1", "2", "3"]

# Randomize the cpu choice.
random.shuffle(choices)

# setting the cpu choice to be the first number on the list of choices.
cpu = choices[0]

rounds = int(input("How many rounds do you want play?"))

# Initializing the amount of wins.
count_cpu = 0
count_human = 0

# Repeat the amount of games the user chose
for i in range(rounds):
    print(f"Round {i+1}:")
    human = input("choose a numbber: 1 = rock"
                  "2 = paper"
                  "3 = scissors")
    # check if the input is valid
    while human != "1" and human != "2" and human != "3":
        human = input("your input is invalid, please try again"
                      "choose a number: 1 = rock"
                                       "2 = paper"
                                       "3 = scissors")

    # Randomizes the choice of the cpu before each round
    random.shuffle(choices)
    cpu = choices[0]

    if human == cpu:
        print("tie!")
        continue

    if human == "1" and cpu == "2":
        print("cpu wins")
        count_cpu += 1
        continue

    if human == "1" and cpu == "3":
        print("you win")
        count_human += 1
        continue

    if human == "2" and cpu == "1":
        print("you win")
        count_human += 1
        continue

    if human == "2" and cpu == "3":
        print("cpu wins")
        count_cpu += 1
        continue

    if human == "3" and cpu == "1":
        print("cpu wins")
        count_cpu += 1
        continue

    if human == "3" and cpu == "2":
        print("you win")
        count_human += 1
        continue

print(f"The result is: You - {count_human}, computer - {count_cpu}")

##################################################################


# # An example of how to replace a char in a string
name = "omer"
name = name.replace('m', 'M')
print(name)

###############################################################

# #Dates exercies

print("""This program gets 10 dates from the user in the format dd.mm.yyyy.
and then prints the amount of dates in each season, and prints them divided by seasons""")

# setting the index of monthes for each season
autumn_monthes = (1, 2, 3)
spring_monthes = (4, 5, 6)
summer_monthes = (7, 8, 9)
winter_monthes = (10, 11, 12)


maximum_month = (12)
minimum_month = (1)
maximum_day = (31)
minimum_day = (1)

# Setting an empty lists, which will be filled with dates, if entered.
winter_dates = []
spring_dates = []
summer_dates = []
autumn_dates = []

# iterating the 10 dates entered by the user
for i in range(10):
    date = input(f"Please enter the {i+1} date")

    # replaces " / " with a " . "
    date = date.replace('/','.')

    # If " . " does not exist in the date, a will be -1
    a = date.find(".")

    # Slpit's the string type of date, to a list, where the day, month, and year, are seperated.
    # in order to acces a speific part of the date.
    date_list = date.split(".")

    # checking if the date ie valid
    while a == -1 or  int(date_list[1]) < minimum_month or int(date_list[1]) > maximum_month \
            or int(date_list[0]) > maximum_day or int(date_list[0]) < minimum_day:
        date = input("Invalid input, try again.")
        date = date.replace('/', '.')
        a = date.find(".")
        date_list = date.split(".")

    # spliting again the valid date (if was invalid)
    date_list = date.split(".")

    # filters the date according to the season.
    # Then insert the date to the matching season list
    if int(date_list[1]) in autumn_monthes:
        autumn_dates += [date]
        continue
    if int(date_list[1]) in spring_monthes:
        spring_dates += [date]
        continue
    if int(date_list[1]) in summer_monthes:
        summer_dates += [date]
        continue
    if int(date_list[1]) in winter_monthes:
        winter_dates += [date]
        continue

# Output
season_dates = [autumn_dates, spring_dates, summer_dates, winter_dates]
season_names = ["autumn", "spring", "summer", "winter"]
for i, season in enumerate(season_dates):
    if len(season) > 0:
        print(f"You entered {len(season)} {season_names[i]} dates. The dates are: {season}")

#########################################################################################

An axample of how to "clean" words from non-letter chars and replace multiple spaces with one.

s= "ggjdrtiytu68@@       @@@@@@@ddfDDS   ''''##f     f f           f##"
filter_str= ''
for char in s:
    if ord(char) >= 97 and ord(char) <= 122 or ord(char)>= 65 and ord(char) <= 90 or (char == " ") :
        filter_str+= char
(filter_str.split())
filter_str = ' '.join(filter_str.split())

print (filter_str)

#####################################################################################

# An example of how to replace multiple spaces with one
myString = "a         b a "
filter_str = ' '.join(filter_str.split())
print(myString)

################################################################################

# An example of a stock data stored in dictionary.

stocks_dict = {
    "TSLA" : {
         "company name": "Tesla",
         "ticker": "TSLA",
         "Employees num": "5000",
         "address": "california",
         "CEO": "eilon mask",
         "stocks data": {
              "14.11.2021": {
                   "open price": "1001.5",
                   "close price": "1020",
                   "volume" : "50000000"
              },
              "15.11.2021": {
                   "open price": "1067.7",
                   "close price": "1045.5",
                   "volume" : "45000345"
              }
         }
     }
}
print(stocks_dict["TSLA"]["stocks data"]["15.11.2021"])

##########################################################################

# Birthday exercise

# setting the options of the main manu for the user
options = ("Insert", "Look Up", "Quit")

print( "Welcome to your \"People Birthday Manager\"")

# creating an empty dictionary.
birthday_dict= {}

# Creating an infinite while loop until the user type Quit
while True:
    print("""Choose mode:
                   Insert
                   Look up
                   Quit""")
    mode = str(input().title()) #make sure only the first letter of each word will be capital

    if mode == "Quit":
        print("See you Later!!")
        exit()         #terminate the program when the user chose quit.

    if mode not in options:
         print("Invalid mode, try again please:")

    if mode == "Insert":
        name = input("Enter the name of the person you want to add").title()
        date = input(f"Enter the birthday date of {name}'s birthday")

        # checking if the name is already in the a dictionary key
        if name in birthday_dict.keys():
            print("Name already exist, choose 1 to overwrite, choose 2 to cancel")
            answer = int(input())
            while answer != 1 and answer != 2:
                print("invalid answer, choose 1 to overwrite, choose 2 to cancel" )
                answer = int(input())
            if answer == 1:
                birthday_dict[name] = date #overwriting
            else:
                print("Canceled, back to the main memu")
                continue
        else:
            birthday_dict[name] = date
        continue

    elif mode == "Look Up":
        name = input("Enter the name you want to look for").title()
        if name in birthday_dict.keys():
            print(f"{name}'s birthday is on {birthday_dict[name]}")
        else:
            print(f"The birthday manager could not find {name}'s birthday")
            print("Would you like the birthday manager to look for suggestions? 1 - yes, 2 - no")
            answer = int(input())
            while answer != 1 and answer != 2:
                print("invalid answer. Would you like the birthday manager to look for suggestions? 1 - yes, 2 - no")
                answer = int(input())
            if answer == 1:
                count = 0
                for key in birthday_dict.keys():
                    if name in key:
                        count += 1
                        print(f"suggustion {count}: {key} : {birthday_dict[key]}")
                if count == 0:
                    print("Im sorry, no suggestions")
            else:
                print("Back to the main memu")
                continue
        continue

#######################################################################################################

# Examples of set options

my_set1 = set((1,2,3))
my_set2 = set((2,3,4))
my_set3 = set()
print(my_set1.union(my_set2))
print(my_set1.difference(my_set2))
print(my_set1.intersection(my_set2))
print(my_set1.symmetric_difference(my_set2))
# print(my_set1.clear())
# print(my_set1.pop())
# print(my_set1)
print(my_set1.issubset(my_set2))
print(my_set3.issubset(my_set1))
print(my_set1.__contains__(4))
print(my_set1.__contains__(3))
print(my_set1.__hash__)
print(my_set1)
print(my_set1.__init_subclass__())
print(my_set1<my_set2)
print(my_set1 | my_set2)
aliasing
a = [1, 2, 3]
b = a
a[0] = 0
print(b)

##########################################################################################

#unique food manager

# gets as an input: all the food a person eats in one day
# gives back the number of unique food - the food that has been eaten only once
print("Welcome to the unique food manager")
food_set = set()
print("Just insert the names of the foods you eat today, when you go to sleep, enter the magic word - $$$")
food = str(input("What did you eat?"))
count =0
while food != "$$$":
    count+=1
    if food in food_set:
        count-=1
    food_set.add(food)
    food = str(input("What did you eat?"))
print(f"You ate {count} unique foods today")










