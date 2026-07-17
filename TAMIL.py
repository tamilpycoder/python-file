#Addition

a=int(input("enter A the value:"))
b=int(input("enter B the value:"))
c=a+b
print(c)

#subtract
a=int(input("enter A the value:"))
b=int(input("enter B the value:"))
c=a-b
print(c)

#Multiplication
a=int(input("enter A the value:"))
b=int(input("enter B the value:"))
c=a*b
print(c)

#Division
a=int(input("enter A the value:"))
b=int(input("enter B the value:"))
c=a/b
print(c)

#Modulus
a=int(input("enter A the value:"))
b=int(input("enter B the value:"))
c=a%b
print(c)


#Floor Division
a=int(input("enter A the value:"))
b=int(input("enter B the value:"))
c=a//b
print(c)

#Exponnintion
a=int(input("enter A the value:"))
b=int(input("enter B the value:"))
c=a**b
print(c)




###CALCULATE PEREMATER

#rectangle
L=float(input("Enter L value:"))
B=float(input("Enter B value:"))
print("Area=",L*B)
print("Perimeter=",2*(L+B))

#Square

Square=float(input("Enter the square value:"))
print("Area=",(Square*Square))
print("Perimeter",4*Square)


#Circle
c=float(input("Enter the circle Value:"))
print("Area=",3.14*c*c)
print("perimeter=",2*3.14*c)

#Find avarage of 3 number

a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=(a+b+c)/3
print(d)

#Chech number
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=(a==b)
print(c)
#greater than or equal to 
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=(a>=b)
print(c)

#lessthen or equal to
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=(a<=b)
print(c)

#square root of the number
a=int(input("enter the number:"))
print(a**0.5)

#simple Interest
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=(a*b*c)/100
print(d)

#Compound Interest
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=a*(1+b/100)**c
e=d-a
print(e)

#operators
a=10
a+=5
print(a)

a-=3
print(a)

a*=2
print(a)


a/=4
print(a)

a%=2
print(a)

a**=3
print(a)

#swap two number
a=10
b=20
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b+",b)


#Check username & Passwoard
Username=(input("Enter your usename:"))
Passwoard=(input("Enter your passwoard:"))
if Username == "admin" and Passwoard == 1234:
    print("login sucessesfull")
else:
    print("username or passwoard is wrong")



#cube root of the  number
A=int(input("Enert the number:"))
b=A**(1/3)
print(b)

#About Me

# My name is Thamaraiselvan
# I am studying B.tech
# I like Python Programming
# I am interested in Photography
# I want to become a CEO


#Uses of Python

'''
Python is used for Web Development.
Python is used for Data Science.
Python is used for Artificial Intelligence.
Python is used for Automation.
Python is used for Game Development.
'''


#Only Comments Program

# This program contains only comments
# No input is used
# No processing is done
# No output is displayed
# End of program




#Calculator Program


a=int(input("Enter A value:"))


b=int(input("Enter B value:"))


c=a+b


print(c)



#Comments Test

a=10
b=20
c=a+b
print(c)

#entha line output la show aaagathu


#Print Data Types

a=10
b=10.5
c="Python"
d=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))



#Input Data Types

a=input("Enter your name:")
b=int(input("Enter your age:"))
c=float(input("Enter your salary:"))

print(type(a))
print(type(b))
print(type(c))


#Integer to Float

a=10
b=float(a)
print(b)

#Float to Integer

a=10.5
b=int(a)
print(b)


#String to Integer Addition

a="10"
b="20"

c=int(a)+int(b)
print(c)


#Using +=

a=10
a+=5
print(a)

    
#Using -=

a=20
a-=5
print(a)


#Using *=

a=10000
a*=2
print(a)


#Using /=

a=300
a/=3
print(a)


#Using %=

a=25
a%=4
print(a)


#Same Variable

a=10
print(a)

a="Python"
print(a)

a=10.5
print(a)



#Print Datatype

a=10
print(type(a))

a="Hello"
print(type(a))

a=5.5
print(type(a))


#Boolean Datatype

a=True
print(type(a))


#String to Integer

a="50"
b=int(a)
print(b)



#Change Variable Five Times

a=10
print(a)

a=20
print(a)

a=30
print(a)

a=40
print(a)

a=50
print(a)


#Add a Value to a List

a=[10,20,30]
a.append(40)
print(a)

#Remove a Value from a List

a=[10,20,30]
a.remove(20)
print(a)

#Update a Dictionary Value

a={"name":"Tamilhh","mark":80}
a["mark"]=95
print(a)

