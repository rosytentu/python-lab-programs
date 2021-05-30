n=input("enter your word")
n=n.lower()
l=len(n)
flag=0
for i in range(l):
    if n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u':
        print("vowel is '{}' at index={}".format(n[i],i))
        flag=1
        
if flag!=1:
    print("vowel is not present")
