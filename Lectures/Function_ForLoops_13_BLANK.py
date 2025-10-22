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




'''
3. Write a function 'power' that accepts two inputs: exponent and base.
The exponent should have a default value of 0.5 (square root)
The function should return the result of base to the power of exponent

When using the function to calculate exponent, for example, 
    exponent = 3, base = 2  ===> 8 (because 2 to the power of 3 is 8)
    base = 4  ===> 2.0 (because 4 to the power of 0.5 is the square root of 4)
'''
# write your code below




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
