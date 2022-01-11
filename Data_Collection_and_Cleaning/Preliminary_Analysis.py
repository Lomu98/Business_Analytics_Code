
import json
from pprint import pprint
from Mask import my_mask
from UnMasker import *
import csv
 
# Opening JSON file
f = open('/Users/lomu/Desktop/Business_Analytics_Analysis/the_savings.json')
 
# Returns JSON object as a dictionary
data = json.load(f)

# Creating a new dictionary and dropping out the initial empty list
new_data = data
new_data.pop(0)

# Applying the attributes unmasker
final_data = attribute_unmasker(new_data)
#print(final_data)

# Applying the levels unmasker
levels_unmasker(final_data)
#print(final_data)

# Transforming JSON in CSV
import pandas as pd

dati = final_data

with open("my_savings.json", "w") as outfile:
    json.dump(final_data, outfile)


df = pd.read_json(r'/Users/lomu/Desktop/Business_Analytics_Analysis/my_savings.json')


# df.to_csv(r'/Users/lomu/Desktop/savings.csv', index = None)

# Pre-requisite - Import the DictWriter class from csv  module
from csv import DictWriter

# Pre-requisite - The CSV file should be manually closed before running this code.

# As we want a new CSV file, we're going to open the file in the write mode 'w'
# Then, for the CSV file, create a file object
with open('NewCsvData.csv', 'w', newline='') as f_object:
    # The list of column names as mentioned in the CSV file
    headersCSV = ["Director", "Type", "Characters", "Genre", "Location", "Temporal collocation", "Saga", "Duration",
                  "First viewing", "id", "isChosen", "gender", "age", "resp.id"]
    # Pass the CSV  file object to the Dictwriter() function
    # Result - a DictWriter object
    dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
    # Write the headers
    dictwriter_object.writeheader()
    # Pass the data in the dictionary as an argument into the writerow() function
    i = 0


    # print(ques)

    for lista in final_data:
        i += 1
        for dict in lista:
            dict['resp.id'] = i
            '''
            dict['ques'] = 0
            for el in ques:
                if dict['ques'] == 0:
                    dict['ques'] = el
                else:
                    pass
            '''
            dictwriter_object.writerow(dict)

    # Close the file object
    f_object.close()

ques = []
tot_ques = 15*67
for n in range(1,tot_ques):
    ques.append(n)
    ques.append(n)
    ques.append(n)


with open('NewCsvData.csv', 'r') as r_object:
    with open('FinalCsvData.csv', 'w') as w_object:
        w = csv.writer(w_object, lineterminator='\n')
        r = csv.reader(r_object)

        all = []
        row = next(r)
        row.append('ques')
        all.append(row)
        i = 0
        for item in r:
            if i < len(ques):
                item.append(ques[i])
                i += 1
                all.append(item)
                print(item)

        w.writerows(all)

r_object.close()
w_object.close()


# Closing file
f.close()