#ordered collection of Hetro elemens. it is mutable. it is accepting duplicate values
# l1=[1,2,3,4,5,6]
# l2=[1.2,2.5,3.4,6.7]
# l3=['john','smith','jamson']

# l1.append(2)
# print(l1)

# L1=[1,6.9,True,'john',[1,2,34]]
# print(L1)
# print(L1[4][2])

# ways to creation of list:
# List1=[1,2,3,4,5]
# List2=list((9,8,7,6))
# print(List2)
# List3=list('AchieversIT')
# print(List3)
# List4=[]
# print(type(List4))
# List4.extend([1,2,3,4,5,6,7,8])
# print(List4)

# indexing and slicing:
# l1=[1,2,3,4,5,6,7,8]
# print(l1[2])
# print(l1[-6])

# e1=l1[0:4]
# print(e1)
# print(l1[:])
# print(l1[::1])
# print(l1[::-1][0])
# print(l1[1:5:1])
# print(l1[-7:-3:1])


# indexing and slicling writing:
# l1[2]=9
# print(l1)
# l1[2]=[1,2,3]
# print(l1)

# l1[-1]=10
# print(l1)

# l1[0:0]=[10,11,12,16]
# # l1[1:2]=[11]
# print(l1)
# l1[0:3]=[13,14,15]
# print(l1)
# l1[::2]=[99,98,97,96,95,94]
# print(l1)

l1=[1,2,3]
l2=[4,5,6]
l4=[1,2,3,4]
l5=[2]

l3=l1+l2
print(l3)

# l4=l1*3
# print(l4)

print(l4<l5)