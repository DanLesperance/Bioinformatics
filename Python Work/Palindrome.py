import sys
#take the first argument from command line 
sequence = sys.argv[1]
sequence = sequence.upper()

#same as in Ex5-1.py will provide the complement nucleotide 
def complement(nuc):
    nucleotides = 'ACGT'
    complements = 'TGCA'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

#obtain the reverse complement palindrome
def RevCompPalindrome(seq):
    halfseq = (len(seq)/2) #palindrome check will only need half the seq (also will truncate any .5s)
    count = 0 
    for nuc in range(0,halfseq): 
        back = seq[(-nuc-1)] #easier than trying to utilize this in the if below
        if seq[nuc] == complement(back): #does nucleotide i = the complement in pos going backwards
            count = count+1 #providing a count for number of potential self hybridizing pairs
    return count

#Take the count and check if it's a palindrome
palindromeCheck = RevCompPalindrome(sequence)

if palindromeCheck == len(sequence)/2:
    print "This sequence is a reverse complement palindrome"
    print "There exists", palindromeCheck, "potentially self hybridizing pair(s)."
else:
    print "This sequence is not a reveerse complement palindrome"
    print "But", palindromeCheck, "potentially self hybridizing pair(s) exist."
   
    

