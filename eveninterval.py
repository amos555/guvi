usr1 = (raw_input())
usr1 = usr1.split()
temp =1
for i in range(int(usr1[0]) +1, int(usr1[1])):
  if(i%2 == 0):
  	if(temp !=1):
  		print(" ")
	print (i)
	temp =0
