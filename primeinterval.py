start = int(raw_input())
end = int(raw_input())
for val in range(start, end + 1): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 
