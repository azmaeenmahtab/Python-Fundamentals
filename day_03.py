# ------------------------tasks-------------------------------
nums = [11, 9, 15, 7, 20, 3, 12, 9, 11, 15]
largest = max(nums)
smallest = min(nums)
print(f"List of numbers: {nums}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")


duplicates_removed = list(set(nums))
print(f"List after removing duplicates: {duplicates_removed}")


sum = 0
for num in nums:
    sum += num
print(f"Sum of all numbers: {sum}")


sentence = "Python is a powerful programming language."
print(f"Sentence: {sentence}")
words = sentence.split()
word_count = len(words)
print(f"Number of words in the sentence: {word_count}")


user_input =  input("Enter a string: ")
print(f"Lowered user input: {user_input.lower()}")


print("creating user profile")
user = {} 
user_name = input("Enter your name: ")
user_email = input("Enter your email: ")
user_age = int(input("Enter your age: "))
user_is_student = input("Are you a student? (yes/no): \n").strip().lower() == "yes"
user["name"] = user_name
user["email"] = user_email
user["age"] = user_age
user["is_student"] = user_is_student
print(f"User profile: {user}\n")


print("updating user profile")
updated_name = input("Enter your updated name: ")
updated_email = input("Enter your updated email: ")
updated_age = int(input("Enter your updated age: "))
updated_is_student = input("Are you still a student? (yes/no): \n").strip().lower() == "yes"
user["name"] = updated_name
user["email"] = updated_email
user["age"] = updated_age
user["is_student"] = updated_is_student
print(f"Updated user profile: {user}")
print()


list_of_students = [
    {
        "name": "Alice",
        "roll_number": 101,
        "department": "CSE",
        "semester": 5
    },
    {
        "name": "Bob",
        "roll_number": 102,
        "department": "EEE",
        "semester": 3
    },
    {
        "name": "Charlie",
        "roll_number": 103,
        "department": "ME",
        "semester": 7
    },
    {
        "name": "David",
        "roll_number": 104,
        "department": "CSE",
        "semester": 5
    },
    {
        "name": "Eve",
        "roll_number": 105,
        "department": "EEE",
        "semester": 3
    }
]
print("List of students: ")
for student in list_of_students:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Department: {student['department']}, Semester: {student['semester']}")

eves_department = list_of_students[4]["department"]
print(f"Eve's department: {eves_department}")


print("Enter the sentence to count the frequency of each word: ")
input_sentence = input()
words = input_sentence.split()
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word frequency:")
for word in word_frequency:
    print(f"{word}: {word_frequency[word]}")

print()


print("filtering numbers greater than 10 from the list")
greater_than_10 = []
for num in nums:
    if num > 10:
        greater_than_10.append(num)
print(f"Numbers greater than 10: {greater_than_10}")















# ------------------------basics-------------------------------
# list
numbers = [1, 2, 3, 4, 5]

# slicing
numbers_slice = numbers[1:4]  
numbers_slice2 = numbers[:3]   
numbers_slice3 = numbers[2:]   
numbers_slice4 = numbers[:] 
# python uses negative index too 
numbers_slice5 = numbers[-1] #last element

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
students.append("Frank") #to the end of the list
students.insert(2, "Grace") #insert at specific index eg. 2

# remove elements by value
students.remove("Bob")
# remove elements by index and return the removed element
removed_student = students.pop(1) 
# by default, pop() removes the last element
removed_last_student = students.pop()


numbers.sort()
numbers.sort(reverse=True) #sort in descending order
numbers.reverse() #reverse the order of the list, it does not sort

len_of_list = len(numbers)

# for i in range(len_of_list): #it prints 0 1 2 index if len is 3
#     print(numbers[i]) 
#     # or
# for student in students:
#     print(student)


# Tuple - once created, cant be modified
cities = ("newyork", 200, 1556500) #tuple can contain different data types
single = (5,) #single element tuple must have a comma
# tuple suports indexing like list
city_name = cities[0]


# Dictionaries
student = {
    "name": "Azmaeen",
    "age": 21,
    "department": "CSE",
    "is_student": True
}
std_name = student["name"]
# cons = if key does not exist, python throws error
# so we use get
std_email = student.get("email", "email not found") #if key does not exist, it returns default value
student["email"] = "azmaeen@gmail.com"
keys = student.keys()
values = student.values()
items = student.items() #returns all key-value pairs

# we can iterate over a dictrionary using key or value
# for key in student:
#     print(key, student[key])

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(key, value)

# remove a key-value using key
removed_value = student.pop("age")

students = {
    "student1": {
        "name": "Rahim",
        "age": 21,
        "department": "CSE"
    },

    "student2": {
        "name": "Karim",
        "age": 22,
        "department": "EEE"
    }
}

karims_department = students["student1"]["department"]
# empty dictionary
empty_dict = {}


# sets - unordered collection of unique elements
names = {"Alice", "Bob", "Bob", "Charlie", "David", "Eve"} #duplicates are removed automatically
# empty set
empty_set = set()

#easy way to remove duplicates from a list and return a list
unique_names = list(set(names))

#does not rely on order of a set, sets are unordered
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
combined_set = A.union(B)  
intersection_set = A.intersection(B)  


# strings
name = "Azmaeen"
first_char = name[0]
sliced_name = name[1:5]
name.strip() #removes begining and ennding whitespace
text = "Hello, World!"
splitted_text = text.split(",") 

text2= "I love JavaScript, Python, and C++"
text2.replace("JavaScript", "Java")
position = text2.find("Python") #if substring doen not exist, returns -1

name.startswith("Az") #returns True
name.endswith("een") #returns True