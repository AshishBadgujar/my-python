# anagrams number
s1=input("enter first string ")
s2=input("enter second string ")
if(sorted(s1)==sorted(s2)):
    print("string is anagrams")
else:
    print("string is not anagrams")