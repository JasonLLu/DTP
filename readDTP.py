import pandas as pd
from io import StringIO  # got moved to io in python3.
import requests

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1mEtPd_cNuc8YISlq_rxUc9cXlzZxo4_nkmmcq5CEli4/export?format=csv&id=1mEtPd_cNuc8YISlq_rxUc9cXlzZxo4_nkmmcq5CEli4')
#check for git
#testing
print('hello')
print(df)