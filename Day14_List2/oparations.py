# l1=[1,2,3,4,5]

# # for i in range(len(l1)):
# #     print(l1[i])

# # for x in l1:
# #     print(x)
# # i=0
# # while i<len(l1):
# #     print(l1[i])
# #     i+=1

# # adding elements to the list:

# '''
# 1.append
# 2.extend
# 3.insert
# 4.copy
# '''
# l1.append(6)
# print(l1) 

# l1.extend([7,8,9,10])
# print(l1)

# l2=l1.copy()
# print(l2)

# l2.insert(0,20)
# print(l2)

# # remove the elements from the list
# '''
# 1.remove
# 2.pop
# 3.clear
# 4.del
# '''
# l2.pop()
# print(l2)

# l2.append(20)
# print(l2)
# l2.remove(20)
# print(l2)

# l2.clear()
# print(l2)

# # del(l2)
# # print(l2)


# # methods in the list

# '''
# index
# count
# reverse
# sort
# '''
# print(l1.index(5))
# print(l1.count(11))
# l1.reverse()
# print(l1)

# l3=[40,10,90,50,20,3,11,1]
# l3.sort()
# print(l3)


# l4=[x**2 for x in range(1,6)]
# print(l4)

nl=[[1,2,3],[4,5,6],[7,8,9]]
print(nl[0][0])
for x in nl:
    print(x)
