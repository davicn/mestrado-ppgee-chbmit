import numpy as np
import pandas as pd
from os.path import expanduser
from mne.io import concatenate_raws, read_raw_edf

HOME = expanduser("~")
CHBMIT = expanduser('/home/davi/physionet.org/files/chbmit/1.0.0/')
PATH = HOME + '/Github/mestrado-ppgee-chbmit/docs'

RECORDS_WITH_SEIZURES = pd.read_csv(PATH+'/RECORDS-WITH-SEIZURES', sep=" ")
RECORDS = pd.read_csv(PATH+'/RECORDS', sep=" ")

FILES = pd.read_json(PATH+'/seizures.json')



x = read_raw_edf(CHBMIT+FILES.iloc[0, 0], preload=True).to_data_frame().T



'''

inicio = FILES.loc[0, 'Seizures'][0]['Start']
fim = FILES.loc[0, 'Seizures'][0]['End']
'''
#print(x.iloc[:, inicio:fim].to_numpy())


print(RECORDS[RECORDS])

