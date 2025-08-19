'''number=int(input('Enter a number to find the factors:'))
for i in range(1,number+1):
    if number%i==0:
        print(i,'is the factor of',number)

pnumber=int(input('Enter anumber to check wether the number is a prime number or not:'))
count=0
for i in range(1,pnumber+1):
    if pnumber%i==0:
        count+=1
if count==2:
    print(pnumber,'is a prime number')
else:
    print(pnumber,'is not a prime number')'''  


'''for i in range(2,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,'is a prime number')
print('loop completed')'''


for i in range(1,4):
    for j in range(1,4):
        print(i,'-',j,end=',')
    print(' ') 


for i in range(1,6):
    for j in range(1,6):
        if i<=j:
         print('*',end=' ')
    print(' ')    

