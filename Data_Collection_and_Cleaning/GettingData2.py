import json
 
# Opening JSON file
f = open('the_savings.json')
 
# returns JSON object as a dictionary
data = json.load(f)

# counting the answers

print(len(data[1:]))

'''
# Iterating through the json list

for i in data[1:]: #la prima lista si salta che è vuota
    for diz in i: #iteriamo sui diz nella seconda lista
        print(diz['gender'])
'''

# Closing file
f.close()