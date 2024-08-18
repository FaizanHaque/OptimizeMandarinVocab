# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:07:31 2018

@author: Faizan
"""
import random
import bisect
import matplotlib.pyplot as plt
import math
import time
import pandas as pd


#use https://zhtoolkit.com/apps/wordlist/create-list.cgi to get your own list of vocab
filename = 'optimizeZHWords.xlsx';

    
#%def view():
df1 = pd.read_excel(filename,'Sheet1')
df2 = pd.read_excel(filename,'Sheet2')
df3 = pd.read_excel(filename,'Sheet3')

#%    print("\n\n 1: list of all Airlines \n")
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    print(df1)
#%view()



#ha%list = ["h]

HSK1= set(df2['HSK1'].tolist())
HSK2= set(df2['HSK2'].tolist())
HSK3= set(df2['HSK3'].tolist())
HSK4= set(df2['HSK4'].tolist())
HSK5= set(df2['HSK5'].tolist())
HSK6= set(df2['HSK6'].tolist())

totalChars = df3['Characters'].tolist()
c100 = set(totalChars[1:100])
c250 = set(totalChars[1:250])
c500 = set(totalChars[1:500])
c1000 = set(totalChars[1:1000])
c2000 = set(totalChars[1:2000])
c2500 = set(totalChars[1:2500])
c3000 = set(totalChars[1:3000])
c5000 = set(totalChars[1:5000])
c10000 = set(totalChars[1:10000])



totalWords = df1['Total Words'].tolist()
tWf=1000
w100 = set(totalWords[1:100])
w250 = set(totalWords[1:250])
w500 = set(totalWords[1:500])
w1000 = set(totalWords[1:1000])
w5000 = set(totalWords[1:5000])
w10000 = set(totalWords[1:10000])
#top2000 = set(totalWords[1:5000])


totalWords= set(totalWords[1:tWf])



knownChars= df1['Known Characters'].tolist()
kCf=391
knownChars = set(knownChars[1:kCf])
knownWords = df1['Known Words'].tolist()
kWf=772
knownWords = set(knownWords[1:kWf])
filterWords =  {'一个','看到', '不过'}
knownWords = knownWords.union(filterWords)

lK = len(knownWords)
kw100 = len(w100.intersection(knownWords.union(knownChars)))
uw100 = w100.difference(knownWords.union(knownChars)) #combinations that I don't know

kw250 = len(w250.intersection(knownWords.union(knownChars)))
uw250 = w250.difference(knownWords.union(knownChars)) #combinations that I don't know

kw500 = len(w500.intersection(knownWords.union(knownChars)))
uw500 = w500.difference(knownWords.union(knownWords.union(knownChars))) #combinations that I don't know

kw1000 = len(w1000.intersection(knownWords.union(knownChars)))
uw1000 = w1000.difference(knownWords.union(knownChars)) #combinations that I don't know

kw5000 = len(w5000.intersection(knownWords.union(knownChars)))
uw5000 = w5000.difference(knownWords.union(knownChars)) #combinations that I don't know

kw10000 = len(w5000.intersection(knownWords.union(knownChars)))
uw10000 = w5000.difference(knownWords.union(knownChars)) #combinations that I don't know



lc100 = len(c100.intersection(knownWords.union(knownChars)))
kc100 = c100.intersection(knownWords.union(knownChars))
uc100 = c100.difference(knownWords.union(knownChars)) #combinations that I don't know

lc250 = len(c250.intersection(knownWords.union(knownChars)))
kc250 = c250.intersection(knownWords.union(knownChars))
uc250 = c250.difference(knownWords.union(knownChars)) #combinations that I don't know

lc500 = len(c500.intersection(knownWords.union(knownChars)))
kc500 = c500.intersection(knownWords.union(knownChars))
uc500 = c500.difference(knownWords.union(knownChars)) #combinations that I don't know

lc1000 = len(c1000.intersection(knownWords.union(knownChars)))
kc1000 = c1000.intersection(knownWords.union(knownChars))
uc1000 = c1000.difference(knownWords.union(knownChars)) #combinations that I don't know

lc2000 = len(c2000.intersection(knownWords.union(knownChars)))
kc2000 = c2000.intersection(knownWords.union(knownChars))
uc2000 = c2000.difference(knownWords.union(knownChars)) #combinations that I don't know

lc2500 = len(c2500.intersection(knownWords.union(knownChars)))
kc2500 = c2500.intersection(knownWords.union(knownChars))
uc2500 = c2500.difference(knownWords.union(knownChars)) #combinations that I don't know


lc3000 = len(c3000.intersection(knownWords.union(knownChars)))
kc3000 = c3000.intersection(knownWords.union(knownChars))
uc3000 = c3000.difference(knownWords.union(knownChars)) #combinations that I don't know


lc5000 = len(c5000.intersection(knownWords.union(knownChars)))
kc5000 = c5000.intersection(knownWords.union(knownChars))
uc5000 = c5000.difference(knownWords.union(knownChars)) #combinations that I don't know

lc10000 = len(c5000.intersection(knownWords.union(knownChars)))
kc10000 = c5000.intersection(knownWords.union(knownChars))
uc10000 = c5000.difference(knownWords.union(knownChars)) #combinations that I don't know



lHw1= len(HSK1.intersection(knownWords.union(knownChars)))
kHw1 = HSK1.intersection(knownWords.union(knownChars))
uHw1 = HSK1.difference(knownWords.union(knownChars)) #combinations that I don't know

lHw2 = len(HSK2.intersection(knownWords.union(knownChars)))
kHw2 = HSK2.intersection(knownWords.union(knownChars))
uHw2 = HSK2.difference(knownWords.union(knownChars)) #combinations that I don't know

lHw3 = len(HSK3.intersection(knownWords.union(knownChars)))
kHw3 = HSK3.intersection(knownWords.union(knownChars))
uHw3 = HSK3.difference(knownWords.union(knownChars)) #combinations that I don't know

lHw4 = len(HSK4.intersection(knownWords.union(knownChars)))
kHw4 = HSK4.intersection(knownWords.union(knownChars))
uHw4 = HSK4.difference(knownWords.union(knownChars)) #combinations that I don't know

lHw5 = len(HSK5.intersection(knownWords.union(knownChars)))
kHw5 = HSK5.intersection(knownWords.union(knownChars))
uHw5 = HSK5.difference(knownWords.union(knownChars)) #combinations that I don't know

lHw6 = len(HSK6.intersection(knownWords.union(knownChars)))
kHw6 = HSK6.intersection(knownWords.union(knownChars))
uHw6 = HSK6.difference(knownWords.union(knownChars)) #combinations that I don't know


#newChars= df1['New Characters'].tolist()
#nCf=1
#newChars = set(knownChars[1:nCf])

newChars=knownChars
knownComb = set()
#list3 = ['海','洋']
#s = ""
#temp0 = []

knownComb= set()
for i in knownChars:
    for j in newChars:
       # temp = set([i+j])
        knownComb.add(i+j)
#        if temp in list1:
#        temp2 = s.join(temp)
unknownComb = knownComb.difference(knownWords) #combinations that I don't know
newComb=  unknownComb.intersection(totalWords) # new combinations that are in the common words
print(newComb) 
len(newComb)
        
