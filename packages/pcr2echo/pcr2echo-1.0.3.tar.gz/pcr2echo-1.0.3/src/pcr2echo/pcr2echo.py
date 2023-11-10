#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import openpyxl
import os

file = input('Enter path to the PCR Echo assembly sheet:') #e.g r'C:\Users\egar1\OneDrive\Documents\GDEC\Automation_scripts\Echo\DestinationPlate96\PCR_template2.xlsx'
file = file.strip('"')

primers = pd.read_excel(io=file)
df = pd.read_excel(file).dropna()

directory = os.path.dirname(file)
#print(directory)

destination_path = os.path.join(directory,'EchoTransferCSV')
if not os.path.exists(destination_path):
    os.makedirs(destination_path)
    
source_path = os.path.join(directory,'SourcePlate96')
if not os.path.exists(source_path):
    os.makedirs(source_path)

print('Created Source and Destination folders')

job = input('Enter the project ID:')


# In[2]:


def record (table, SP_type, Qtile):
    #Set save locations
    Version = input('File version number: ')
    prefix = source_path
    suffix=f'ESP96_{job}_Quartile{Qtile}_{SP_type}_{Version}.xlsx'
    outfile = os.path.join(prefix,suffix)
    
    # Create an Excel writer object
    writer = pd.ExcelWriter(outfile, engine='openpyxl')
    table.to_excel(writer, sheet_name='Sheet1', startrow = 0, index=True)
    
    # Save the changes
    writer.save()
    writer.close()
    
    #print (f'File saved {outfile} ')
    


# In[3]:


def record_dest(table):
    Version = input('File version number: ') 
    
    prefix = destination_path
    suffix=f'EchoTransfer_{job}_{Version}.csv'
    final = os.path.join(prefix,suffix)
    print(final)
    table.to_csv(final, index=False)    


# In[4]:


#Template plasmid Source96 plate
wells = [
    'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
    'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
    'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
    'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
    'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
    'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
    'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
    'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8',
    'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9',
    'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10',
    'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11',
    'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12'
]

n=0
ZourcePlate96 = {}
group_dict = {}

dead_volume = 25 #uL
max_volume = 55

df2 = df.set_index('Fragment_name', inplace=False)
plasmid_source = []

# group the dataframe by 'Template plasmid' and store them in the dictionary
for name, group in df.groupby('Template_plasmid'):
    group_dict[name] = group['Fragment_name'].tolist()

test = df.groupby('Template_plasmid')

#print('df.groupby(template plasmid', test.head())

# Within each group of template plasmid transfers ...
for group_name in group_dict.keys():
    group_list = group_dict[group_name]
    #print('group list', group_list)
    uL = dead_volume

# ... lookup the transfer volume
    for j, value in enumerate(group_list):
        #print('j: ', j)
        #print('value', value)
        transfer_vol = df2.loc[df2.index == value, 'Plasmid_transfer_volume_nL'].values[0] 
        transfer_vol = transfer_vol/1000
        current_well = wells[n]
        
        #Decide if transfers will come from the same well, or if it will come from a new well.      
        if (transfer_vol + uL <= max_volume) and j < (len(group_list)-1):
            uL = uL + transfer_vol
            plasmid_source.append(current_well)
        elif j == (len(group_list)-1):
            uL = uL + transfer_vol 
            ZourcePlate96.update({current_well: [group_name, uL]})
            plasmid_source.append(current_well)
            n=n+1
            uL = dead_volume
        else:
            n=n+1
            ZourcePlate96.update({current_well: [group_name, uL]})
            plasmid_source.append(current_well)
            uL = dead_volume
            
#print('ZourcePlate96', ZourcePlate96)            
#Use this later to lookup the source wells
#This plasmid source well is just randomly slapped on and is not linked to the samples???
#print('plasmid source', plasmid_source)
df2 = df.set_index('Fragment_name', inplace=False)
df2['Plasmid source well 96'] = plasmid_source
#print('df2',df2)

#Source plate 96 for plasmid template
dfS = pd.DataFrame(data=ZourcePlate96).transpose(copy=True)
dfS.reset_index(inplace=True)
dfS.columns=['Well','Sample', 'Volume (uL)']

#print(dfS)
record(table=dfS, SP_type='Template', Qtile='1')


# In[5]:


#Water Source96 plate
n=0
sourcePlate96 = {}
group_dict = {}
waterSource96 = []

