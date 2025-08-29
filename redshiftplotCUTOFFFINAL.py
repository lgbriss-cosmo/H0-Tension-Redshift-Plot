# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 18:41:18 2025

@author: lucyg
"""

import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as mcolors
from matplotlib.backends.backend_pdf import PdfPages
#from matplotlib.gridspec import GridSpec

#import and process data

### Repository containing the .csv with the dataset

#PLEASE NOTE: REDSHIFT LOWER LIMITS HAVE BEEN GREATLY EXAGGERATED FOR DISPLAY ON THE FOLLOWING:
    # CMB OBSERVATIONS HAVE A LOWER LIMIT OF 900
    # GW OBSERVATION GW170817 HAS A LOWER LIMIT OF 0.42
    # FOR ACCURATE REDSHIFT PLEASE CONSULT THE NON-EXAGGERATED FILE
data_path = "C:\\Users\\lucyg\\Documents\\PhD\\H0tensionredshiftplot\\"
fil = data_path+'datasetredshiftEXAGGERATED.csv'

# Impose cutoffs
# measurement_no_cutoff: Use measurement_no_cutoff number of measurements for each data type
measurement_no_cutoff = None
# accuracy_cutoff: Use only the measurements which have 2 sigma<accuracy_cutoff in km s-1 Mpc-1
accuracy_cutoff = 4
# date_cutoff: Use only measurements obtained after the year data_cutoff
date_cutoff = 2015

### Load the dataset and count the number of data points
nr=1
with open(fil, 'r+') as file:
    reader = csv.reader(file)
    first_line = file.readline()
    next(reader, None)
    for row in reader:
        nr += 1
    nc = first_line.count(',')+1
    
### Load the data points into arrays
H0 = np.zeros(nr)
Hl = np.zeros(nr)
Hp = np.zeros(nr)
redshiftlower = np.zeros(nr)
redshiftupper = np.zeros(nr)
additionaldatasets = ["" for x in range(nr)]
method = ["" for x in range(nr)]
lbl    = ["" for x in range(nr)]
auth   = ["" for x in range(nr)]
etal   = ["" for x in range(nr)]
year   = ["" for x in range(nr)]
set    = ["" for x in range(nr)]
arxiv = ["" for x in range(nr)]

i=0
with open(fil, 'r+') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        method[i] = row[0]
        lbl[i]    = row[1]
        auth[i]   = row[2]
        etal[i]   = row[3]
        year[i]   = row[4]
        set[i]    = row[5]
        H0[i] = float(row[6])
        Hl[i] = float(row[7])
        Hp[i] = float(row[8])
        arxiv[i] = row[9]
        redshiftlower[i] = float(row[10])
        redshiftupper[i] = float(row[11])
        additionaldatasets[i] = row[12]
        i += 1

#empty lists of arrays of rectangles

baowithplanckarray = []
cmbwithplanckarray = []
cmbwithoutplanckarray = []
nocmbwithbbnarray = []
cmblensingarray = []

cepheidssn1aarray = []
trgbsn1aarray = []
mirassn1aarray = []
masersarray = []
tullyfisherarray = []
surfacebrightnessarray = []
sniiarray = []
hiigalaxiesarray = []
stronglensingarray = []
lensingrelatedarray = []
gwrelatedarray = []

arraylist = [baowithplanckarray,cmbwithplanckarray,cmbwithoutplanckarray,nocmbwithbbnarray,cmblensingarray,cepheidssn1aarray,trgbsn1aarray,mirassn1aarray,masersarray,tullyfisherarray,surfacebrightnessarray,sniiarray,hiigalaxiesarray,stronglensingarray,lensingrelatedarray,gwrelatedarray]

#empty lists of rectangles

baowithplanck = []
cmbwithplanck = []
cmbwithoutplanck = []
nocmbwithbbn = []
cmblensing = []

cepheidssn1a = []
trgbsn1a = []
mirassn1a = []
masers = []
tullyfisher = []
surfacebrightness = []
snii = []
hiigalaxies = []
stronglensing = []
lensingrelated = []
gwrelated = []

listsofrectangles = []#[baowithplanck,cmbwithplanck,cmbwithoutplanck,nocmbwithbbn,cmblensing,cepheidssn1a,trgbsn1a,mirassn1a,masers,tullyfisher,
#surfacebrightness,snii,hiigalaxies,stronglensing,lensingrelated,gwrelated]
colourlist=['cornflowerblue','b','mediumspringgreen','midnightblue','c','r','y','m','tab:brown','tab:purple','lime','orangered',
            'g','darkslategray','lightcoral','darkorchid','rosybrown','maroon','darkgreen','slateblue','tab:orange',
            'olivedrab']
unsortedlabellist=list(dict.fromkeys(lbl))

#build rectangle lists

for i in range(nr):
    if auth[i]=='0':
        continue
    elif date_cutoff!=None and float(year[i])<date_cutoff:
        continue
    elif accuracy_cutoff!=None and Hl[i]+Hp[i]>accuracy_cutoff:
        continue
    elif method[i]=='Indirect':
        if lbl[i]=='BAO with Planck':
            baowithplanckarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        if lbl[i]=='CMB with Planck':
            cmbwithplanckarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='CMB without Planck':
            cmbwithoutplanckarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='No CMB; with BBN':
            nocmbwithbbnarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='Pl(k) + CMB lensing':
            cmblensingarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
    elif method[i]=='Direct':
        if lbl[i]=='Cepheids-SNIa':
            cepheidssn1aarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='TRGB-SNIa':
            trgbsn1aarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='Miras-SNIa':
            mirassn1aarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='Masers':
            masersarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='Tully-Fisher Relation':
            tullyfisherarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='Surface Brightness Fluctuations':
            surfacebrightnessarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='SNII':
            sniiarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='HII galaxies':
            hiigalaxiesarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='Strong Lensing; mass model-dependent':
            stronglensingarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='Lensing related; mass model-dependent':
            lensingrelatedarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])
        elif lbl[i]=='GW related':
            gwrelatedarray.append([Hl[i]+Hp[i],mpl.patches.Rectangle((H0[i]-Hl[i],redshiftlower[i]),Hp[i]+Hl[i],redshiftupper[i]-redshiftlower[i]),lbl[i],method[i],colourlist[unsortedlabellist.index(lbl[i])]])

#make a list of remaining labels after cuts
fulllistoflabels=[]
for array in arraylist:
    for measurement in array:
        fulllistoflabels.append(measurement[2])

remaininglabels=list(dict.fromkeys(fulllistoflabels))
print(remaininglabels)

#sort each patch list in order of uncertainty, largest to smallest
for i in range(len(arraylist)):
    list.sort(arraylist[i], key=lambda measurement: measurement[0],reverse=True)
    if measurement_no_cutoff!=None and len(arraylist[i])>measurement_no_cutoff:
        arraylist[i]=arraylist[i][-measurement_no_cutoff:]

manualsortlist=['Lensing related; mass model-dependent','Pl(k) + CMB lensing','Strong Lensing; mass model-dependent',
           'GW related','SNII','Surface Brightness Fluctuations','Tully-Fisher Relation','HII galaxies','Miras-SNIa',
           'Masers','TRGB-SNIa','Cepheids-SNIa','BAO with Planck','CMB without Planck','CMB with Planck','No CMB; with BBN']

#print(len(manualsortlist))
#print(manualsortlist)

manualsortlist=[x for x in manualsortlist if x in remaininglabels]

#print(len(manualsortlist))
#print(manualsortlist)
#print(arraylist)

arraylist = [x for x in arraylist if x!=[]]
#print(arraylist)

#for i in range(len(arraylist)):
   # print(arraylist[i][0][2])
    #print(manualsortlist.index(arraylist[i][1][2]))

def sortmeasurements(sort_type,orderofsort=[]):
    '''Sorts the types of measurements into a plotting order, with the last elements in the list plotted over the first. 
        - sort_type "manual" sorts the list according to a user-specified order
        - sort_type "automatic" sorts the list from largest to smallest uncertainty'''
    global labellist
    if sort_type=='manual':
        labellist=orderofsort
        list.sort(arraylist, key=lambda measurementlist: labellist.index(measurementlist[0][2]))
        for i in range(len(arraylist)):
            rectangleslist=[]
            colourlist[i]=arraylist[i][0][4]
            for k in range(len(arraylist[i])):
                rectangleslist.append(arraylist[i][k][1])
            listsofrectangles.append(rectangleslist)
    elif sort_type=='automatic':
        list.sort(arraylist, key=lambda measurementlist: measurementlist[-1][0],reverse=True)
        for i in range(len(arraylist)):
            rectangleslist=[]
            labellist.append(arraylist[i][0][2])
            colourlist[i]=arraylist[i][0][4]
            for k in range(len(arraylist[i])):
                rectangleslist.append(arraylist[i][k][1])
            listsofrectangles.append(rectangleslist)
    
listsofrectangles=[x for x in listsofrectangles if x!=[]]

#print(manualsortlist)

sortmeasurements('manual',manualsortlist)

# alpha (transparency) of each data type - this is for the SORTED LIST, with more transparent patches in the background
importantalpha=0.9
unimportantalpha=0.4
mimportantalpha=0.6

alphalist=[]

# Set transparency on a gradient

#for i in range(len(manualsortlist)):
#    alphalist.append(unimportantalpha+(importantalpha-unimportantalpha)*i/(len(manualsortlist)))
    
# else set a flat transparency

alphalist = [0.9 for i in range(len(manualsortlist))]
    
#alphalist[3]=0.9

#alphalist=[0.9,0.4,0.4,0.4,0.4,0.6,0.6,0.6,0.6,0.9,0.9,0.9,0.9,0.9,0.9]

#________PLOT__________#

pdf = PdfPages('H0redshiftCUTOFF.pdf')


fig, ax = plt.subplots(nrows=1,ncols=2,sharex=True,figsize=(10,8),width_ratios=[7,1],dpi=300)

# build patch collections

listsofpatches=[]
print(len(listsofrectangles))
for i in range(len(listsofrectangles)):
    listsofpatches.append(mpl.collections.PatchCollection(listsofrectangles[i], alpha=alphalist[i],facecolors=colourlist[i],edgecolors='black'))

# empty patches for labels
emptypatchlist = [mpl.patches.Patch(color=colourlist[i],label=labellist[i]) for i in range(len(labellist))]

# lists of handles to pass to legends

handlelistdirect=[]
handlelistindirect=[]

for i in range(len(emptypatchlist)):
    if arraylist[i][0][3]=='Indirect':
        handlelistindirect.append(emptypatchlist[i])
    elif arraylist[i][0][3]=='Direct':
        handlelistdirect.append(emptypatchlist[i])
        
# plot patch collections

for i in range(len(listsofpatches)):
    ax[0].add_collection(listsofpatches[i])

### Plot SH0eS and Planck lower and upper measurements as dotted lines for reference
ax[0].vlines([73.04-1.04,73.04+1.04,67.4-0.5,67.4+0.5],0,1089,colors=['maroon','maroon','blue','blue'],linestyles='dotted',label=['SH0ES lower','SH0ES upper','Planck lower', 'Planck upper'])

# set plot range
ax[0].set_xlim(65,78)
ax[0].set_ylim(10**-3,10**3.1)

# axes labels and scales
ax[0].set_xlabel('H0')
ax[0].set_ylabel('z')
ax[0].set_yscale('log')

# plot legends
indirectlegend = ax[1].legend(handles=handlelistindirect,ncol=1,loc='upper left',borderaxespad=0,title='Indirect Measurements')
ax[1].add_artist(indirectlegend)
ax[1].legend(handles=handlelistdirect,ncol=1,loc='center left',borderaxespad=0,title='Direct Measurements')
ax[1].axis('off')

# plot and save figure
plt.tight_layout()
pdf.savefig()
pdf.close()