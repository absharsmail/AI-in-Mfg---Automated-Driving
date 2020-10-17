 # balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

train_data = np.load('C:/Users/Ant Pc/GitHub/AI-in-Mfg---Automated-Driving/Aaftab/training_data.npy',allow_pickle=True)
trdt=pd.DataFrame(train_data)
print(trdt.head())
'''
print(trdt[0][100][80:475,50:910].reshape((395*860,1)).shape)
for i in range(len(trdt)):
    trdt[0][i]=trdt[0][i][80:475,50:910].reshape(395*860)

'''
i=0
i=[]

def rectify(c):
    choice=c
    o=0
    if choice==[1,1,0,0]:
        o=0

    elif choice==[1,0,1,0]:
        o=1

    elif choice==[1,0,0,1]:
        o=2

    elif choice==[0,1,1,0]:
        o=3

    elif choice==[0,1,0,1]:
        o=4
    elif choice==[0,0,1,1]:
        o=5
    elif choice==[1,0,0,0]:
        o=6
    elif choice==[0,1,0,0]:
        o=7
    elif choice==[0,0,1,0]:
        o=8
    elif choice==[0,0,0,1]:
        o=9

    else:
        o=o
    return o

choice=[]

for data in train_data:
    choicee=data[1]
    choice.append(rectify(choicee))

choice=pd.DataFrame(choice)

choice.to_csv('choice.csv')

pd.DataFrame(a).to_csv('poice.csv')