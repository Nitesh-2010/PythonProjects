n = complex(input("Enter any number = "))
if (n.imag==0):
    print(n, " is entirely a real no.")
elif(n.real==0):
    print(n, " is enitrely an imaginary no.")
else:
    print(n, " is a general complex no.")