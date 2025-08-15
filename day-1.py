# To print given string is palindrome or not

s=input("enter string:")
if(s[::-1]==s):
    print("palindrome")
else:
    print("not palindrome")

#input:  malayalam
#output: palindrome

#counting the frequency of each character in a string

s=input("enter string:")
res=''
for i in s:
    if i not in res:
        print(i,'-',s.count(i))
        res+= i

#input: enter string:college
#output: c - 1
#        o - 1
#        l - 2
#        e - 2
#        g - 1

#reversing a string without using builtin reverse functions

s=input("enter string:")
l=len(s)
i=l-1
while i>=0:
    print(s[i],end='')
    i-=1

#remove all spaces from a given string

s = input("Enter string: ")
s = s.replace(" ", "")
print(s)

#input:  Enter string: pace college
#output: pacecollege

#no.of vowels and consonants in a string

s=input("enter string: ")
vowels ='aeiou'
v_count=0
c_count=0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
print("vowels:",v_count)
print("consonants:",c_count)

#input:  enter string: pace college
#output: vowels: 5
#        consonants: 6
            
        

