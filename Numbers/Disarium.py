n = int(input("Enter any number = "))
c = len(str(n))
s = 0
a = n
while (n!=0):
    d = n%10
    n = n//10
    s += (d**c)
    c -= 1
if (s==a):
    print(a, " is a Disarium number")
else:
    print(a, " is not a Disarium number")    