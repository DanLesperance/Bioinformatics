import sys
from Bio import SeqIO
from Bio import Seq
from Bio.Alphabet import IUPAC

handle = sys.argv[1]
sequence = ''
count = 1
intron = ''
for seqrec in SeqIO.parse(handle,'fasta'):
    #print(count)
    if count == 1:
        sequence = str(seqrec.seq)
        count+=1
        #print(sequence)
    else:
        intron = str(seqrec.seq)
    sequence = sequence.replace(intron,'')
#print(sequence)
#print(intron)

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC



mRNA = sequence
mRNA = mRNA.upper()

mRNA = Seq(mRNA,IUPAC.unambiguous_dna)
trans = mRNA.translate()
print(trans[0:-1])