dead_volume = 25 #uL
max_volume = 55
uL = dead_volume

# iterate over each unique group and retrieve values from column 1
for i in df['Fragment_name']:
    #print(i)
    transfer_vol = df2.loc[df2.index == i, 'Water transfer (uL)'].values[0] 
    current_well = wells[n]
    if (transfer_vol + uL <= max_volume):
        uL = uL + transfer_vol
        waterSource96.append(current_well)
        
    elif j == (len(df)-1):
        uL = uL + transfer_vol 
        sourcePlate96.update({current_well: ['Water', uL]})
        waterSource96.append(current_well)
        n=n+1
        uL = dead_volume
        
    else:
        n=n+1
        waterSource96.append(current_well)
        sourcePlate96.update({current_well: ['Water', uL]})
        uL = dead_volume


#print('waterSource96',waterSource96)
#print('sourcePlate96',sourcePlate96)
#Create new column with transfer well info
df2['Water source well 96'] = waterSource96

#Source plate 96 for water transfers
dfS2 = pd.DataFrame(data=sourcePlate96).transpose(copy=True)
dfS2.reset_index(inplace=True)
dfS2.columns=['Well', 'Sample', 'Volume (uL)']
#print(dfS2)
#record(dfS2, SP_type='Water', Qtile='3')
#print('Saving water source plate')


# In[6]:


#Water Source96 plate
n=0
sourcePlate96 = {}
group_dict = {}
waterSource96 = []

dead_volume = 25 #uL
max_volume = 55
uL = dead_volume

# iterate over each unique group and retrieve values from column 1
counter = 0
for i in df['Fragment_name']:
    print('i', i)
    counter = counter+1
    print('counter', counter)
    
    transfer_vol = df2.loc[df2.index == i, 'Water transfer (uL)'].values[0] 
    current_well = wells[n]
    print('current well', current_well)
    
    if counter == (len(df)) and (transfer_vol + uL <= max_volume):  #if you're on the last well, add the sourcePlate96 entry.
        print('LAST OPTION')
        uL = uL + transfer_vol 
        sourcePlate96.update({current_well: ['Water', uL]})
        waterSource96.append(current_well)
        n=n+1
    
    elif (transfer_vol + uL <= max_volume):
        print('FIRST OPTION')
        uL = uL + transfer_vol
        waterSource96.append(current_well) #record a transfer from the current well
        
    else:
        print('NEW WELL')
        sourcePlate96.update({current_well: ['Water', uL]}) #This is how much total water should be transferred to the well we just ended
        n=n+1 #update to a new well
        uL = dead_volume #reset well to be empty (except dead volume)
        uL = uL + transfer_vol  #start adding up the total transfer volume for this well
        waterSource96.append(current_well) #record a transfer from the current (new) well
        

print('waterSource96',waterSource96)
print('sourcePlate96',sourcePlate96)
#Create new column with transfer well info
df2['Water source well 96'] = waterSource96

#Source plate 96 for water transfers
dfS2 = pd.DataFrame(data=sourcePlate96).transpose(copy=True)
dfS2.reset_index(inplace=True)
dfS2.columns=['Well', 'Sample', 'Volume (uL)']
print(dfS2)
record(dfS2, SP_type='Water', Qtile='3')
print('Saving water source plate')


# In[7]:


# Generate 384W SP well map
SP384 = []
rows = 'ABCDEFGHIJKLMNOP'
cols = []
for n in range (1,25):
    cols.append(n)

aRows = rows[slice(0,25,2)]
bRows = rows[slice(1,25,2)]
#print(aRows, bRows)

oneCol = cols[slice(0,25,2)]
twoCol = cols[slice(1,25,2)]
#print(oneCol, twoCol)

wellsQ1 =[]
for i in aRows:
    for j in oneCol:
        wellsQ1.append(i+str(j))

wellsQ2 =[]
for i in aRows:
    for j in twoCol:
        wellsQ2.append(i+str(j))    

wellsQ3 =[]
for i in bRows:
    for j in oneCol:
        wellsQ3.append(i+str(j))
        
wellsQ4 =[]
for i in bRows:
    for j in twoCol:
        wellsQ4.append(i+str(j))

#96 well plate by row
SP96 = []
rows96 = 'ABCDEFGH'
cols96 = []
for n in range (1,13):
    cols96.append(n)

