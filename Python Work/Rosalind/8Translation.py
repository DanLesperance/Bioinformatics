from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

handle = sys.argv[1]
seq_file = open(handle)
mRNA = ''.join(seq_file.read().split())
mRNA = mRNA.upper()
seq_file.close()

mRNA = Seq(mRNA,IUPAC.unambiguous_rna)
trans = mRNA.translate()
print(trans[0:-1])
