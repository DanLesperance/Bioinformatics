import sys
seq_handle = sys.argv[1]
seq_file = open(seq_handle)
seq = ''.join(seq_file.read().split())
seq = seq.upper()
seq_file.close()



def nucFreq(seq):
    freq = {'A':0, 'T':0, 'G':0, 'C':0}
    for nuc in seq:
        value = freq.get(nuc,'X')
        if not value == 'X':
            value = value+1
            freq[nuc] = value
    sortedFreq =sorted(freq.items(), key=lambda p: p[1], reverse = True)
    return sortedFreq
print 'Here are the most prevalent to least prevalent nucleotides'
print nucFreq(seq)
print 'The original sequence was:'
print seq
print 'Any unconventional nucleotides were not counted in the frequency'
