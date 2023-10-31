#Try, except
age = 0
validated = False
while not validated or age < 14:
    try:
        age = int(input("Please enter your age: "))
        validated = True
    except ValueError:
        print("You've entered a wrong value.")

if age > 0:
    print(f"Your are {age} years old")



#validating_integers
print("Welcome to the times table quiz")
print("Enter a times table that you would like to be tested on:")

times_table = int(input())


print("Enter the maximum value for your times table: ")
max_value = int(input())
max_value = max_value + 1
answer = 0
print(f"Here is your quiz on the {times_table} times table")
for x in range(1, max_value):
    answer = x * times_table
    print(f"{x} times {times_table} is ...")
    print("Answer:")
    user_answer = int(input())
    if user_answer == answer:
        print("Correct")
    else:
        print("Incorrect")
