name='Abhilash'

print(name[0])

# for x in name:
#     print(x)

# print(len(name))
# print(type(name))
# print(dir(str)) 

for i in range(0,len(name)):
    print(name[i])

#slicing[start:stop:step]

str1=name[:4:2]
print(str1)
print(name[-8])
rev=name[::-1]
print(rev)
rev1=''
for i in range(len(name)-1,-1,-1):
    rev1+=name[i]
if rev1==name:
    print('it is a palandrome')
else:
    print('it is not')   


print(name.find('h',3,6))        
print(name.rfind('h',0,6))
print(name.index('d'))

'''
'''