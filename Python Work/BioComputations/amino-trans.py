# Import the required modules
import sys

# Assign the user input to variables
seqfile = sys.argv[1]
codonfile = sys.argv[2]

# read the sequence from a file
def readseq(seqfile):
    theseq = ''.join(open(seqfile).read().split())
    theseq = theseq.upper()
    return theseq

# read codons from a file
def readcodons(codonfile):
    f = open(codonfile)
    data = {}
    for l in f:
        sl = l.split()
        key = sl[0]
        value = sl[2]
        data[key] = value    
    f.close()

    b1 = data['Base1']
    b2 = data['Base2']
    b3 = data['Base3']
    aa = data['AAs']
    st = data['Starts']

    codons = {}
    init = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        codons[codon] = aa[i]
        init[codon] = (st[i] == 'M')
    return codons,init

# Determine amino-acid translation based on codon table in "codons".
# Any codon missing from the table (due to N's not in third position
# or whatever) are translated as X.
def trans(codons,seq,frame):
    aalist = []
    for i in range(0,len(seq),3):
        #tfFix will ensure that the codon is read at the right spot
        tfFix = i + (frame-1) 
        codon = seq[tfFix:tfFix+3]
        aa = codons.get(codon,'X')
        aalist.append(aa)
    aaseq = ''.join(aalist)
    return aaseq

#Create a reverse complement of the original sequence for to account
#for all 6 translation reading frames (3 forward and 3 reverse)
def RevComp(seq):
    d = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    revcomp = []
    for nuc in seq:
        v = d.get(nuc,nuc)
        revcomp.insert(0,v)
    revcomp = ''.join(revcomp)
    return revcomp

# If N exists in the third position in any of the translation 
# frames. Ensure the codon file reads the same amino acid for 
# any letter input, if so fix the sequence to output the correct
# amino acid sequence. 
def fixN (codons, seq, frame):
    seq = list(seq)
    for i in range(0, len(seq),3):
        tfFix = i + (frame-1)
        checkSet = set()
        extraBP = len(seq)%3
        codon = seq[tfFix:tfFix+3]
        # Potentially easier way to solve the 
        # out of index error; however, this 
        # if/else statement worked rather well
        if extraBP == 1:
            f = 1
        elif extraBP == 2:
            f = 2
        else:
            f = 0
        # ensure the codon will be within the 
        # index 
        if seq[tfFix] < (len(seq)-f):
            # Look for an N in the third position
            if seq[tfFix+2] == 'N':
                # Use a for loop to set 3rd position
                # to TCA and G respectively
                for nuc in 'TCAG':
                    seq[tfFix+2] = nuc 
                    codon = seq[tfFix:tfFix+3]
                    codon = ''.join(codon)
                    aa = codons.get(codon,'X')
                    checkSet.add(aa)
                # If the codons all produce the same amino
                # acid, the set's length should only be 1
                ## At no pt should all of the 4 possiblities
                ## result in an X, so this solution should work
                ## a simple check howerver may be to see if X exists
                ## in the set
                if len(checkSet) == 1:
                    seq[tfFix+2] = 'T'
                    print "T at index", tfFix+2, "is used in place of the N nucleotide provided"
                    print "The bp at this position, due to degeneracy of the code, allows it to be any"
                    print "nucleotide"
                else:
                    seq[tfFix+2] = 'N'
            print seq[tfFix+2],
    seq = ''.join(seq)                
    return seq
                
        
        
                


# Call the appropriate functions to get the codon table and the sequence
seq = readseq(seqfile)
codons,init = readcodons(codonfile)
seq = fixN(codons,seq,1)
print "Translation for the first translation frame: \n", trans(codons,fixN(codons,seq,1),1)
print "Translation for the second translation frame: \n", trans(codons,fixN(codons,seq,2),2)
print "Translation for the third translation frame: \n",trans(codons,fixN(codons,seq,3),3)
print "Translation for the first reverse complement frame: \n", trans(codons,RevComp(fixN(codons,seq,1),1)
print "Translation for the second reverse complement frame: \n", trans(codons, RevComp(fixN(codons,seq,2),2)
print "Translation for the third reverse complement frame: \n", trans(codons, RevComp(fixN(codons,seq,3),3)

