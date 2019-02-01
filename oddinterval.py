usr = (raw_input())
usr = usr.split()
temp =1
for i in range(int(usr[0]) +1, int(usr[1])):
  if(i%2 != 0):
  	if(temp !=1):
  		print(" ")
	print (i)
	temp =0
    
    
