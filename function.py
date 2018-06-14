#Question 1: Create a function to calculate the area of a circle by taking radius from user.
x = float(input("Enter radius of circle : "))
def area(x):                            #Defining the function
    a = 3.14*x*x
    print("Area of circle is : ")
    print(a)
area(x)                                 #Calling of function


#Question 2:Write a function “perfect()” that determines if parameter number is a perfect number.
# Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
def perfect():
    for Number in range(1, 1000):
        Sum = 0
        for n in range(1, Number - 1):
            if(Number % n == 0):
                Sum = Sum + n
        if( Sum == Number):
            print(Number)
perfect()


#Question 3:Print multiplication table of 12 using recursion.

def table(n, i=1):
    print (n*i)
    if i != 10:
        table(n,i+1)
table(12)


#Question 4: Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(a,b):
    if b == 1:
        return a
    else:
        return a * power(a,b-1)
x = int(input("Enter a number : "))
y = int(input("Enter it's power : "))
print (power(x,y))


#Question 5: Write a function to find factorial of a number but also store the factorials calculated in a dictionary.

a = {}
def factorial(fact):
    if fact==0 or fact==1:
        return 1
    else:
        return fact * factorial(fact - 1)
for i in range(5):
        f = float(input("Enter a number : " ))
        print(factorial(f))
        y = factorial(f)
        a.update({f : y})
        print(a)