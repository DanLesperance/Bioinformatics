setwd("C:/Users/Dan/Desktop/Armbruster Lab/Project")


##Load in Bam file and index into the bam info
library(Rsamtools)
bam <- scanBam('CAALB_20170711_K00134_IL100090633_ATTCAGAA-TAAGATTA-EC-31_L004_R1.fastq.gz.CL.PE.gz.cln.bam.srt.bam.rmDP.bam.RG.bam.mrg.bam')
bam[1]
bamInfo <- bam[[1]]
head(bamInfo)


##Understand what exists in each subset of the data to understand how R works with this data
#bamInfo$qname[1]
#bamInfo$flag
#length(bamInfo$pos)
#bamInfo$cigar 
bamInfo$pos
head(bamInfo)


##In order for manipulation, make the bam file into a DF
bamDF <- as.data.frame(bamInfo)
bamDF[1,]
is.na(bamDF$pos) #check df for any NA
bamDF$PosEnd <- bamDF$pos+bamDF$qwidth  #create an end position 
head(bamDF)
levels(bamDF$rname)


## Make a filtered bam file using DF 
# Check with indexing
bamDF[1,]
filteredBAM <- bamDF[-c(1,2,3),]
bamDF[1,]
filteredBAM[1,]
bamDF[4,]==filteredBAM[1,]

#Make Bam File 
write(filteredBam, file = 'FilteredBamFromR.bam',sep = "")