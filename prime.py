number = int(raw_input())
if number > 1:
   for i in range(2,number):
       if (number % i) == 0:
           print("no")
   else:
       print("yes")
       
