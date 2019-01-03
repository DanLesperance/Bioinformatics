import xml.etree.ElementTree as ET
import sys
import gzip

## Arguments
#Set up user specified arguments as necessary and check for their accuracy
#to work in the program
f = sys.argv[1]
if not 'mzxml.gz' in f:
    print >> sys.stderr, 'Please provide a mzxml.gz file for the first argument'
    sys.exit()

sc = sys.argv[2]
try:
    test = int(sc)
    if sc >1700 and sc < 200 :
        print >> sys.stderr, 'Please use a value greater than 200 and less than 1700 for a scan number'
        sys.exit()
except ValueError:
    print >> sys.stderr, 'Please provide an integer for scan number as the second argument'
    sys.exit()
    
peptideSeq = sys.argv[3]
peptideSeq = peptideSeq.upper()
valid_sym = 'ACDEFGHIKLMNPQRSTVWY'
for pep in peptideSeq:
    if not pep in valid_sym:
        print >> sys.stderr, 'Please provide a valide peptide sequence for the third argument'
        sys.exit()

try:
    if sys.argv[4].upper() in 'Y B ALL':
        ion = sys.argv[4]
        ion = ion.upper()
    else:
        print >> sys.stderr, 'Please provide B, Y, or All for Ion output (4th arg)'
        sys.exit()
except IndexError:
    ion = 'ALL'
    pass


xmlDoc= gzip.open(f)
ns = ''
scan_count = 1



#Parse down to B64 peak read for specified scan value
for event,ele in ET.iterparse(xmlDoc):
    if ns =='':
        p = ele.tag.find('}')
        if p >= 0:
            ns = ele.tag[:(p+1)]
    if event == 'end' and ele.tag == ns+'scan':
        if scan_count == int(sc):
            for child in ele:
                if child.tag == ns+'peaks':
                    c = child.text
        scan_count = scan_count+1



from base64 import b64decode
from array import array

#decode the b64 and set up the arrays
peaks = array('f',b64decode(c))
if sys.byteorder != 'big':
        peaks.byteswap()
mzs = peaks[::2]
ints = peaks[1::2]

#peaks[2*(i-1)]   is the m/z value of the ith peak (i=1,2,3,4,...)
#peaks[2*(i-1)+1] is the intensity value of the ith peak (i=1,2,3,4,...)
#mzs[i-1] is the m/z value of the ith peak
#ints[i-1] is the intensity value of the ith peak

mw = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
          'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
          'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
          'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06 }
valid_sym = 'ACDEFGHIKLMNPQRSTVWY'


b = 1
y = 19
revPep = peptideSeq[::-1]


##Start to mass spec plot
#Foundations: scale, plot, label
import matplotlib.pyplot as pyp
from sklearn import preprocessing as preproc
min_max = preproc.MinMaxScaler(feature_range=(0,100))
intsScaled = min_max.fit_transform(ints)
fig, ax = pyp.subplots()
pyp.bar(mzs,intsScaled)
ax.set_xlabel('m/z \n'"**B and Y Ions calculated using molecular weight of G=58 Daltons**")
ax.set_ylabel('Intensity %')
ax.set_title('Mass Spec')

#Create instance for textfile to write into
file1 = open(sc+peptideSeq+'.txt','w')

#Match and calculate B and Y Ions along with annotation if match occurs
#Write in what matches occur into text file as well
annotation = 0
bion_match = ''
file1.write('Query Sequence' +' '+ peptideSeq+ '\n\n')
for let in peptideSeq:
    b = mw.get(let)+ b
    for m in range(0,len(mzs)):
        if mzs[m] > mzs[m-1]+3 or mzs[m] == mzs[0]:
            if (int(mzs[m])-2)<= b <= (int(mzs[m]+2)):
                bion_match = bion_match + str(let)
                annotation = intsScaled[m]+0.1*m
                if annotation > 100:
                    annotation = 90
                file1.write(str(let)+ ' ' + str(mzs[m]) + ' ' +'B Ion\n')
                if ion in 'B ALL':
                    pyp.text(mzs[m],annotation,str(let),color='blue')
                    pyp.text(mzs[m]-30,annotation+3, round(mzs[m],1),color='blue')
file1.write('B Ion matched to' + ' '+ bion_match+'\n\n')
yion_match = ''
for let in revPep:
    y = mw.get(let) + y
    for m in range(0,len(mzs)):
        if mzs[m] > mzs[m-1]+3 or mzs[m] == mzs[0]:
            if (int(mzs[m])-2)<= y <= (int(mzs[m]+2)):
                yion_match = yion_match + str(let)
                annotation = intsScaled[m]+0.1*m
                if annotation > 100:
                    annotation = 90
                file1.write(str(let) + ' ' + str(mzs[m]) + ' '+'Y Ion\n')
                if ion in 'Y ALL':
                    pyp.text(mzs[m]-30, annotation+3,round(mzs[m],1), color='red')
                    pyp.text(mzs[m], annotation , str(let), color='red')
file1.write('Y Ion matched to' + ' '+ yion_match+'\n')

#Final annoations in the plot, last minute useful information                
pyp.text(mzs[-1]-50,108,'Full:'+' '+peptideSeq)
pyp.text(mzs[-1]-50,104,'B Ion:'+' '+bion_match,color ='blue')
pyp.text(mzs[-1]-50,101,'Y Ion:'+' '+yion_match[::-1], color='red')

file1.close()

pyp.show()


