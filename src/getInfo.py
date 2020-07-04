import numpy as np
import pandas as pd
from os.path import expanduser

HOME = expanduser("~")
PATH = HOME + '/Github/mestrado-ppgee-chbmit'

files = pd.read_csv(
    PATH+'/docs/edf-with-seizures/files.txt', sep=" ", header=None).to_numpy()

# print(pd.read_csv(PATH+'/edf-with-seizures/'+files.iloc[0]))
x = pd.read_csv(PATH+'/docs/edf-with-seizures/' +
                  files[3, 0], header=None)
print(x.iloc[1,0])

for i in range(len(x)):
    if 'Channel ' in x.iloc[i,0]:
        print(x.iloc[i,0])

#d = {'freq':int(x.iloc[0,0][20:-3])}
#print(d)