#Add a Value to a Set

a={10,20,30}
a.add(40)
print(a)

#Modify Mutable Object

a=[10,20]
print(a)
a.append(30)
print(a)

#Simple Calculator

a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Area of Rectangle

a=float(input("Enter Length:"))
b=float(input("Enter Breadth:"))
print(a*b)

#Area of Circle

a=float(input("Enter Radius:"))
print(3.14*a*a)

#Total and Average

a=int(input())
b=int(input())
c=int(input())
d=a+b+c
print(d)
print(d/3)

#Seconds Conversion

a=int(input("Enter Seconds:"))
b=a//3600
c=(a%3600)//60
d=a%60
print(b)
print(c)
print(d)

#Using +=

a=10
a+=5
print(a)

#Using -=

a=10
a-=5
print(a)

#Using *=

a=10
a*=5
print(a)

#Using //=

a=10
a//=3
print(a)

#Using %=

a=10
a%=3
print(a)

#Check Whether Two Numbers are Equal

a=int(input())
b=int(input())
print(a==b)

#Check Greater Number

a=int(input())
b=int(input())
print(a>b)

#Check Age Above 18

a=int(input())
print(a>18)

#Check Pass or Fail

a=int(input())
print(a>=35)

#Check Salary Above 50000

a=int(input())
print(a>50000)

#Username and Password Validation

a=input("Enter Username:")
b=input("Enter Password:")

if a=="admin" and b=="1234":
    print("Login Success")
else:
    print("Login Failed")

#Check Age and Citizenship

a=int(input("Age:"))
b=input("Citizen:")

if a>=18 and b=="yes":
    print("Eligible")
else:
    print("Not Eligible")

#Check Temperature

a=int(input())

if a<20 or a>30:
    print("Outside Range")
else:
    print("Within Range")

#Use NOT Operator

a=input("Username:")

if not a=="admin":
    print("Invalid User")
else:
    print("Valid User")

#Check Voting Eligibility

a=int(input())

if a>=18:
    print("Can Vote")
else:
    print("Cannot Vote")

#Bitwise AND

a=10
b=5
print(a&b)

#Bitwise OR

a=10
b=5
print(a|b)

#Bitwise XOR

a=10
b=5
print(a^b)

#Left Shift

a=10
print(a<<2)

#Right Shift

a=10
print(a>>2)

#Use is Operator

a=10
b=10
print(a is b)

#Use is not Operator

a=10
b=20
print(a is not b)

#Compare Same Lists

a=[1,2,3]
b=a
print(a is b)

#Compare Different Lists

a=[1,2,3]
b=[1,2,3]
print(a is b)

#Compare Integer Identities

a=100
b=100
print(a is b)

#Check Name in List

a=["Kumaran","Ravi","Arun"]
print("Kumaran" in a)

#Check Letter in String

a="Python"
print("P" in a)

#Check Number in Tuple

a=(10,20,30)
print(20 in a)

#Check Key in Dictionary

a={"name":"Tamil","age":21}
print("name" in a)

#Check Value in Set

a={10,20,30}
print(20 in a)

#Convert Name to Uppercase

a=input("Enter Name:")
print(a.upper())

#Convert Sentence to Lowercase

a=input("Enter Sentence:")
print(a.lower())

#Count Vowels in String

a=input("Enter String:")
b=0

for i in a:
    if i in "aeiouAEIOU":
        b=b+1

print(b)

#Reverse a String

a=input("Enter String:")
print(a[::-1])

#Check Palindrome

a=input("Enter String:")

if a==a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Find Largest Number

a=[10,50,30,20]
print(max(a))

#Find Smallest Number

a=[10,50,30,20]
print(min(a))

#Remove Duplicates

a=[10,20,20,30,30]
print(list(set(a)))

#Find Second Largest Number

a=[10,50,30,20]
a.sort()
print(a[-2])

#Find Sum of List Values

a=[10,20,30,40]
print(sum(a))

#Create a Tuple

a=(10,20,30)
print(a)

#Count Occurrences of a Value

a=(10,20,10,30)
print(a.count(10))

#Find Index of a Value

a=(10,20,30)
print(a.index(20))

#Convert Tuple to List

a=(10,20,30)
b=list(a)
print(b)

#Perform Tuple Unpacking

a=(10,20,30)
b,c,d=a

print(b)
print(c)
print(d)

#Remove Duplicates Using Set

a=[10,20,20,30]
print(set(a))

#Perform Union

