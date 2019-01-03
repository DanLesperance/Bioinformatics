setwd("C:/Users/Dan/Desktop/Armbruster Lab/Project")


##Load in Bam file and index into the bam info
library(Rsamtools)
filterbam <- scanBam('PicardBamFiltered.bam')

filterbamInfo <- filterbam[[1]]
head(filterbamInfo)


bamFilteredDF <- as.data.frame(filterbamInfo)
length(bamFilteredDF$pos)
length(bamDF$pos)
is.na(bamFilteredDF$pos) #check df for any NA
length(bamDF$pos)-length(bamFilteredDF$pos) #see how many reads were filtered out

#Compare with bamFilteredDF at same locations
#provides a list of True or False if the given start position
#exists at that index
bamDF$pos>1710 & bamDF$pos<1810 
bamDF$pos>1410 & bamDF$pos<1510
bamDF$pos>2010 & bamDF$pos<2110
bamFilteredDF$pos >1410 & bamFilteredDF$pos <1510
bamFilteredDF$pos >2010 & bamFilteredDF$pos <2110
bamFilteredDF$pos >1710 & bamFilteredDF$pos <1810

#see how many start positions within cutoffs exist in the data
length(bamFilteredDF$pos[(bamFilteredDF$pos >1710 & bamFilteredDF$pos <1810)])
length(bamDF$pos [(bamDF$pos>1710 & bamDF$pos<1810)])

#check to ensure the two files are similar the first 1 or 2 should be exactly the same 
head(bamDF$pos,50)
head(bamFilteredDF$pos,50)
head(bamDF)
head(bamFilteredDF)

