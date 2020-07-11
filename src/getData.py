import numpy as np
import pandas as pd
from os.path import expanduser
from mne.io import concatenate_raws, read_raw_edf
from joblib import Parallel, delayed


def variance(x):
    return np.var(x, axis=1)


def energy(x):
    return np.array([
        np.sum(x[i]**2)
        for i in range(len(x))])


HOME = expanduser("~")
CHBMIT = expanduser('/home/davi/physionet.org/files/chbmit/1.0.0/')
PATH = HOME + '/Github/mestrado-ppgee-chbmit/docs'
RECORDS_WITH_SEIZURES = pd.read_csv(PATH+'/RECORDS-WITH-SEIZURES', sep=" ")
FS = 256

d = pd.read_json(
    '/home/davi/Github/mestrado-ppgee-chbmit/docs/seizures.json').iloc[53:]

d.index = np.arange(len(d))

print(d)

raws = []
labels = ['time', 'T8-P8-1', 'ECG', '--0', '--1', '--2', '--3', '--4']

for i in range(len(d)):

    start = [d.loc[i, 'Seizures'][ii]['Start']
             for ii in range(len(d.loc[i, 'Seizures']))]
    end = [d.loc[i, 'Seizures'][ii]['End']
           for ii in range(len(d.loc[i, 'Seizures']))]

    raw = read_raw_edf(CHBMIT+d.loc[i, 'File Name'])

    df = raw.to_data_frame()

    use_col = [i for i in df.columns if i not in labels]

    df = df.loc[:, use_col].T
    ft = Parallel(n_jobs=4)(delayed(energy)(
        df.iloc[:, i*FS:(i+1)*FS].to_numpy()) for i in range(df.shape[1]//FS))

    dd = pd.DataFrame(data=np.array(ft), columns=df.index)

    col = np.repeat('n', len(dd))

    for j in range(len(start)):
        col[start[j]:end[j]] = np.repeat('s', (end[j]-start[j]))

    dd['seizure'] = col

    raws.append(dd)

pd.concat(raws).to_csv('chb14_energy.csv', index=False)
