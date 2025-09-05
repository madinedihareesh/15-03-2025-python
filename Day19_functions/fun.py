import math
def fun(name):
    print('Hello',name)


fun('Abhi')
fun('Karthik')


def squre(l,b):
    print(l*b)

squre(b=10,l=10)


def even(n):
    if n%2==0:
        print(n,'is an even number')
    else:
        print(n,'is a odd number') 

even(9)


def area(length,breth,height):
    print(length*breth*height,'is the area of a cuboid')


area(10,6,3)
area(10,6,height=3)

def billing(amount,gst=5):
    if amount>0:
        tol=amount+gst
    print(tol)    

billing(100)
billing(100,15)


def wel():
    return 'Welcome to the world'

print(wel())


def circle(r):
    return math.pi*(r**2)

print(circle(12))


def prime(n):
    if n>0:
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
    if count==2:
        print(n,'is a prime number')
    else:
        print(n,'is not a prime number')

prime(4)

