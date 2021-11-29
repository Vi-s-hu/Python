# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))


n1, n2 = 0, 1 
count = 0


if nterms <= 0: # check if the number of terms is valid
   print("Please enter a positive integer")

elif nterms == 1: # if there is only one term, return n1
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:") # generate fibonacci sequence
   while count < nterms:
       print(n1)
       nth = n1 + n2
       
       n1 = n2 # update values
       n2 = nth
       count += 1