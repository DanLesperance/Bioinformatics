##At the end should be a heatmap of differentially expressed genes
##btwn Thyroid and Adrenal glands in healthy patients


Brain_vs_Adrenal <- read.table(file='Galaxy110-[FeatureCounts_].tabular',sep=
                                 '\t',header=T)
head(Brain_vs_Adrenal)
AdrenBrainSamps <- read.table(file='AdrenalThyroid.txt',sep='\t',head=T,
                              row.names=1)
#Make all rows with duplicated genenames into d1 and rmv
d1 <- duplicated(Brain_vs_Adrenal$GENENAME)
sum(d1)
Brain_vs_AdrenalFixed<- Brain_vs_Adrenal[!d1,]

#Look into formatting and see if anything sticks out
#Rmv any missing values or odd values that are observed
head(Brain_vs_Adrenal[,2:8])
head(Brain_vs_Adrenal[,1])
AdrenBrainSamps
head(Brain_vs_AdrenalFixed)
missing <- is.na(Brain_vs_AdrenalFixed$GENENAME)
Brain_vs_AdrenalFixed <- Brain_vs_AdrenalFixed[!missing,]

#Rather than numbering row names, make the rownames the genename
rownames(Brain_vs_AdrenalFixed)<- Brain_vs_AdrenalFixed$GENENAME
#Make any columns you don't need NULL for DESeq analysis
Brain_vs_AdrenalFixed[,1] <- NULL
head(Brain_vs_AdrenalFixed)
Brain_vs_AdrenalFixed[,7]<- NULL

data_deseq <- DESeqDataSetFromMatrix(Brain_vs_AdrenalFixed,AdrenBrainSamps, design = ~1)
head(counts(data_deseq))
AdrenBrainSamps<- AdrenBrainSamps[-6,]
AdrenBrainSamps

nrow(data_deseq)
data_deseq <- data_deseq[rowSums(counts(data_deseq))>1,]
nrow(data_deseq)


rld <- rlog(data_deseq,blind=F)
sampleDists <- dist(t(assay(rld)))
sampleDists
colors <- colorRampPalette(rev(brewer.pal(9,'Blues')))(255)
pheatmap(sampleDistMatrix,clustering_distance_rows = sampleDists,
         clustering_distance_cols = sampleDists,col=colors)

geneVars <- rowVars(assay(rld))
geneVarsOrdered <- order(geneVars,decreasing=T)
topVarGenes <- head(geneVarsOrdered,50)
mat<- assay(rld)[topVarGenes,]
mat<- mat-rowMeans(mat)
df <- as.data.frame(colData(rld)[,c('Cell'),drop=F])
topGenesHeatmap <- pheatmap(mat)
