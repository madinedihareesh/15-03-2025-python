# n = int(input('Enter a number : '))
# rev = 0
# if(n !=0):
#     while 
def palindrome(number):
    
    s=str(number)
    
    if s==s[::-1]:
    
        print(s,"It is palindrome")
    else:
        print("It is not a palindrome")
palindrome(1221)    

for i in range(6, 1, -1):
    for j in range(1, i+1):
        print('* ', end='')
    print()


number=int(input('Enter a number wether it is a palendrome or not:'))
check=number
rev=0
while number>0:
    r=number%10
    rev=rev*10+r
    number//=10
print(rev)
if check==rev:
    print(rev,'is a palendrome')
else:
    print(rev,'is not a palandrome')  
    





    
