import pandas as pd
from io import StringIO  # got moved to io in python3.
import requests

data = pd.read_csv('https://docs.google.com/spreadsheets/d/1mEtPd_cNuc8YISlq_rxUc9cXlzZxo4_nkmmcq5CEli4/export?format=csv&id=1mEtPd_cNuc8YISlq_rxUc9cXlzZxo4_nkmmcq5CEli4')

#[Jason, Kevin, ...]
kerberos = data[data.columns[0]]
#[[6006,6009], [6008,6009]]
good = data[data.columns[1]]
#same as good
bad = data[data.columns[2]]


# ex: [[Jason, 6006, 6036], [Kevin,802,6009]]
nodeList = []
for i in range (0, len(data.columns)):
	nodeList.append(data.loc[i])




