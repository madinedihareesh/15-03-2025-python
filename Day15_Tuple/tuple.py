# t1=(1,2,3,4.5,5.6,'john',1,2,3)
# print(t1)
# print(t1[0])
# t1[0]=10
# print(t1)

# ways to create a list:
# t1=(1,2,3,4)
# t2=tuple([4,5,6,7])
# print(t2)
# t3=tuple('Peter')
# print(t3)
# t4=(3,)
# print(type(t4))
# t5=9,8,7,6,5
# print(type(t5))


# reading of tuple with index:
# print(t1[0])
# print(len(t1))
# print(t1[-1])

# slice oparations on tuple:
# T=t1[::-1]
# print(T)

# traversing through a tuple:
T=1,2,3,4,5,6,7,8,9,10

# length=0
# while length<len(T):
#     print(T[length])
#     length+=1


# for i in range(len(T)):
#     print(T[i])

# for X in T:
#     print(X)


t1=(1,2,3)
t2=(4,5,6)

t3=t1+t2
print(t3)

t4=t1*4
print(t4)


# packing and unpacking
a,*b=t1
print(a)
print(b)


# comprohension
T2=(*(x for x in range(1,6)),)
print(T2)