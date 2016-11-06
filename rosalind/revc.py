def reverseComplement (dna):
	revc = list()
	for i in dna:
		if i is 'A':
			revc.append('T')
		if i is 'T':
			revc.append('A')
		if i is 'C':
			revc.append('G')
		if i is 'G':
			revc.append('C')
	revc.reverse()
	for i in revc:
		print (i, end="")
	print ()

t = input()
reverseComplement (t)