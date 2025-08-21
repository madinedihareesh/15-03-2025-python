name='AchieversIT'
# rindex:
print(name.rindex('e',0,5))
# count:
print(name.count('e',5))
# ljust
print(len(name))
subname=name.ljust(14,'*')
print(len(subname))
print(subname)
# rjust
subname1=name.rjust(14,'*')
print(subname1)
# center
subname2=name.center(20,'*')
print(subname2)
# zfill
subname3=name.zfill(20)
print(subname3)
subname4=name[0:9].count('e')
print(subname4)

string='   Hello   '
print(len(string))
# lstrip
string1=string.lstrip()
print(len(string1))
print(string1)
# rstrip
string2=string.rstrip()
print(len(string2))
print(string2)
# strip
string3=string.strip()
print(len(string3))
print(string3)

# joins and splits:
ex='a-b-c-d-e'
print(ex.replace('-',','))
s1='abhi'
s2='Karthik'
print(s1.join(s2))
# split
rep='venkata shashank kumar'
repl=rep.split(' ',1)

for x in repl:
    print(x)

#rslipt
rep2=rep.rsplit(' ',1) 
print(rep2)

# splitlines
para='''HI there 
today we are discussing 
about strings'''
print(para.splitlines())

# prefix and sufix
qout="Python is powerful and more easy to learn"
# startswith
print(qout.startswith('P'))
# endswith
print(qout.endswith('learn'))
# removeprefix
print(qout.removeprefix('Py'))
# removesufix
print(qout.removesuffix('rn'))

# partion:
email='ambika@gmail.com'
print(email.partition('@'))
# upper
whish='hello'
print(whish.upper())
# lower
greeting='How are you doing'
print(greeting.lower())
movie='sky high'
print(movie.title())
print(movie.capitalize())
print(greeting.swapcase())

print('welcome'.isalpha())
print(isinstance(79.15,float))

print(dir(str))





