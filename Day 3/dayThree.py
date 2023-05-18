nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
# if there are two terms, return n1 and n2
elif nterms == 2:
    print("Fibonacci sequence:")
    print(n1)
    print(n2)
# generate Fibonacci sequence
else:
    print("Fibonacci sequence:")
    print(n1)
    print(n2)
    while count < nterms - 2:
        nth = n1 + n2
        print(nth)
        # update values
        n1 = n2
        n2 = nth
        count += 1
