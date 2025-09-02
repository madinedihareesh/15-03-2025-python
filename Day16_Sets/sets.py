'''s1={1,2,3,4,5,1,2}
s2=set([1,2,3,4,5,1,2])
s3=set('python')
s4={5}
print(type(s4))
s5=set()
print(type(s5))

for i in s3:
    print(i)

for x in s1:
    print(x) 


s4.add(4)
print(s4)

s4.remove(4)
print(s4)

s4.clear()
print(s4)


s1.pop()
print(s1)
s1.pop()
print(s1)'''

'''
S={1,2,3,4,5,6,7,8,9,10}
A={1,2,3,4,5} B={6,7,8,9,10} c={1,2,3,4,5,6,7,8,9,10}
d={1,2,3,4,5} e={4,5,6,7,8}
d union e={1,2,3,4,5,6,7,8}
d intersection e={4,5}
d - e={1,2,3}
e-d={6,7,8}
d-e != e-d
d^e=d-e u e-d
{1,2,3,6,7,8}
'''

A={1,2,3,4,5}
B={4,5,6,7,8}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))


c={11,12,13}
c.update([14,15,16])
print(c)

L1=[x**2 for x in range(1,6)]
print(L1)
T1=(*(x for x in range(1,6)),)
print(T1)
S1={x for x in range(1,6)}
print(S1)