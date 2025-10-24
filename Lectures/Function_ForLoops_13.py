# Class Activities (Lecture 13)

## Practice functions with default arguments
'''
1. Write a function called 'simple_greeting' that takes a name and an age as input parameters.
The age has a default value of 20.
The function should return a string in the format: "Hello, [name]. You are [age] years old." 
For example, when involking the function, you should see
    print(simple_greeting(name = "Alice")) ==>  "Hello, Alice. You are 20 years old."
    print(simple_greeting(name = "Bob", age = 30))  ==> "Hello, Bob. You are 30 years old."
'''
# write your code below
# solution 1:
def simple_greeting(name, age = 20):
    message = f"Hello {name}. you are {age} years old." # f-string is a special type of string
    return message

# soluton 2
# def simple_greeting(name, age = 20):
#     message = "Hello " + name + ". You are " + str(age) + " years old." # construct a string using addition operators
#     return message

my_message = simple_greeting(name="Bob", age=30)
print(my_message)



'''
2. Write a function 'triangle_area' that computes the area of a triangle 
using its base and height (input parameters) and returns the area.
Both the base and height should have default values of 1.
When using the function, you should see
   print(triangle_area())  ===> 0.5
   print(triangle_area(base = 10, height = 5))  ===> 25.0
Hint: area = 0.5 * base * height
'''
# write your code below
def triangle_area(base = 1, height = 1):
    area = 0.5 * base * height
    return area

print(triangle_area())
print(triangle_area(base=10, height=5))



'''
3. Write a function 'power' that accepts two inputs: exponent and base.
The exponent should have a default value of 0.5 (square root)
The function should return the result of base to the power of exponent

When using the function to calculate exponent, for example, 
    exponent = 3, base = 2  ===> 8 (because 2 to the power of 3 is 8)
    base = 4  ===> 2.0 (because 4 to the power of 0.5 is the square root of 4)
'''
# write your code below
def power(base, exponent = 0.5):
    answer = base ** exponent
    return answer

print(power(base = 2, exponent = 3))
print(power(base = 4 ))



## Practice functions with for loops
'''
4. Write a function 'upperCounter' that takes a string, my_str, as input and 
count the number of characters that are uppercases.
Set 'HELICOPTER' as default argument for my_str.
The function should return (NOT PRINT) a message (string) in the format: 
    "[my_str] has [counter] number of uppercase characters." 

When calling the function, for example, 
print(upperCounter())    ===> "HELICOPTER has 10 uppercase characters."
print(upperCounter(my_str = "A Beautiful Day!"))     ===> "Beautiful Day! has 2 uppercase characters."

Hint: 
- Use for loop to iterate the input string and count the number of uppercases 
    using string method ".isupper()" -> review Lecture 9: String Methods.
- Use a counter variable, counter, to count the number of uppercases using a for-loop.
- Use function str() to convert a number (e.g., 5) into a string (e.g.,'5').
- Use addition operations to construct the message by adding strings together.
    e.g, 'a' + 'b' => 'ab'
'''
# write your code below
# solution 1:
# def upperCounter(my_str = "HELICOPTER"):
#     count = 0
#     for char in my_str:
#         if char.isupper() == True:
#             count += 1

#     string = f"{my_str} has {count} number of uppercase characters." 
#     return string

# soluton 2
def upperCounter(my_str = "HELICOPTER"):
    count = 0
    for i in range(len(my_str)):
        if my_str[i].isupper() == True:
            count += 1
            
    string = f"{my_str} has {count} number of uppercase characters." 
    return string

print(upperCounter())
print(upperCounter(my_str = "A Beautiful Day!"))

'''
5. Define a function, sum_of_n, that takes an integer, n, as input.
The function should return the sum of all integers from 1 to n, inclusive.
Default value of n is 1.
When calling the function and plugging in 4 as the argument, for example,
    print(sum_of_n(n = 4))  ===> 10  (because 1 + 2 + 3 + 4 = 10)
Hint:
    use range() to generate the sequence of number from 1 to n.
    use a for loop to iterate the range() and add each number up.
'''
# write your code below
def sum_of_n(n):
    sum_num = 0
    for i in range(1, n+1, 1):
        sum_num += i

    return sum_num

print(sum_of_n(n = 4))