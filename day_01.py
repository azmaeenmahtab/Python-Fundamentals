# practice
# player_name = 'Rafi'
# age2 = 25
# price = 19.99 
# city = 'New York'
# is_active = True
# middle_name = None

# print(f"player name: {player_name}")
# print(type(player_name))

# print("2026", "11", "24", sep="-", end="   !\n")

# name1 = input("enter your name: ")
# age1 = input("enter your age: ")

# converted_age = int(age1)


# day - 01 - task

name = input("enter your name: ")
age = int(input("enter your age: "))

print(f"user name : {name}")
print(f"user age : {age}")

num1 = 100
num2 = 50

addition = num1 + num2
subtraction = num1 - num2
division = num1 / num2
multiplication = num1 * num2

celcius = 37
farhenheit = (celcius * 9/5) + 32

num3 = 35
is_even = num3 % 2 == 0


sub1 = 78
sub2 = 87
sub3 = 80
total_marks = sub1 + sub2 + sub3
average_marks = total_marks / 3


len = 5
height = 10
area = len * height


money = 3506
thousand_count = 0
five_hundred_count = 0
one_hundred_count = 0
fifty_count = 0
twenty_count = 0
ten_count = 0
five_count = 0
two_count = 0
one_count = 0


if money >= 1000:
    thousand_count = money // 1000
    money = money % 1000
if money >= 500:
    five_hundred_count = money // 500
    money = money % 500
if money >= 100:
    one_hundred_count = money // 100
    money = money % 100
if money >= 50:
    fifty_count = money // 50
    money = money % 50
if money >= 20:
    twenty_count = money // 20
    money = money % 20
if money >= 10:
    ten_count = money // 10
    money = money % 10
if money >= 5:
    five_count = money // 5
    money = money % 5
if money >= 2:
    two_count = money // 2
    money = money % 2
if money >= 1:
    one_count = money // 1
    money = money % 1




print("Denomination for the given amount is below: ")
print(f"1000: {thousand_count}")
print(f"500: {five_hundred_count}")
print(f"100: {one_hundred_count}")
print(f"50: {fifty_count}")
print(f"20: {twenty_count}")
print(f"10: {ten_count}")
print(f"5: {five_count}")
print(f"2: {two_count}")
print(f"1: {one_count}")