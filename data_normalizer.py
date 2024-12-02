import csv
import pandas as pd
df = pd.read_csv('train.csv')
#abstractText
df_2 = pd.read_csv('PubMed Multi Label Text Classification Dataset.csv')
bio_data = df_2['abstractText']

cs = df['Computer Science']
bio = df['Quantitative Biology']
phy = df['Physics']
fin = df['Quantitative Finance']
math = df['Mathematics']
text = df['ABSTRACT']
cs_list = []
bio_list= []
phy_list=[]
fin_list = list()
for index in range(0,len(cs)):
    if cs[index] == 1:
        cs_list.append(text[index])
    elif bio[index] == 1:
        bio_list.append(text[index])
    elif phy[index]==1:
        phy_list.append(text[index])
    elif fin[index]==1:
        fin_list.append(text[index])
    elif math[index] == 1:
        fin_list.append(text[index])
print('CS: '+str(len(cs_list)))
print('BIO: '+str(len(bio_list)))
print('PHY: '+str(len(phy_list)))
print('FIN: '+str(len(fin_list)))
all_data = list()
for item in cs_list[4000:4500]:
    all_data.append(item)
#for item in bio_list:
    #all_data.append(item)
for item in phy_list[4000:4500]:
    all_data.append(item)
for item in fin_list[3000:3500]:
    all_data.append(item)
for item in bio_data[2000:2500]:
    all_data.append(item)
with open('testing_corpus_generated/train_spread_even.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(['Abstract'])
    for item in all_data:
        writer.writerow([item])
print('All_DATA: '   +str(len(all_data)))
#all_data.append(cs_list[:300])
#all_data.append(bio_list)
#all_data.append(phy_list[:300])
#all_data.append(fin_list[:200])
#dframe = pd.DataFrame(data = {'Text':all_data})
#dframe.to_csv('generaldata.csv')
#print(dframe)
        