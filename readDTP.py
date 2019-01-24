import pandas as pd
import requests
import csv
#Useful for converting google doc:
#export?format=csv&id=



#Grabs data from google sheets as a string
csv_content = requests.get('https://docs.google.com/spreadsheets/d/1wquNQ_ICc298ZLmLD6Of6MdIMa-zr5kQ2N1EyelSBJ4/export?format=csv&id=1wquNQ_ICc298ZLmLD6Of6MdIMa-zr5kQ2N1EyelSBJ4').text

#Converts string to csv file
f = open('csv_content.csv','w')
f.write(csv_content) 
f.close()




#Debugging code
# line_count = 0
# with open('csv_content.csv') as csv_reader:
# 	for row in csv_reader:
# 		if line_count == 0:
# 			print(f'Column names are {"".join(row)}')
# 			line_count += 1
# 		else:
# 			print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
# 			line_count += 1
# 	print(f'Processed {line_count} lines.')