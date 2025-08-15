# [1] Check if a number is prime or not

"""n=int(input("enter number:"))
count=0
for i in range(1,n+1):
    if(n%i==0):
       count+=1
if(count==2):
    print("prime")
else:
    print("not prime")"""

#input:  enter number:6
#output: not prime
#        enter number:5
#        prime

# [2] find the factorial of number

"""n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)"""

#input:  enter number:5
#output: 120

# [3] print fibonacci series upto n terms

"""n=int(input("enter number:"))
a=0
b=1
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b"""
    
#input:  enter number:7
#output: 0 1 1 2 3 5 8

# [4] finding the sum of digits of a given number

"""n=int(input("enter number:"))
sum=0
while n>0:
    digit = n % 10
    sum+=digit
    n//=10
print(sum)"""

#input:  enter number:123
#output: 6

#reverse the digits of a given number

n=int(input("enter number:"))
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n//=10
print(rev)








