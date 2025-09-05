l1=[1,2,3,4,5]
def add(n):
    total=0
    for i in n:
        total+=i
    print(total) 

add(l1)


def vol(a,b,c,/):
    print('volume:',a*b*c)


vol(10,20,30)


def sum(*,a,b,c):
    print('sum of numbers:',a+b+c)


sum(a=10,b=20,c=30)

# positional vs keyword arrguments

def fun(a,b,c):
    print(a,b,c)

fun(a=10,b=20,c=30)  

# mixed postional and keyword arrgument

def fun(a,b,/,*,c,d):
    print(a,b,c,d)

fun(10,20,c=30,d=40)


def cal(*args):
    total=0
    for x in args:
        total+=x
    print(total)

cal(1,2,3,4,5,6,7,8,9,10)    


def mat(**Kwargs):
    print(Kwargs)

mat(a=10,b=20,c=30)


def test(*args,**kwargs):
    print(args,kwargs)


test(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)    



