#input
#seq = 'AAAAAAAAAAAAAA'
#seq = 'CACACACACACAC'
seq = 'ATTCGATTCGATTCG'
#seq = 'TTAGCTTAGC'

def TandemRep(seq):
    HalfLength = len(seq)/2 
    answer = "There is not an integer number of tandem repeats"
    for i in range(0,HalfLength):
        #Do not want to divide by 0 (impossible) or by 1 (always == itself)
        if i ==0:
            i = HalfLength+1 
        elif i == 1:
            i = HalfLength+1
        #take a chunk of the sequence by some value
        chunk = len(seq)/i
        #see if that chunk multiplied by that value == to the entire seq
        if (seq[0:chunk]*i)==seq:
            print chunk
            answer = 'yes there exists a integer number of tandem repeats'
    print answer          
TandemRep(seq)       
     

