import sys
from Bio import SeqIO

handle = sys.argv[1]
for seqRec in SeqIO.parse(handle,'fasta'):
    DNA = seqRec.seq


def ReverseComplement(DNA):
    result = ""
    for i in range(len(DNA) - 1, -1, -1):
        if (DNA[i] == "A"):
            result += "T"
        elif (DNA[i] == "T"):
            result += "A"
        elif (DNA[i] == "C"):
            result += "G"
        else:
            result += "C"
    return result


def IsReverseComplement(strDNA):
    return (strDNA == ReverseComplement(strDNA))


def RestrictionSites(resDNA):
    resultList = []
    for i in range(4, 13):
        for j in range(0, len(resDNA) - i + 1):
            if (IsReverseComplement(resDNA[j:j + i])):
                resultList.append(str(j + 1) + ' ' + str(i))
    return resultList


for dna in RestrictionSites(DNA):
    print(dna)

