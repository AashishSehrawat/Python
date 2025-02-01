# Q1: Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
# age = int(input("Enter your age: \n" ))
# if age < 13:
#     print("Child")

# if age >= 13 and age <=19:
#     print("teen")

# if age >= 20 and age <= 59:
#     print("adult")

# if age >= 60:
#     print("Old")


# Q2: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday. 
# day = "Wednesda"
# age = 45
# if day == "Wednesday":
#     if age >= 18:
#         print("Price of ticket is 10$")
#     else:
#         print("Price is 6$")
# else:
#     if age >= 18:
#         print("Price of ticket is 12$")
#     else:
#         print("Price is 8$")



# Q3: Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F(below 60).
# score = 96
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")



# Q4: Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
# color = "Green"
# condition = ""
# if color == "Green":
#     condition = "Unripe"
# elif color == "Yellow":
#     condition = "Ripe"
# elif color == "Brown":
#     condition = "Over-ripe"
# else: 
#     print("Enter correct details")
#     exit()
# print(condition)



# Q5: Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
# distance = 12
# if distance < 3:
#     mode = "Walk"
# elif distance <15:
#     mode = "Bike"
# else: 
#     mode = "Car"

# print(mode)




# Q6: Problem: Customize a coffee order: 'Small", "Medium", or •Large" with an option for "Extra shot" of espresso.
# order = "small"
# extra_shot = True

# if extra_shot:
#     if order == "small":
#         order = "small"  
#     elif order == "medium":
#         order = "medium"
#     elif order == "large":
#         order = "large"
#     print("Extrashot with " + order)
# else:
#     if order == "small":
#         order = "small"  
#     elif order == "medium":
#         order = "medium"
#     elif order == "large":
#         order = "large"
#     print(order)



# Q7: Problem: Check if a password is "Weak•, "Medium•, or •Strong". Criteria: < 6 chars Weak), 6-10 chars (Medium), chars (Strong).
# password = "cgvhbjnhk"
# if len(password) < 6:
#     res = "weak"
# elif len(password) < 10:
#     res = "medium"
# else:
#     res = "strong"
# print(res)



# Q8: Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).
year = 3000
if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print("leap")
else: print("non-leap")


