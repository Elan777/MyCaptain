nos = int(input("How many numbers Do you want: "))

n1, n2 = 0, 1
count = 0

if nos <= 0:
   print("Please enter a positive integer")

elif nos == 1:
   print("Fibonacci sequence upto",nos,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nos:
       print(n1)
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1
