n = int(input("Enter any number = "))
a = n
r = 0
while (n!=0):
    d = n%10
    r = r*10+d
    n = n//10
if (r==a):
    print(a, " is a Palindrome number")
else:
    print(a, " is not a Palindrome number")