for i in rows96:
    for j in cols96:
        SP96.append(i+str(j))

#This is the mapping of wells for each of the 4 quartiles in the 384-well plate
Q1map = {}  
for idx, i in enumerate(SP96):
    Q1map.update({i:wellsQ1[idx]})
print("Q1map: ", Q1map)
print("")
dfQ1map = pd.DataFrame(data=(Q1map), index=[x for x in range(0,96)])
#print(dfQ1map)

Q2map = {}  
for idx, i in enumerate(SP96):
    Q2map.update({str(i):str(wellsQ2[idx])})  
print("Q2map: ", Q2map)
print("")

Q3map = {}
for idx, i in enumerate(SP96):
    Q3map.update({str(i):str(wellsQ3[idx])})  
print("Q3map: ", Q3map)
print("")

Q4map = {}
for idx, i in enumerate(SP96):
    Q4map.update({str(i):str(wellsQ4[idx])})  
print("Q4map: ", Q4map)
print("")


# In[8]:


#Create a dataframe to link the fragment name, template plasmid, sourceplate 96, and sourceplate 384

mapped_templates = []
for i in df['Fragment_name']:
    plasmid = (df.loc[df['Fragment_name']==i, 'Template_plasmid']).values
    mapped_templates.extend({'Fragment_name': i, 'Template_plasmid': p} for p in plasmid) 
frag_temp = pd.DataFrame(mapped_templates)


sp = pd.DataFrame(ZourcePlate96).transpose()
sp2 = sp.reset_index(drop=False)
# This will change the column names in place without needing to assign the result back to 'df'
sp2.rename(columns={'index': 'Wells', 0: 'Sample', 1: 'Volume'}, inplace=True)
#print(sp2)

sp96_map = []
for i in sp2['Sample']:
    name = (sp2.loc[sp2['Sample']==i, 'Wells']).values
    sp96_map.extend({'Template_plasmid': i, 'SP96_Wells': x} for x in name) 
temp_sp96 = pd.DataFrame(sp96_map)
#print(temp_sp96)

merge1 = frag_temp.merge(temp_sp96, how='left', left_on='Template_plasmid', right_on='Template_plasmid')
#print(merge1)

sp384_map = []  ### requires the quartile mapping code to be run first
ice = []
for i in merge1['SP96_Wells']:
    ice.append(i)
    mapped_value = Q1map[i]
    sp384_map.append(mapped_value)
df_new = pd.DataFrame({'SP384_Wells':sp384_map, 'SP96_Wells': ice})
#print(df_new)

LinkedTemplates = merge1.merge(df_new, how='left', left_on='SP96_Wells', right_on='SP96_Wells')
#LinkedTemplates


# In[9]:


#The plasmid template, primer, and water excel SP96 files are downloaded and correspond to individual quartiles of the 384-W plate.
#Since the primers are ordered from a plate, then just upload it as Q2
Q2_file = input('Enter file path to the primer source plate.  Columns must be named '"Sample"' and '"Well"': ')
Q2_file = Q2_file.strip('"')
           
#Create dataframe from excel
dfQ2 = pd.read_excel(Q2_file).dropna()
dfQ2.set_index('Sample', inplace=True)
#print('dfQ2',dfQ2)

#For each well of the 96w source plate, map the corresponding well from the 384w plate.
#Q1mapped = [Q1map[i] for i in df2['Plasmid source well 96']]

#print('DF2', df2)
Q1mapped = []
for i in df2['Plasmid source well 96']:
    mapped_value = Q1map[i]
    Q1mapped.append(mapped_value)
    

#Make a tuple of all the primers that will be transferred from df2, then look up the source well 96 from the Q2 spreadsheet.
FragmentPrimer = df[['Fragment_name','Primer 1','Primer 2']]
allPrimers =[]
for primer in df['Primer 1'], df['Primer 2']:
    allPrimers.append(primer)
    
Fdf = pd.DataFrame(data=[])
Rdf = pd.DataFrame(data=[])
Fprimer = []
Rprimer = []
for frag in df['Fragment_name']:
    Fprimer.append(df2.loc[frag, 'Primer 1'])
    Rprimer.append(df2.loc[frag, 'Primer 2'])
