def dnaToRna (dna):
	dna = dna.replace('T', 'U')
	return dna

t = input()
print( dnaToRna(t) )