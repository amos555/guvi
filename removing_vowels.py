s = raw_input()
n = s

vowels = ('a', 'e', 'i', 'o', 'u')
for x in s.lower():
	if x in vowels:
		n = n.replace(x,"")
		
def reverse(n):
  str = ""
  for i in n:
    str = i + str
  return str

print (reverse(n))
