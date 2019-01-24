import pandas as pd
import requests
import csv
#Useful for converting google doc:
#export?format=csv&id=




csv_content = requests.get('https://docs.google.com/spreadsheets/d/1mEtPd_cNuc8YISlq_rxUc9cXlzZxo4_nkmmcq5CEli4/export?format=csv&id=1mEtPd_cNuc8YISlq_rxUc9cXlzZxo4_nkmmcq5CEli4').text

print(csv_content)
print('**********')


# line_count = 0
# for row in csv_content:
#     if line_count == 0:
#         print(f'Column names are {", ".join(row)}')
#         line_count += 1
#     else:
#         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#         line_count += 1
# print(f'Processed {line_count} lines.')