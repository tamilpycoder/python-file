'''#function
def greet(a):
    for i in range(a):
        print("Welcome to Python")
i=int(input("Enter the number:"))
greet(i)

#2nd Function
def Welcome():
    a=input("Enter the Student's Name:")
    print("Welcome",a)
Welcome()

#Add function
def add():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=a+b
    print(c)
add()

#Square Function
def square():
    a=int(input("Enter the number:"))
    print(a**2)
square()

#Square Function
def cube():
    a=int(input("Enter the number:"))
    print(a**3)
cube()

#Odd or even

def tamil():
    a=int(input("Enter the number:"))
    if a%2==0:
        print("It is Even")
    else:
        print("It is Odd")
tamil()

#possitive or negative number

def tamil():
    a=int(input("Enter the number:"))
    if a>=0:
        print("It is possitive")
    else:
        print("It is Negative")
tamil()

#Maximum

def num():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=[a,b]
    print(max(c))
num()

#minimum

def num():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    d=int(input("Enter the number:"))
    c=[a,b,d]
    print(min(c))
num()


#Area of circle

def area_circle(c):
    b=3.14*c*c
    print(b)

area_circle(5)

#leap year

def check_leap_year():
    year=int(input("Enter the year:"))
    if year%4==0:
        print("It is leap year")
    else:
        print("It is not leap year")

check_leap_year()

##largest  number
def find_largest():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    c=int(input("Enter the number:"))
    d=[a,b,c]
    print(max(d))
find_largest()

#Table
def multiplication_table():
    table=int(input("Enter the number:"))
    for i in range(1,11):
        print(i,"x",table,"=",table*i)
multiplication_table()

#Reverse
def reverse_number():
    a=(input("Enter the number:"))
    print(a[::-1])
reverse_number()'''










