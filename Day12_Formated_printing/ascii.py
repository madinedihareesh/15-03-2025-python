value='A'
print(ord(value))
print(ord('{'))

# for i in range(65,91):
#     print(chr(i))

# for i in range(0,126):
#     print(chr(i))

print('\u1F00\u1F10\u0C60')

# formating styles
print('hello')
print('world')

print('Hello \nworld')
print('Hello \fworld')
print('valid \rso')
print('hello\tworld')
print('hello\vworld')
print('hello\\world')
print('\'hello world\'')
print('world\b')
print('\N{angry face}')
print('\N{yen sign}')
print('\N{grinning face}')

# c style printing
# it is a 32gb hard drive costs $11.10
# 32 %d%i
# 11.10 %f%F%g
# sting %S
memory=32
device='hard drive'
price=11.10

print('it is a',memory,'gb',device,'costs $',price)
print('it is %dgb %s costs $%g'%(memory,device,price))

print('it is a {}gb {} costs ${}'.format(memory,device,price))
print('it is a {}gb {} costs ${}'.format(price,device,memory))
print('it is a {2}gb {1} costs ${0}'.format(price,device,memory))


print(f'it is a {memory}gb {device} costs ${price}')
