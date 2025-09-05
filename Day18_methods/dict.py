d1={1:'one',2:'two',3:'three',4:'four',5:'five'}
'''
1.key()
2.values()
3. items()
4. get()
5.setdefault()
'''
# keys()
k=d1.keys()
print(k)

for x in k:
    print(d1[x])

# values: 
v=d1.values()
print(v)
for x in v:
    print(x)

person={'name':'Abhi','age':30,'loc':'vijayawada','ocu':'study'}
deatils=person.keys()

for x in deatils:
    print(person[x])


#items()
item=person.items()
print(item) 


# get()
g=person.get('job','missing')
print(g)

# set default()
s=person.setdefault('age')
print(s)

# update()
print(person)
personedu={'Degree':'B.ech','college':'vvit','pass':2025}
person.update(personedu)
print(person)

# copy()
d2=d1.copy()
print(d2)

# pop()
d2.pop(5)
print(d2)

# popitem()
d2.popitem()
print(d2)

d2.clear()
print(d2)