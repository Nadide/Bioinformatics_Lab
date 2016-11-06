def dnaToRna (dna):
	for i in dna:
		if i is 'T':
			print ('U', end="")
		else:
			print (i, end="")
	print ()

t = input()
dnaToRna (t)