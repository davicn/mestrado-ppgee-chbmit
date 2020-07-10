import numpy as np
import pandas as pd
from os.path import expanduser
from mne.io import concatenate_raws, read_raw_edf
from joblib import Parallel, delayed


def variance(x):
    return np.var(x, axis=1)


HOME = expanduser("~")
CHBMIT = expanduser('/home/davi/physionet.org/files/chbmit/1.0.0/')
PATH = HOME + '/Github/mestrado-ppgee-chbmit/docs'
RECORDS_WITH_SEIZURES = pd.read_csv(PATH+'/RECORDS-WITH-SEIZURES', sep=" ")
FS = 256

d = pd.read_json(
    '/home/davi/Github/mestrado-ppgee-chbmit/docs/seizures.json').iloc[:6]


# for i in range(len(d)):
# Carregando edf
# raw = read_raw_edf(CHBMIT+d.loc[i,'File Name'])
#
# df = raw.to_data_frame().T
# col = np.repeat('n',len(df.columns))
# col[start:end] = np.repeat('s',(end-start))
#
# df.columns = col
# raws.append(df.T)
#
#
#
raws = []

for i in range(len(d)):
    start = d.loc[i, 'Seizures'][0]['Start']
    end = d.loc[i, 'Seizures'][0]['End']

    raw = read_raw_edf(CHBMIT+d.loc[i, 'File Name'])
    df = raw.to_data_frame().drop(columns=['time', 'T8-P8-1']).T
    
    ft = Parallel(n_jobs=4)(delayed(variance)(
        df.iloc[:, i*FS:(i+1)*FS].to_numpy()) for i in range(df.shape[1]//FS))

    dd = pd.DataFrame(data=np.array(ft), columns=df.index)
    col = np.repeat('n', len(dd))
    
    col[start:end] = np.repeat('s', (end-start))

    dd['seizure'] = col
    raws.append(dd)
#
pd.concat(raws).to_csv('testando.csv',index=False)

# print(np.array(ft).shape)
# print(df.shape)
# print(np.var(df.iloc[:, :256].to_numpy(), axis=1).shape)
