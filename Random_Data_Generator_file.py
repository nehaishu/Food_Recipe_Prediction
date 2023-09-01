#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_excel('food-3.xlsx')


# In[3]:


df= df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
df = df.applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x)


# In[5]:


col=['col-1', 'col-2', 'col-3', 'col-4', 'col-5', 'col-6', 'col-7', 'col-8',
       'col-9', 'col-10', 'col-11', 'col-12', 'col-13', 'col-14', 'col-15',
       'col-16', 'col-17', 'col-18', 'col-19','output']


# In[6]:


df=df[col]


# In[7]:


df


# In[8]:


whole_reciepe_ingredients_main_ingredients_list=[]
main_ingredients_list=[]


# In[9]:


PhoolMakhaneKiKheer_list=df.iloc[169,:20].values.tolist()
PhoolMakhaneKiKheer_main_list=['milk','ghee']
main_ingredients_list.append(PhoolMakhaneKiKheer_main_list)
whole_reciepe_ingredients_main_ingredients_list.append(PhoolMakhaneKiKheer_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list


# In[10]:


EggCurry_list=df.iloc[170,:20].values.tolist()
EggCurry_main_list=['eggs','chilllipowder','onions','gingergarlicpaste']
main_ingredients_list.append(EggCurry_main_list)
main_ingredients_list
whole_reciepe_ingredients_main_ingredients_list.append(EggCurry_list)
whole_reciepe_ingredients_main_ingredients_list


# In[11]:


main_ingredients_list


# In[12]:


upma_list=df.iloc[172,:20].values.tolist()
upma_list_main_list=['semolina','onion','chillies', 'carrot']
whole_reciepe_ingredients_main_ingredients_list.append(upma_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(upma_list_main_list)
main_ingredients_list


# In[13]:


brownricepayasam_list=df.iloc[173,:20].values.tolist()
brownricepayasam_main_list=['brownrice','jaggery','milk','cashews']
whole_reciepe_ingredients_main_ingredients_list.append(brownricepayasam_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(brownricepayasam_main_list)
main_ingredients_list


# In[14]:


OnionDosa_list=df.iloc[174,:20].values.tolist()
OnionDosa_main_list=['uraddal','onions']
whole_reciepe_ingredients_main_ingredients_list.append(OnionDosa_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(OnionDosa_main_list)
main_ingredients_list


# In[15]:


BrinjalFry_list=df.iloc[175,:20].values.tolist()
BrinjalFry_main_list=['brinjal','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(BrinjalFry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(BrinjalFry_main_list)
main_ingredients_list


# In[16]:


BrinjalCurry_list=df.iloc[176,:20].values.tolist()
BrinjalCurry_main_list=['brinjal','onions','chillipowder']
whole_reciepe_ingredients_main_ingredients_list.append(BrinjalCurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(BrinjalCurry_main_list)
main_ingredients_list


# In[17]:


Potatofry_list=df.iloc[177,:20].values.tolist()
Potatofry_main_list=['potatoes','chillies','onions']
whole_reciepe_ingredients_main_ingredients_list.append(Potatofry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Potatofry_main_list)
main_ingredients_list


# In[18]:


chickenfry_list=df.iloc[178,:20].values.tolist()
chickenfry_main_list=['chicken','onions','chillies','gingergarlicpaste']
whole_reciepe_ingredients_main_ingredients_list.append(chickenfry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(chickenfry_main_list)
main_ingredients_list


# In[19]:


ladiesfringercurry_list=df.iloc[179,:20].values.tolist()
ladiesfringercurry_main_list=['ladiesfingers','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(ladiesfringercurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(ladiesfringercurry_main_list)
main_ingredients_list


# In[20]:


onionpakodi_list=df.iloc[180,:20].values.tolist()
onionpakodi_main_list=['gramflour','riceflour','onions']
whole_reciepe_ingredients_main_ingredients_list.append(onionpakodi_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(onionpakodi_main_list)
main_ingredients_list


# In[21]:


sambhar_list=df.iloc[181,:20].values.tolist()
sambhar_main_list=['toordal','tamarindjuice','curryleaves','tomato']
whole_reciepe_ingredients_main_ingredients_list.append(sambhar_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(sambhar_main_list)
main_ingredients_list


# In[22]:


Mangodal_list=df.iloc[182,:20].values.tolist()
Mangodal_main_list=['toordal','rawmangoes','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(Mangodal_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Mangodal_main_list)
main_ingredients_list


# In[23]:


Cucumbercurry_list=df.iloc[183,:20].values.tolist()
Cucumbercurry_main_list=['cucumber','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(Cucumbercurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Cucumbercurry_main_list)
main_ingredients_list


# In[24]:


Haleem_list=df.iloc[184,:20].values.tolist()
Haleem_main_list=['chicken','ghee','chillies','gingergarlicpaste']
whole_reciepe_ingredients_main_ingredients_list.append(Haleem_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Haleem_main_list)
main_ingredients_list


# In[25]:


ivygourdcurry_list=df.iloc[185,:20].values.tolist()
ivygourdcurry_main_list=['ivygourd','onions','chillies','tomato']
whole_reciepe_ingredients_main_ingredients_list.append(ivygourdcurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(ivygourdcurry_main_list)
main_ingredients_list


# In[26]:


BitterGourdcurry_list=df.iloc[186,:20].values.tolist()
BitterGourdcurry_main_list=['bittergourd','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(BitterGourdcurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(BitterGourdcurry_main_list)
main_ingredients_list


# In[27]:


BitterGuardfry_list=df.iloc[187,:20].values.tolist()
BitterGuardfry_main_list=['bittergourd','onions','chillies','corianderpowder']
whole_reciepe_ingredients_main_ingredients_list.append(BitterGuardfry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(BitterGuardfry_main_list)
main_ingredients_list


# In[28]:


TamarindPulihora_list=df.iloc[188,:20].values.tolist()
TamarindPulihora_main_list=['tamarindjuice','rice','peanuts','chillies','curryleaves']
whole_reciepe_ingredients_main_ingredients_list.append(TamarindPulihora_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(TamarindPulihora_main_list)
main_ingredients_list


# In[29]:


Mangopulihora_list=df.iloc[189,:20].values.tolist()
Mangopulihora_main_list=['rawmangoes','rice','peanuts','dryredchillies']
whole_reciepe_ingredients_main_ingredients_list.append(Mangopulihora_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Mangopulihora_main_list)
main_ingredients_list


# In[30]:


Curdrice_list=df.iloc[190,:20].values.tolist()
Curdrice_main_list=['rice','curd','blackmustardseeds']
whole_reciepe_ingredients_main_ingredients_list.append(Curdrice_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Curdrice_main_list)
main_ingredients_list


# In[31]:


prawnsfry_list=df.iloc[191,:20].values.tolist()
prawnsfry_main_list=['prawns','gingergarlicpaste','chillipowder','garammasala',]
whole_reciepe_ingredients_main_ingredients_list.append(prawnsfry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(prawnsfry_main_list)
main_ingredients_list


# In[32]:


Bobbatlu_list=df.iloc[192,:20].values.tolist()
Bobbatlu_main_list=['wheatflour','jaggery','bengalgramdal']
whole_reciepe_ingredients_main_ingredients_list.append(Bobbatlu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Bobbatlu_main_list)
main_ingredients_list


# In[33]:


EggDosa_list=df.iloc[193,:20].values.tolist()
EggDosa_main_list=['egg','uraddal','rice','chillipowder']
whole_reciepe_ingredients_main_ingredients_list.append(EggDosa_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(EggDosa_main_list)
main_ingredients_list


# In[34]:


Boorelu_list=df.iloc[194,:20].values.tolist()
Boorelu_main_list=['uraddal','bengalgramdal','jaggery']
whole_reciepe_ingredients_main_ingredients_list.append(Boorelu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Boorelu_main_list)
main_ingredients_list


# In[35]:


Meduvada_list=df.iloc[195,:20].values.tolist()
Meduvada_main_list=['uraddal','onions','corianderleaves']
whole_reciepe_ingredients_main_ingredients_list.append(Meduvada_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Meduvada_main_list)
main_ingredients_list


# In[36]:


pesarattu_list=df.iloc[196,:20].values.tolist()
pesarattu_main_list=['greengram','ginger','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(pesarattu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(pesarattu_main_list)
main_ingredients_list


# In[37]:


kheer_list=df.iloc[197,:20].values.tolist()
kheer_main_list=['rice','milk','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(kheer_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(kheer_main_list)
main_ingredients_list


# In[38]:


palathalikalu_list=df.iloc[198,:20].values.tolist()
palathalikalu_main_list=['milk','riceflour','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(palathalikalu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(palathalikalu_main_list)
main_ingredients_list


# In[39]:


jaggeryundrallu_list=df.iloc[199,:20].values.tolist()
jaggeryundrallu_main_list=['riceflour','jaggery']
whole_reciepe_ingredients_main_ingredients_list.append(jaggeryundrallu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(jaggeryundrallu_main_list)
main_ingredients_list


# In[40]:


kudumulu_list=df.iloc[200,:20].values.tolist()
kudumulu_main_list=['riceflour']
whole_reciepe_ingredients_main_ingredients_list.append(kudumulu_list)


# In[41]:



whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(kudumulu_main_list)
main_ingredients_list


# In[42]:


Tapalachekka_list=df.iloc[201,:20].values.tolist()
Tapalachekka_main_list=['riceflour','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(Tapalachekka_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Tapalachekka_main_list)
main_ingredients_list


# In[43]:


Mysorebonda_list=df.iloc[202,:20].values.tolist()
Mysorebonda_main_list=['allpurposeflour','riceflour','curd']
whole_reciepe_ingredients_main_ingredients_list.append(Mysorebonda_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Mysorebonda_main_list)
main_ingredients_list


# In[44]:


poori_list=df.iloc[203,:20].values.tolist()
poori_main_list=['wheatflour','gramflour']
whole_reciepe_ingredients_main_ingredients_list.append(poori_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(poori_main_list)
main_ingredients_list


# In[45]:


Masalapoori_list=df.iloc[204,:20].values.tolist()
Masalapoori_main_list=['wheatflour','gramflour','corianderpowder']
whole_reciepe_ingredients_main_ingredients_list.append(Masalapoori_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Masalapoori_main_list)
main_ingredients_list


# In[46]:


chapathi_list=df.iloc[205,:20].values.tolist()
chapathi_main_list=['wheatflour']
whole_reciepe_ingredients_main_ingredients_list.append(chapathi_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(chapathi_main_list)
main_ingredients_list


# In[47]:


Roti_list=df.iloc[206,:20].values.tolist()
Roti_main_list=['wheatflour']
whole_reciepe_ingredients_main_ingredients_list.append(Roti_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Roti_main_list)
main_ingredients_list


# In[48]:


Putharekulu_list=df.iloc[207,:20].values.tolist()
Putharekulu_main_list=['rice','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(Putharekulu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Putharekulu_main_list)
main_ingredients_list


# In[49]:


doublekameetha_list=df.iloc[208,:20].values.tolist()
doublekameetha_main_list=['bread','sugar','milk']
whole_reciepe_ingredients_main_ingredients_list.append(doublekameetha_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(doublekameetha_main_list)
main_ingredients_list


# In[50]:


sunnunda_list=df.iloc[209,:20].values.tolist()
sunnunda_main_list=['uraddal','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(sunnunda_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(sunnunda_main_list)
main_ingredients_list


# In[51]:


Laddu_list=df.iloc[210,:20].values.tolist()
Laddu_main_list=['gramflour','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(Laddu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Laddu_main_list)
main_ingredients_list


# In[52]:


Ariselu_list=df.iloc[211,:20].values.tolist()
Ariselu_main_list=['riceflour','jaggery']
whole_reciepe_ingredients_main_ingredients_list.append(Ariselu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Ariselu_main_list)
main_ingredients_list


# In[53]:


Semiyapayasam_list=df.iloc[212,:20].values.tolist()
Semiyapayasam_main_list=['vermicelli','sugar','milk']
whole_reciepe_ingredients_main_ingredients_list.append(Semiyapayasam_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Semiyapayasam_main_list)
main_ingredients_list


# In[54]:


ravaladdu_list=df.iloc[213,:20].values.tolist()
ravaladdu_main_list=['semolina','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(ravaladdu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(ravaladdu_main_list)
main_ingredients_list


# In[55]:


kajjikayalu_list=df.iloc[214,:20].values.tolist()
kajjikayalu_main_list=['allpurposeflour','sugar','semolina']
whole_reciepe_ingredients_main_ingredients_list.append(kajjikayalu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(kajjikayalu_main_list)
main_ingredients_list


# In[56]:


Gavvalu_list=df.iloc[215,:20].values.tolist()
Gavvalu_main_list=['allpurposeflour','jaggery']
whole_reciepe_ingredients_main_ingredients_list.append(Gavvalu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Gavvalu_main_list)
main_ingredients_list


# In[57]:


PachiPulusu_list=df.iloc[216,:20].values.tolist()
PachiPulusu_main_list=['tamarindjuice','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(PachiPulusu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(PachiPulusu_main_list)
main_ingredients_list


# In[58]:


Sakinalu_list=df.iloc[217,:20].values.tolist()
Sakinalu_main_list=['riceflour']
whole_reciepe_ingredients_main_ingredients_list.append(Sakinalu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Sakinalu_main_list)
main_ingredients_list


# In[59]:


punugulu_list=df.iloc[218,:20].values.tolist()
punugulu_main_list=['uraddal','rice']
whole_reciepe_ingredients_main_ingredients_list.append(punugulu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(punugulu_main_list)
main_ingredients_list


# In[60]:


chintachigurupachadi_list=df.iloc[219,:20].values.tolist()
chintachigurupachadi_main_list=['tamarindleaves','dryredchillies','dryredchillies']
whole_reciepe_ingredients_main_ingredients_list.append(chintachigurupachadi_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(chintachigurupachadi_main_list)
main_ingredients_list


# In[61]:


sheerkhurma_list=df.iloc[220,:20].values.tolist()
sheerkhurma_main_list=['milk','vermicelli','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(sheerkhurma_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(sheerkhurma_main_list)
main_ingredients_list


# In[62]:


channamasalacurry_list=df.iloc[221,:20].values.tolist()
channamasalacurry_main_list=['chickpeas','chillipowder', 'chillies','gingergarlicpaste']
whole_reciepe_ingredients_main_ingredients_list.append(channamasalacurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(channamasalacurry_main_list)
main_ingredients_list


# In[63]:


onionsamosa_list=df.iloc[222,:20].values.tolist()
onionsamosa_main_list=['allpurposeflour','onions']
whole_reciepe_ingredients_main_ingredients_list.append(onionsamosa_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(onionsamosa_main_list)
main_ingredients_list


# In[64]:


whole_reciepe_ingredients_main_ingredients_list


# In[65]:


Aloosamosa_list=df.iloc[223,:20].values.tolist()
Aloosamosa_main_list=['allpurposeflour','potatoes','onions']
whole_reciepe_ingredients_main_ingredients_list.append(Aloosamosa_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Aloosamosa_main_list)
main_ingredients_list


# In[66]:


whole_reciepe_ingredients_main_ingredients_list


# In[67]:


AlooGobi_list=df.iloc[224,:20].values.tolist()
AlooGobi_main_list=['potatoes','cauliflower','chillipowder']
whole_reciepe_ingredients_main_ingredients_list.append(AlooGobi_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(AlooGobi_main_list)
main_ingredients_list


# In[68]:


whole_reciepe_ingredients_main_ingredients_list


# In[69]:


Boticurry_list=df.iloc[225,:20].values.tolist()
Boticurry_main_list=['goatintestine','onions','chillipowder','garammasala']
whole_reciepe_ingredients_main_ingredients_list.append(Boticurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Boticurry_main_list)
main_ingredients_list


# In[70]:


RajmaMasala_list=df.iloc[226,:20].values.tolist()
RajmaMasala_main_list=['kidneybeans','chillies','onions']
whole_reciepe_ingredients_main_ingredients_list.append(RajmaMasala_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(RajmaMasala_main_list)
main_ingredients_list


# In[71]:


LiverMasala_list=df.iloc[227,:20].values.tolist()
LiverMasala_main_list=['liver','onions','chillipowder','garammasala']
whole_reciepe_ingredients_main_ingredients_list.append(LiverMasala_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(LiverMasala_main_list)
main_ingredients_list


# In[72]:


Murukulu_list=df.iloc[228,:20].values.tolist()
Murukulu_main_list=['riceflour','chillipowder']
whole_reciepe_ingredients_main_ingredients_list.append(Murukulu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Murukulu_main_list)
main_ingredients_list


# In[73]:


BhejaFry_list=df.iloc[229,:20].values.tolist()
BhejaFry_main_list=['goatbrain','chillipowder','onions']
whole_reciepe_ingredients_main_ingredients_list.append(BhejaFry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(BhejaFry_main_list)
main_ingredients_list


# In[74]:


Mushroomfry_list=df.iloc[230,:20].values.tolist()
Mushroomfry_main_list=['mushrooms','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(Mushroomfry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Mushroomfry_main_list)
main_ingredients_list


# In[75]:


Coconutchutney_list=df.iloc[231,:20].values.tolist()
Coconutchutney_main_list=['coconutpieces','dryredchillies','curryleaves']
whole_reciepe_ingredients_main_ingredients_list.append(Coconutchutney_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Coconutchutney_main_list)
main_ingredients_list


# In[76]:


Tomatochutney_list=df.iloc[232,:20].values.tolist()
Tomatochutney_main_list=['tomatoes','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(Tomatochutney_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Tomatochutney_main_list)
main_ingredients_list


# In[77]:


Masalavada_list=df.iloc[234,:20].values.tolist()
Masalavada_main_list=['bengalgramdal','gingergarlicpaste']
whole_reciepe_ingredients_main_ingredients_list.append(Masalavada_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Masalavada_main_list)
main_ingredients_list


# In[78]:


whole_reciepe_ingredients_main_ingredients_list


# In[79]:


Bottleguardhalwa_list=df.iloc[235,:20].values.tolist()
Bottleguardhalwa_main_list=['bottlegourd', 'milk','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(Bottleguardhalwa_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Bottleguardhalwa_main_list)
main_ingredients_list


# In[80]:


Tomatorice_list=df.iloc[236,:20].values.tolist()
Tomatorice_main_list=['tomatoes','rice','chillipowder']
whole_reciepe_ingredients_main_ingredients_list.append(Tomatorice_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Tomatorice_main_list)
main_ingredients_list


# In[81]:


MirchiBajji_list=df.iloc[237,:20].values.tolist()
MirchiBajji_main_list=['gramflour','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(MirchiBajji_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(MirchiBajji_main_list)
main_ingredients_list


# In[82]:


AlooBajji_list=df.iloc[238,:20].values.tolist()
AlooBajji_main_list=['potatoes','gramflour',]
whole_reciepe_ingredients_main_ingredients_list.append(AlooBajji_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(AlooBajji_main_list)
main_ingredients_list


# In[83]:


GonguraMuttoncurry_list=df.iloc[239,:20].values.tolist()
GonguraMuttoncurry_main_list=['mutton','sorrelleaves','chillipowder','gingergarlicpaste']
whole_reciepe_ingredients_main_ingredients_list.append(GonguraMuttoncurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(GonguraMuttoncurry_main_list)
main_ingredients_list


# In[84]:


Gongurachutney_list=df.iloc[240,:20].values.tolist()
Gongurachutney_main_list=['sorrelleaves','dryredchillies']
whole_reciepe_ingredients_main_ingredients_list.append(Gongurachutney_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Gongurachutney_main_list)
main_ingredients_list


# In[85]:


Mintleaves_list=df.iloc[241,:20].values.tolist()
Mintleaves_main_list=['mintleaves','dryredchillies']
whole_reciepe_ingredients_main_ingredients_list.append(Mintleaves_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Mintleaves_main_list)
main_ingredients_list


# In[86]:


BagaraRice_list=df.iloc[242,:20].values.tolist()
BagaraRice_main_list=['rice','mintleaves','tomatoes','onions']
whole_reciepe_ingredients_main_ingredients_list.append(BagaraRice_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(BagaraRice_main_list)
main_ingredients_list


# In[87]:


BrinjalPotatocurry_list=df.iloc[243,:20].values.tolist()
BrinjalPotatocurry_main_list=['brinjal','potatoes','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(BrinjalPotatocurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(BrinjalPotatocurry_main_list)
main_ingredients_list


# In[88]:


PalakDal_list=df.iloc[244,:20].values.tolist()
PalakDal_main_list=['toordal','tomatoes','spinachleaves']
whole_reciepe_ingredients_main_ingredients_list.append(PalakDal_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(PalakDal_main_list)
main_ingredients_list


# In[89]:


DrumstickTomatocurry_list=df.iloc[245,:20].values.tolist()
DrumstickTomatocurry_main_list=['drumsticks','onions','tomatoes','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(DrumstickTomatocurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(DrumstickTomatocurry_main_list)
main_ingredients_list


# In[90]:


Gobimanchurian_list=df.iloc[246,:20].values.tolist()
Gobimanchurian_main_list=['cauliflower','allpurposeflour','chillipowder']
whole_reciepe_ingredients_main_ingredients_list.append(Gobimanchurian_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Gobimanchurian_main_list)
main_ingredients_list


# In[91]:


osmaniaBiscuit_list=df.iloc[247,:20].values.tolist()
osmaniaBiscuit_main_list=['allpurposeflour','sugar','milk']
whole_reciepe_ingredients_main_ingredients_list.append(osmaniaBiscuit_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(osmaniaBiscuit_main_list)
main_ingredients_list


# In[92]:


CarrotHalwa_list=df.iloc[248,:20].values.tolist()
CarrotHalwa_main_list=['carrots','milk','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(CarrotHalwa_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(CarrotHalwa_main_list)
main_ingredients_list


# In[93]:


GingerChutney_list=df.iloc[249,:20].values.tolist()
GingerChutney_main_list=['ginger','dryredchillies','tamarindjuice','jaggery']
whole_reciepe_ingredients_main_ingredients_list.append(GingerChutney_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(GingerChutney_main_list)
main_ingredients_list


# In[94]:


Ugadipachadi_list=df.iloc[250,:20].values.tolist()
Ugadipachadi_main_list=['mangoes','banana','neemflower']
whole_reciepe_ingredients_main_ingredients_list.append(Ugadipachadi_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Ugadipachadi_main_list)
main_ingredients_list


# In[95]:


Lemonrice_list=df.iloc[251,:20].values.tolist()
Lemonrice_main_list=['lemons','rice','turmericpowder']
whole_reciepe_ingredients_main_ingredients_list.append(Lemonrice_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Lemonrice_main_list)
main_ingredients_list


# In[96]:


Garlicchillipowder_list=df.iloc[252,:20].values.tolist()
Garlicchillipowder_main_list=['garlic','dryredchillies']
whole_reciepe_ingredients_main_ingredients_list.append(Garlicchillipowder_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Garlicchillipowder_main_list)
main_ingredients_list


# In[97]:


moongdalvada_list=df.iloc[253,:20].values.tolist()
moongdalvada_main_list=['moongdal','chillies','ginger']
whole_reciepe_ingredients_main_ingredients_list.append(moongdalvada_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(moongdalvada_main_list)
main_ingredients_list


# In[98]:


Tomatorasam_list=df.iloc[254,:20].values.tolist()
Tomatorasam_main_list=['tomatoes','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(Tomatorasam_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(Tomatorasam_main_list)
main_ingredients_list


# In[99]:


tomatodal_list=df.iloc[263,:20].values.tolist()
tomatodal_main_list=['toordal','tomatoes','tamarindjuice']
whole_reciepe_ingredients_main_ingredients_list.append(tomatodal_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(tomatodal_main_list)
main_ingredients_list


# In[100]:


garlicchutney_list=df.iloc[264,:20].values.tolist()
garlicchutney_main_list=['dryredchillies','garlic','jaggery']
whole_reciepe_ingredients_main_ingredients_list.append(garlicchutney_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(garlicchutney_main_list)
main_ingredients_list


# In[101]:


muddapappu_list=df.iloc[265,:20].values.tolist()
muddapappu_main_list=['toordal','ghee']
whole_reciepe_ingredients_main_ingredients_list.append(muddapappu_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(muddapappu_main_list)
main_ingredients_list


# In[102]:


ravakesari_list=df.iloc[266,:20].values.tolist()
ravakesari_main_list=['semolina','sugar']
whole_reciepe_ingredients_main_ingredients_list.append(ravakesari_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(ravakesari_main_list)
main_ingredients_list


# In[103]:


kheemasamosa_list=df.iloc[267,:20].values.tolist()
kheemasamosa_main_list=['allpurposeflour','onions','meat','gingergarlicpaste']
whole_reciepe_ingredients_main_ingredients_list.append(kheemasamosa_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(kheemasamosa_main_list)
main_ingredients_list


# In[104]:


makkaroti_list=df.iloc[268,:20].values.tolist()
makkaroti_main_list=['maizeflour']
whole_reciepe_ingredients_main_ingredients_list.append(makkaroti_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(makkaroti_main_list)
main_ingredients_list


# In[105]:


eggfry_list=df.iloc[269,:20].values.tolist()
eggfry_main_list=['eggs','onions','chillipowder','gingergarlicpaste']
whole_reciepe_ingredients_main_ingredients_list.append(eggfry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(eggfry_main_list)
main_ingredients_list


# In[106]:


channamasalacurry_list=df.iloc[270,:20].values.tolist()
channamasalacurry_main_list=['chickpeas','chillipowder','onions']
whole_reciepe_ingredients_main_ingredients_list.append(channamasalacurry_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(channamasalacurry_main_list)
main_ingredients_list


# In[107]:


capsicummasalarice_list=df.iloc[271,:20].values.tolist()
capsicummasalarice_main_list=['capsicum','onions','chillies']
whole_reciepe_ingredients_main_ingredients_list.append(capsicummasalarice_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(capsicummasalarice_main_list)
main_ingredients_list


# In[108]:


methichicken_list=df.iloc[272,:20].values.tolist()
methichicken_main_list=['chicken','chillies','fenugreekleaves']
whole_reciepe_ingredients_main_ingredients_list.append(methichicken_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(methichicken_main_list)
main_ingredients_list


# In[109]:


gobi65_list=df.iloc[274,:20].values.tolist()
gobi65_main_list=['cauliflower','chillies','onions']
whole_reciepe_ingredients_main_ingredients_list.append(gobi65_list)
whole_reciepe_ingredients_main_ingredients_list
main_ingredients_list.append(gobi65_main_list)
main_ingredients_list


# In[111]:


cols=['col-1', 'col-2', 'col-3', 'col-4', 'col-5', 'col-6', 'col-7', 'col-8',
       'col-9', 'col-10', 'col-11', 'col-12', 'col-13', 'col-14', 'col-15',
       'col-16', 'col-17', 'col-18', 'col-19']


# In[112]:


# Generates Random Rows for each Reciepe
import numpy as np
import random 
def generate_random_rows(ingredients_list,main_ingredients_list,df, cols):
    output=ingredients_list[-1]
    random_list = [item for item in ingredients_list if item not in main_ingredients_list]
    n = random.randint(5, len(ingredients_list)-1)
    n=n-len(main_ingredients_list)
    if n <= len(random_list):
        random_ingredients = random.sample(random_list, n)
        random_ingredients=main_ingredients_list + random_ingredients


    
    # Fill the remaining columns with NaN
    missing_cols = len(col) - len(random_ingredients)
    random_ingredients.extend([np.nan] * missing_cols)
    
    new_row = pd.DataFrame([random_ingredients], columns=cols)
    new_row['output'] = output
    
    return new_row


# In[120]:


# call the Random row generator function and After Generating the Rows it appends 10 different Rows to main Dataframe and returns it
def generate_ten_rows(whole_reciepe_ingredients_complete_list,whole_reciepe_ingredients_main_ingredients_list,df,cols):
    for i in range(len(whole_reciepe_ingredients_complete_list)):
        ingredients_list=whole_reciepe_ingredients_complete_list[i]
        main_ingredients_list=whole_reciepe_ingredients_main_ingredients_list[i]
        for j in range(0,10):
            df_new=generate_random_rows(ingredients_list,main_ingredients_list,df,col)
            df = df.append(df_new, ignore_index=True)
    return df


# In[ ]:





# Work Tobe done :
# 
# Create the below two lists for all unique Reciepes

# In[ ]:


# both list should have same no of lists reciepe order should be same in both lists
whole_reciepe_ingredients_complete_list=[chknbiryni_list,---,etc..,]
whole_reciepe_ingredients_main_ingredients_list=[chknbiryni_main_ingredients_list,-----,etc..,]


# In[121]:


final_data=generate_ten_rows(whole_reciepe_ingredients_main_ingredients_list,main_ingredients_list,df,cols)


# In[122]:


final_data


# In[123]:


final_data.to_excel('final_data.xlsx')


# In[ ]:





# In[ ]:





# In[ ]:




