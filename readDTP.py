import pandas as pd
from io import StringIO  # got moved to io in python3.
import requests

# Google Form: https://docs.google.com/forms/d/e/1FAIpQLScgo-RXVqytOKyXCMGfC36GE-tu9a6hGjEbm5MzTH_RRTkuxA/viewform?usp=pp_url
# Google Response: https://docs.google.com/spreadsheets/d/1wquNQ_ICc298ZLmLD6Of6MdIMa-zr5kQ2N1EyelSBJ4/edit#gid=590454524

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1mEtPd_cNuc8YISlq_rxUc9cXlzZxo4_nkmmcq5CEli4/export?format=csv&id=1mEtPd_cNuc8YISlq_rxUc9cXlzZxo4_nkmmcq5CEli4')

print(df)
