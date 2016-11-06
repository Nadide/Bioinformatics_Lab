def CountNucleotides (dna):
	print ("A:", dna.count('A')+dna.count('a'))
	print ("C:", dna.count('C')+dna.count('c'))
	print ("G:", dna.count('G')+dna.count('g'))
	print ("T:", dna.count('T')+dna.count('t'))

t = input()
CountNucleotides (t)