import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

handle = sys.argv[1]

for seq_rec in SeqIO.parse(handle,'fasta'):
    N=str(seq_rec.seq)
nuc = 0
st=0
peptide = []

for nuc in range(0,len(N)):
    if N[nuc:nuc+3] == 'ATG':
        cds=N[nuc:]
        prot = Seq(cds, IUPAC.unambiguous_dna)
        prot= prot.translate(to_stop=True)
        if len(prot)*3+nuc< len(N):

            peptide.append(str(prot))
    if nuc<st:
        continue


N = Seq(N, IUPAC.unambiguous_dna)
N = str(N.reverse_complement())

for NUC in range(0,len(N)):
    if N[NUC:NUC+3]=='ATG':
        CDS = N[NUC:]
        PROT = Seq(CDS, IUPAC.unambiguous_dna)
        PROT = PROT.translate(to_stop=True)
        if len(PROT)*3+NUC < len(N):

            peptide.append(str(PROT))
peptide=set(peptide)
peptide = '\n'.join(peptide)
print(peptide)
