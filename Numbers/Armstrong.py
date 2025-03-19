n = int(input("enter any number = "))
c = len(str(n))
s = 0
a = n
while (n!=0):
    d = n%10
    n = n//10
    s += (d**c)
if (s==a):
    print(a, " is an Armstrong number")
else:
    print(a, " is not an Armstrong number")