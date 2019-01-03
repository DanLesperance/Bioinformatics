setwd("C:/Users/Dan/Desktop/Armbruster Lab/Project")


##Load in Bam file and index into the bam info
library(Rsamtools)
bam <- scanBam('CAALB_20170711_K00134_IL100090633_ATTCAGAA-GCCTCTAT-EC-12_L004_R1.fastq.gz.CL.PE.gz.cln.bam.srt.bam.rmDP.bam.RG.bam.mrg.bam')
bam[1]
bamInfo <- bam[[1]]
head(bamInfo)


##Understand what exists in each subset of the data to understand how R works with this data
#bamInfo$qname[1]
#bamInfo$flag
#length(bamInfo$pos)
#bamInfo$cigar 



##In order for manipulation, make the bam file into a DF
bamDF <- as.data.frame(bamInfo)
bamDF[1,]
is.na(bamDF$pos) #check df for any NA
bamDF$PosEnd <- bamDF$pos+bamDF$qwidth  #create an end position 



#Use bamInfo to check position between cutoffs
#If the start position is within cutoff add to newList
newList<- ''

for(i in 1:length(bamInfo$pos)){
  if (bamInfo$pos[i]>1610){
    if (bamInfo$pos[i]<1910){
      newList<- c(newList,bamInfo$qname[i])
    }
  }
}

newList<- newList[-1] #Delete first value
length(newList)
class(bamInfo$pos[1]) #ensure $pos and $qwidth are integers for next steps
class(bamInfo$qwidth[1])

#Create a list of DF indeces 
#Where the End position is between the cutoffs
#Ie. DF[5] will go into the list as 5
#these will be used to index bamInfo qNames
posEndList<- c('')

for(i in 1:length(bamDF$PosEnd)){
  if(bamDF$PosEnd[i]>1610){
    if (bamDF$PosEnd[i]<1910){
      posEndList<- c(posEndList,i)
    }
  }
}
#check and remove first empty observation
posEndList
posEndList<- posEndList[-1]

#Use list provided from above to add to newlist
#indexing by numbers provided in list of DF indeces
#this will provide qnames indexed from above
for(i in 1:(length(posEndList)-1)){
  newList <- c(newList, bamInfo$qname[as.integer(posEndList[i])])
}

newList
length(newList)
duplicated(newList)#check if duplicates exist
length(newList[!duplicated(newList)])#check the length without duplicates against with duplicates
length(newlist)
#write to file
write(newList[!duplicated(newList)],file = 'readListForRemoval.txt',sep = "")


