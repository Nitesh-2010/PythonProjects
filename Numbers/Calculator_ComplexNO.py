import sys
a = complex(input("Enter the 1st complex number = "))
b = complex(input("Enter the 2nd complex number = "))
print("Sum = ", a + b)
print("Difference for 1st and 2nd= ", a - b, "\nDifference for 2nd and 1st = ", b - a )
print("Product = ", a * b)
if (abs(b)==0):
    print("Divison by 0 is not possible")
    sys.exit(0)
print("Quotient when the 2nd no. divided the 1st no. = ", a/b, "\nQuotient when the 1st no. divides the 2nd no. = ",b/a)    