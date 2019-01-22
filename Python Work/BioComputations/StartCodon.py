#2.1
##Input
Codon = 'ATG'

##Make Codon backwards and lowercase
#only works when input is three characters
RevCodon = Codon[2]+Codon[1]+Codon[0] 
LowerRevCodon = RevCodon.lower()

##result
print 'The lower case and backwards codon is', LowerRevCodon

#2.2
##Input
seq = 'gcatcacgttatgtcgactctgtgtggcgtctgctggg'

##Position and Trans Frame of first start Codon
FirstStart = seq.find('atg')
TransFrame = (FirstStart%3)+1

##Output
print 'The first start codon is at position', FirstStart,'aka', FirstStart+1, 'base pairs from the beginning'
print 'The first start codon is in translation frame',TransFrame
