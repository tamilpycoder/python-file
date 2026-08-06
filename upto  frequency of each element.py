for i in range(10):
    print("Hello Data Science")


a=int(input("Enter N value:"))

for i in range(1,a+1):
    print(i)


a=int(input("Enter N value:"))

for i in range(a,0,-1):
    print(i)


a=int(input("Enter N value:"))

for i in range(2,a+1,2):
    print(i)


a=int(input("Enter N value:"))

for i in range(1,a+1,2):
    print(i)


a=int(input("Enter N value:"))
b=0

for i in range(1,a+1):
    b=b+i

print(b)


a=int(input("Enter Number:"))
b=1

for i in range(1,a+1):
    b=b*i

print(b)


a=int(input("Enter Number:"))

for i in range(1,11):
    print(a,"x",i,"=",a*i)


a=int(input("Enter Number:"))
b=0

while a>0:
    b=b+1
    a=a//10

print(b)


a=int(input("Enter Number:"))
b=0

while a>0:
    c=a%10
    b=b*10+c
    a=a//10

print(b)


a=int(input("Enter Number:"))

if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")


a=int(input("Enter Number:"))

if a%2==0:
    print("Even")
else:
    print("Odd")


a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
c=int(input("Enter C value:"))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


a=int(input("Enter Year:"))

if a%400==0 or a%4==0 and a%100!=0:
    print("Leap Year")
else:
    print("Not Leap Year")


a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
c=input("Enter Operator:")

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("Invalid Operator")


a=int(input("Enter Number:"))

if a%5==0 and a%11==0:
    print("Divisible")
else:
    print("Not Divisible")


a=int(input("Enter Mark:"))

if a>=90:
    print("A Grade")
elif a>=80:
    print("B Grade")
elif a>=70:
    print("C Grade")
elif a>=50:
    print("D Grade")
else:
    print("Fail")


a=input("Enter Character:")

if a in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


a=int(input("Enter Age:"))

if a>=18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
c=int(input("Enter C value:"))

if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)


a=int(input("Enter N terms:"))
b=0
c=1

for i in range(a):
    print(b)
    d=b+c
    b=c
    c=d


a=int(input("Enter Number:"))
b=a
c=0

while a>0:
    d=a%10
    c=c*10+d
    a=a//10

if b==c:
    print("Palindrome")
else:
    print("Not Palindrome")


a=int(input("Enter Number:"))
b=a
c=0

while a>0:
    d=a%10
    c=c+d**3
    a=a//10

if b==c:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


a=int(input("Enter N value:"))

for i in range(2,a+1):
    b=0

    for j in range(1,i+1):
        if i%j==0:
            b=b+1

    if b==2:
        print(i)


a=int(input("Enter N value:"))
b=0

for i in range(2,a+1):
    c=0

    for j in range(1,i+1):
        if i%j==0:
            c=c+1

    if c==2:
        b=b+1

print(b)


a=int(input("Enter A value:"))
b=int(input("Enter B value:"))

while b!=0:
    c=a%b
    a=b
    b=c

print(a)


a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
c=a*b

while b!=0:
    d=a%b
    a=b
    b=d

print(c//a)


a=int(input("Enter Number:"))
b=0

while a>0:
    c=a%10
    b=b+c
    a=a//10

print(b)


a=int(input("Enter Number:"))
b=1

while a>0:
    c=a%10
    b=b*c
    a=a//10

print(b)


a=int(input("Enter Number:"))

for i in range(1,a+1):
    if a%i==0:
        print(i)


a=[10,50,20,40,30]

print(max(a))


a=[10,50,20,40,30]

print(min(a))


a=[10,20,30,40,50]

print(sum(a))


a=[10,20,30,40,50]

b=sum(a)
c=len(a)

print(b/c)


a=[10,21,30,41,50,61]
b=0
c=0

for i in a:
    if i%2==0:
        b=b+1
    else:
        c=c+1

print("Even=",b)
print("Odd=",c)


a=[10,50,30,40,20]

a.sort()

print(a[-2])


a=[10,20,20,30,30,40]
b=[]

for i in a:
    if i not in b:
        b.append(i)

print(b)


a=[10,20,30,40,50]
b=[]

for i in range(len(a)-1,-1,-1):
    b.append(a[i])

print(b)


a=[30,10,20]
b=[60,50,40]

c=a+b
c.sort()

print(c)


a=[10,20,10,30,20,10]
b={}

for i in a:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1

print(b)