Fdf['Primers'] = Fprimer
Fdf['Fragment_name'] = [x for x in df['Fragment_name']]
Rdf['Primers'] = Rprimer
Rdf['Fragment_name'] = [x for x in df['Fragment_name']]

allPrimers = Fdf.merge(right=Rdf, how='outer')

pMap96 = []
for n in allPrimers['Primers']:
    pMap96.append(dfQ2.loc[n,'Well'])
allPrimers['SourceWell96'] = pMap96

pMap384 = []
for n in allPrimers['SourceWell96']:
    pMap384.append(Q2map[n])
allPrimers['SourceWell384'] = pMap384

allPrimersT = allPrimers.merge(right=df, how = 'left')
allPrimersT.set_index('Primers', inplace = True)
#print(allPrimers)

transf384 = []
for n in allPrimersT['Fragment_name']:
    transf384.append(df2.loc[n,'uL_primer'])
allPrimersT['primer_transfer'] = transf384

Q3mapped = [Q3map[i] for i in df2['Water source well 96']]   


df_mapped = df['Template_plasmid']
#print('Q1 mapped', Q1mapped)

#for i in df_mapped:
list1 = LinkedTemplates['SP384_Wells'].to_list()

#Create a new dataframe with the mapped 384plate source well.
tf_df = pd.DataFrame(index=df['Fragment_name'], data={'Plasmid Source Well 384':list1, 
                                                     'Water source well 384': Q3mapped})

#print('tfdf', tf_df)
#print(allPrimersT)


# In[10]:


SP384name = '384PP_BP' #input('Source plate name: ')
DP96name = 'AB0080_Thermo_96_plate' #input('Destination plate name: ')


# In[11]:


#Primer transfers
echo_df = pd.DataFrame(data={'Source Well': allPrimersT['SourceWell384'], 'Destination Well': allPrimersT['Destination well'], 
                             'Transfer Volume': allPrimersT['uL_primer']*1000, 'Molecule': allPrimersT.index})
echo_df.reset_index(inplace=True)
echo_df2= echo_df[['Source Well', 'Destination Well', 'Transfer Volume', 'Molecule']]
#print(echo_df2)


# In[12]:


#Add the plasmid transfers to the Echo CSV dataframe

#For each fragment (unique PCR), look up the plasmid template used
template_name = [df2.loc[i,'Template_plasmid'] for i in df['Fragment_name']]
#print('template name', template_name)

#For each fragment (unique PCR), look up the plasmid transfer volume 
plas_transfer = [float(df2.loc[i, 'Plasmid_transfer_volume_nL']) for i in df['Fragment_name']] #nL transfer

#For each fragment (unique PCR), look up the destination well 
destWell = [(df2.loc[i, 'Destination well']) for i in df['Fragment_name']] #nL transfer

#Look up the source well
template_SW = [tf_df.loc[n,'Plasmid Source Well 384'] for n in df['Fragment_name']]  #Fix, the tf_df is not correctly mapped!!!

#Create Echo transfer dataframe and merge with the existing one
plasmid_df = pd.DataFrame(data={'Source Well': template_SW, 'Transfer Volume': plas_transfer, 'Destination Well': destWell, 'Molecule': template_name})
#print('plasmid_df', plasmid_df)
merged2 = echo_df2.merge(right=plasmid_df, how='outer')
#print('merged2', merged2)

#print(merged2)


# In[13]:


#Add the water transfers to the Echo CSV dataframe

#For each fragment (unique PCR), look up the plasmid template used
template_name = [df2.loc[i,'Template_plasmid'] for i in df['Fragment_name']]

#For each fragment (unique PCR), look up the plasmid transfer volume 
water_transfer = [float(df2.loc[i, 'Water transfer (uL)']*1000) for i in df['Fragment_name']] #nL transfer

#Look up the source well
water_SW = [tf_df.loc[n,'Water source well 384'] for n in df['Fragment_name']]

#Create Echo transfer dataframe and merge with the existing one
water_df = pd.DataFrame(data={'Source Well': water_SW, 'Transfer Volume': water_transfer, 'Destination Well': destWell, 'Molecule': 'Water'})
merged3 = merged2.merge(right=water_df, how='outer')
merged3['Source Plate Name'] = SP384name
merged3['Destination Plate Name'] = DP96name

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
#reset display
#pd.reset_option('all')
#display(merged3)

#TODO add error handling for negative values 


# In[14]:


record_dest(merged3)
print("Done")

