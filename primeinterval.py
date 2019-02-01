usr = int(raw_input())
usr = usr.split()
temp = 1
for val in range(int(usr[0]+1), int(usr[1])): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 
