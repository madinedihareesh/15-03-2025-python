d1={'name':('Peter','Bruce','clark'),'age':(20,40,35),'loc':('NY','Gotam','starcity')}

for i in d1['name']:
    print(i)

d2={1:'one',2:'two',3:'three'}

d2[1]='Ace'

print(d2)

d2[4]='four'
print(d2)

# itarable pairs
l1=[['name','abhi'],['age',23],['loc','vij'],['ocu','study']]
d3=dict(l1)
print(d3)
'''
[[],[],[]]
[(),(),()]
([],[],[])
((),(),())
'''
# zip function
l2=[1,2,3,4]
l3=['one','two','three','four']
d4=dict(zip(l2,l3))
print(d4)

# enumarated function
d4=dict(enumerate(l3,start=1))
print(d4)

'''
l1=[x for x in range(1,6)]
t1=(*(x for x in range(1,6)),)
s1={x for x in range(1,6)}
'''

# comprehension with iterable pairs
d5={x:y for x,y in l1}
print(d5)

# zip function
d6={x:y for x,y in zip(l2,l3)}
print(d6)

# enumarate function
d7={x:y for x,y in enumerate(l3,start=1)}
print(d7)