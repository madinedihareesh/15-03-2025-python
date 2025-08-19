# i=0
# while True:
#     i+=1
#     print(i)
#     if i<10:
#         continue
#     else:
#         break


# else suite:

# i=0
# while i<10:
#     i+=1
#     print(i)
# else:
#     print('The loop has reached its limit')

# i=6
# while i>0:
#     i-=1
#     print('* '*i)

# i=0
# while i<5:
#     i+=1
#     print(' '*(5-i)+'*'*i)    


'''
range(start,stop,step)
(start=0, if(start<stop,start+=1))

range(0,5,1)
range(6,12)

syntax: 

for var in range/seq
not in
'''

# for abhi in range(1,6,1):
#     print(abhi)


# for i in range(5,0,-1):
#     print(i)    

# for i in range(1,11,2):
#     if i%2==0:
#         print(i,'is a even number')
#     else:
#         print(i,'is a odd number')  
  
'''
5!=5*4*3*2*1
5!=1*2*3*4*5
011235813
'''
# fact=1
# for i in range(1,6):
#     fact=fact*i
# print(fact)    

a=0
b=1
for i in range(10):
    print(a,end=' ')
    c=a+b
    a=b
    b=c
print(' ')    
    

name='AchiveresIT'
for x in name:
    print(x)    
