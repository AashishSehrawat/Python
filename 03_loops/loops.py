# Q1: Given a list of numbers, count how many are positive.
# numbers = [1,5,-2,-45,56,23,-56,-9]
# count = 0
# for x in numbers:
#     if x>0:
#         count = count+1

# print(count)




# Q2: Problem: Calculate the sum of even numbers up to a given number n.
# n = 10
# sum = 0
# for num in range(1,n+1):
#     if num%2 == 0:
#         sum += num
# print(sum)


# Q3: Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
# number = 2
# for x in range(1,11):
#     if x == 5: continue
#     print(number*x)



# Q4: Problem: Reverse a string using a loop.
# str = "jaatman"
# rev = ""
# for i in range(0, len(str)):
#     rev += str[len(str)-i-1]
# print(rev)



# Q5: Problem: Given a string, find the first non-repeated character.
# input = "teeter"
# for ch in input:
#     if input.count(ch) == 1:
#         print(ch)
#         break



# Q6: Problem: Compute the factorial of a number using a while loop.
# num = 5
# ans = 1
# for x in range(1, num+1):
#     ans *= x
# print(ans)



# Q7: Problem: Keep asking the user for input until they enter a number between 1 and 10.
# while True:
#     number = int(input("Enter the number: \n"))
#     if 1 <= number <= 10:
#         break




# Q8: Problem: Check if a number is prime.
# number = 4
# count = 0
# i = 1
# while i <= number:
#     if number%i == 0:
#         count += 1
#     if count > 2:
#         print("Non-Prime")
#         break
#     i += 1
# if i == number+1: print("Prime")



# Q9: Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange"]
# for ch in items:
#     if items.count(ch) >= 2:
#         print("Duplicates")
#         break



# Q10: Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time

attempts = 0
max_attemp = 5
wait_time = 1

while attempts < max_attemp:
    print(attempts+1 ," ", wait_time)
    attempts += 1
    wait_time *= 2
 


 # ----------------------------------------------------------------------------------------

