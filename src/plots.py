import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


d = pd.read_csv(
    '/home/davi/Github/mestrado-ppgee-chbmit/data/all_energy_train.csv')


plt.ioff()
#sns.pairplot(hue='seizure',data=d.loc[:,['FP1-F7', 'F7-T7','seizure']])
'''for i in range(d.shape[1]-1):
    fig = plt.figure()
    sns.kdeplot(
        d.query("seizure=='s'").iloc[:, i], shade=True, Label='Com crise')
    sns.kdeplot(
        d.query("seizure=='n'").iloc[:, i], shade=True, Label='Sem crise')
    plt.title(d.columns[i])
'''

plt.plot(d.query("seizure=='n'").iloc[:, 0],'.')
plt.plot(d.query("seizure=='s'").iloc[:, 0],'.')
plt.show()