a={1,2,3}
b={3,4,5}
print(a.union(b))

#Perform Intersection

a={1,2,3}
b={2,3,4}
print(a.intersection(b))

#Perform Difference

a={1,2,3}
b={2,3,4}
print(a.difference(b))

#Perform Symmetric Difference

a={1,2,3}
b={2,3,4}
print(a.symmetric_difference(b))

#Store Student Details

a={"name":"Kumaran","mark":90}
print(a)

#Update Marks

a={"mark":80}
a["mark"]=95
print(a)

#Check Whether a Key Exists

a={"name":"Kumaran","age":21}
print("name" in a)

#Find Total Marks

a={"tamil":80,"english":90,"maths":85}
print(sum(a.values()))

#Loop Through Dictionary

a={"name":"Kumaran","age":21}

for i in a:
    print(i,a[i])

#Check Even or Odd

a=int(input())

if a%2==0:
    print("Even")
else:
    print("Odd")

#Check Positive or Negative

a=int(input())

if a>=0:
    print("Positive")
else:
    print("Negative")

#Check Pass or Fail

a=int(input())

if a>=35:
    print("Pass")
else:
    print("Fail")

#Check Age Eligibility

a=int(input())

if a>=18:
    print("Eligible")
else:
    print("Not Eligible")

#Find Largest of Two Numbers

a=int(input())
b=int(input())

if a>b:
    print(a)
else:
    print(b)

#Grade System

a=int(input())

if a>=90:
    print("A")
elif a>=75:
    print("B")
elif a>=50:
    print("C")
else:
    print("D")

#ATM Balance Check

a=int(input())

if a>1000:
    print("Sufficient Balance")
elif a==1000:
    print("Minimum Balance")
else:
    print("Low Balance")

#Traffic Signal Action

a=input()

if a=="red":
    print("Stop")
elif a=="yellow":
    print("Wait")
else:
    print("Go")

#Calculator

a=int(input())
b=int(input())
c=input()

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
else:
    print(a*b)

#Electricity Bill Calculation

a=int(input())

if a<=100:
    print(a*2)
elif a<=200:
    print(a*3)
else:
    print(a*5)

#Password Check

a=input()

if a=="1234":
    print("Correct")
else:
    print("Wrong")

#Login Validation

a=input()
b=input()

if a=="admin" and b=="1234":
    print("Login Success")
else:
    print("Login Failed")

#Ticket Booking Eligibility

a=int(input())

if a>=18:
    print("Can Book Ticket")
else:
    print("Cannot Book Ticket")

#Salary Eligibility

a=int(input())

if a>=30000:
    print("Eligible")
else:
    print("Not Eligible")

#Check Divisibility by 5

a=int(input())

if a%5==0:
    print("Divisible")
else:
    print("Not Divisible")

#College Admission Eligibility

a=int(input("Enter Mark:"))

if a>=60:
    if a>=80:
        print("Engineering Seat")
    else:
        print("Arts Seat")
else:
    print("Not Eligible")

#Loan Approval

a=int(input("Enter Salary:"))

if a>=30000:
    if a>=50000:
        print("Loan Approved")
    else:
        print("Loan Pending")
else:
    print("Loan Rejected")

#Driving Licence Eligibility

a=int(input("Enter Age:"))

if a>=18:
    if a>=21:
        print("Driving Licence Approved")
    else:
        print("Learner Licence")
else:
    print("Not Eligible")

#Employee Bonus Eligibility

a=int(input("Enter Experience:"))

if a>=2:
    if a>=5:
        print("Bonus Eligible")
    else:
        print("Small Bonus")
else:
    print("No Bonus")

#Scholarship Eligibility

a=int(input("Enter Mark:"))

if a>=70:
    if a>=90:
        print("Full Scholarship")
    else:
        print("Half Scholarship")
else:
    print("No Scholarship")

#Print Numbers from 1 to 100

for i in range(1,101):
    print(i)

#Print Even Numbers

for i in range(2,101,2):
    print(i)

#Print Odd Numbers

for i in range(1,101,2):
    print(i)

#Multiplication Table

a=int(input("Enter Number:"))

for i in range(1,11):
    print(a*i)

#Factorial

a=int(input("Enter Number:"))
b=1

for i in range(1,a+1):
    b=b*i

print(b)

#Square Star Pattern

for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

#Number Pattern

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

#Triangle Pattern

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

#Multiplication Tables

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()

#Chessboard Pattern

for i in range(8):
    for j in range(8):
        print("#",end=" ")
    print()
