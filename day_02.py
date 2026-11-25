# for i in range(1 , 11):
#     print(f"{i} * {i} = {i*i}")

# for i in range(10, 0, -1):
#     print(i)

# for i in [1, 2, 3, 4, 5]:
#     print(i)

# tasks
print("Enter a number to know postive or negative: ")
num = int(input())
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else: 
    print("Zero")


print("Enter three numbers to know the largest one: ")
a = int(input())
b = int(input())
c = int(input())
if(a > b) and (a > c):
    print(f"{a} is the largest number")
elif(b > a) and (b > c):
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")


print("Enter your subject mark: ")
mark = int(input())
if mark >= 80:
    print("Grade A+")
elif mark >= 75:
    print("Grade A")
elif mark >= 70:
    print("Grade A-")
elif mark >= 65:
    print("Grade B+")
elif mark >= 60:
    print("Grade B")
elif mark >= 55:
    print("Grade B-")
elif mark >= 50:
    print("Grade C")
elif mark >= 45:
    print("Grade D")
elif mark >= 40:
    print("Grade E")
else:
    print("Fail")


print("Even numbers between 1 to 100 are: ")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
    

print("Enter number of multiplication table: ")
val = int(input())
for i in range(1, 11):
    print(f"{val} * {i} = {val*i}")



print("Enter value of N to get sum from 1 to N: ")
num1 = int(input())
sum = 0
for i in range(1, num1 + 1):
    sum += i
print(f"Sum of numbers from 1 to {num1} is: {sum}")


print("--------Password Verification System--------")
print("Enter your password: ")
password = input()
print("Enter your password again: ")
password2 = input()
if password == password2:
    print("Password matched")
else:
    print("Password not matched")




print("Enter the number you want to count digits: ")
num3 = int(input())
count = 0
while num3 != 0:
    num3 //= 10
    count += 1
print(f"Number of digits: {count}")


mail = "azmaeen@gmail.com"
pass3 = "123456@abc"
print("Your Mail: azmaeen@gmail.com")
print("Your Password: 123456@abc")
print("----------Login----------")
print("Enter your mail: ")
mail_input = input()
print("Enter your password: ")
password_input = input()
if pass3 == password_input and mail_input.lower() == mail.lower():
    print("Login successful")
else:
    print("Login failed")




# menu driven calculator
while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please try again.")

