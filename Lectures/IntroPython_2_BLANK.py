# Class Activities (Lecture 2)

## Some examples about input("some message"), int(), and int(input())
# input("some message"):
classname = input("What is this class? ")
print("This class is ", classname)

# int()
num_5 = int('5') # convert '5' to 5
num_6 = int('6') # convert '6' to 6
total_num = num_5 + num_6 # calculate the sum
print("The total number is: ", total_num)

# int(input()): convert user input number into an integer number
user_input_number = int(input("Please type in a whole number: "))
print(user_input_number)  


## TODO: Below are in-class exercise for Lecture 2
'''
1: Create a variable called number_of_units and assign 3 to it
    Then in the next line, print out number_of_units
'''



'''
2: What's wrong with the following lines of code? can you fix it?
print out the student's name by using its variable
'''
# 2ndStudent = "Jane" # uncomment the code to see what's happened?



'''
3. The code below calculates the area of a triangle. Add comments to 
each line explaining what it is doing.
'''
base = 10
height = 3
area = base * height
area = area/2
print("The triangle area is", area)
