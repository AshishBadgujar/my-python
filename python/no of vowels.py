#no of vowels
s1=input("enter string ")
vowels=0
for i in s1:
    if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
        vowels=vowels+1

print(vowels)