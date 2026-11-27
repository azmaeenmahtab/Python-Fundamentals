# day 04 tasks
# modules
import random as r
import datetime as dt
import os #helps python to interact with the operating system
import json


def add(a, b):
    return a + b

def is_even(num):
    return num % 2 == 0

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def largest_of_list(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


def unique_ticket_id():
    timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")

    random_number = r.randint(1000, 9999)

    unique_id = f"{timestamp}{random_number}"

    return unique_id


def current_date_time():
    now = dt.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculator(a, b, operation):
    if operation == '+':
        return add(a, b)
    elif operation == '-':
        return subtract(a, b)
    elif operation == '*':
        return multiply(a, b)
    elif operation == '/':
        return divide(a, b)
    else:
        raise ValueError("Invalid operation. Choose from '+', '-', '*', or '/'.")


def search_by_id(id, data):
    for item in data:
        if item.get('id') == id:
            return item
    return None


print("\n summation of two numbers")
sum_result = add(5, 3)
print(f"Sum: {sum_result}\n")

print("\n check if a number is even")
is_even_result = is_even(4)
print(f"Is 4 even? {is_even_result}\n")


print("\n get grade based on score")
grade_result = grade(85)
print(f"Grade for score 85: {grade_result}\n")


print("\n find the largest number in a list")
largest_result = largest_of_list([3, 5, 2, 8, 1])
print(f"Largest number in the list: {largest_result}\n")


print("\n generate a unique ticket ID")
ticket_id = unique_ticket_id()
print(f"Unique Ticket ID: {ticket_id}\n")


print("\n get current date and time")
current_time = current_date_time()
print(f"Current Date and Time: {current_time}\n")


print("\nto use calculator , call calculator(a, b, operation) where operation can be '+', '-', '*', or '/'.\n")
calculator_result = calculator(10, 5, '+')
print(f"Calculator Result (10 + 5): {calculator_result}\n")


print("\nsearch for an item by ID in a list of dictionaries")
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]
search_result = search_by_id(2, data)
if search_result:
    print(f"Item found: {search_result}\n")
else:
    print("Item not found.\n")


print("\n module ends here\n")




# -----------------------------basics------------------------------



r.randint(1, 10)
r.random() # picks a random float between 0 and 1
r.choice(['a', 'b', 'c', 'd']) # picks a random element from a list
r.shuffle(['a', 'b', 'c', 'd']) # shuffles a list in place means original list is changed

now = dt.datetime.now() # returns current date and time
today = dt.date.today() # returns current date

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

formatted = now.strftime("%d-%m-%Y")

current_directory = os.getcwd() # returns the current working directory
files = os.listdir(current_directory) # returns a list of files and directories in the current working directory
os.mkdir("new_directory") # creates a new directory in the current working directory

if os.path.exists("new_directory"): # checks if a directory exists
    print("Directory exists")

file_path = os.path.join(current_directory, "new_directory") # joins the current directory path with the new directory name

# python dictionary
student = {
    "name": "Azmaeen",
    "age": 21,
    "department": "CSE"
}

json_string = json.dumps(student) # converts python dictionary to json string

student_dict = json.loads(json_string) # converts json string back to python dictionary

