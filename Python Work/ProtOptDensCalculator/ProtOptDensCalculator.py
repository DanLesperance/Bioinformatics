from scipy import stats
from prettytable import PrettyTable
import sys

#Stand_values will be pulled from file in future
#User specified values by prompt
standard = [0,1,2,4,8]
stand_values = [.093,.184,.266,.514,.892]
opt_dens = [.423,.444,.654,.234,.456,.865,.543]
dil_factor = int(input("What dilution factor was used \n"))
amt_of_prot = int(input("Please enter the micrograms of protein to utilize \n"))

#These values will be utilized for calculations of how much
#of each substance to add
slp, int, r, p, std_err = stats.linregress(standard,stand_values)

#Higher than .9 is generally allowed, but provides more confidence here
if r < 0.96:
    sys.stderr.write("Your standard does not follow a good linear regression")
    sys.exit()


#Calculate concentration, protein amount to add, and buffer to add
miG_per_miL = list(map(lambda x : (x-int)/slp, opt_dens))
protein = list(map(lambda x: (x*3)/amt_of_prot, miG_per_miL))
buffer = list(map(lambda x: 24-x-6, protein))

miG_per_miL_rounded = [round(elem,1) for elem in miG_per_miL]
prot_rounded = [round(elem,1) for elem in protein]
buf_rounded = [round(elem,1) for elem in buffer]


#Creation of table and file for table
opt_dens_Table = PrettyTable()

col_names = ["Protein ug/uL","Buffer", "Protein","Dye","Total"]

opt_dens_Table.add_column(col_names[0],miG_per_miL_rounded)
opt_dens_Table.add_column(col_names[1],buf_rounded)
opt_dens_Table.add_column(col_names[2],prot_rounded)
opt_dens_Table.add_column(col_names[3],[6]*len(buf_rounded))
opt_dens_Table.add_column(col_names[4],[24]*len(buf_rounded))

with open("Protein_Concentration.txt",'w') as w:
    w.write(str(opt_dens_Table))



