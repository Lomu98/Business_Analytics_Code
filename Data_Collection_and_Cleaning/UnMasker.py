
import json
from pprint import pprint
from Mask import my_mask

def attribute_unmasker(file: dict):
    '''
    :param file:
    :return: a new file with unmasked attribute
    '''
    final_data = []
    for respondent in file:
        final_resp = []
        for answer in respondent:
            # print(answer)
            new_answer = {}
            for att in my_mask['attributes'].values():
                new_answer[att] = 0
                new_answer['id'] = 0
                new_answer['isChosen'] = 0
                new_answer['gender'] = 0
                new_answer['age'] = 0
            for x in new_answer:
                if x == 'Director':
                    new_answer[x] = answer['0']
                elif x == 'Type':
                    new_answer[x] = answer['1']
                elif x == 'Characters':
                    new_answer[x] = answer['2']
                elif x == 'Genre':
                    new_answer[x] = answer['3']
                elif x == 'Location':
                    new_answer[x] = answer['4']
                elif x == 'Temporal collocation':
                    new_answer[x] = answer['5']
                elif x == 'Saga':
                    new_answer[x] = answer['6']
                elif x == 'Duration':
                    new_answer[x] = answer['7']
                elif x == 'First viewing':
                    new_answer[x] = answer['8']
                elif x == 'id':
                    new_answer['id'] = answer['id']
                elif x == 'isChosen':
                    new_answer['isChosen'] = answer['isChoiced']
                elif x == 'gender':
                    new_answer['gender'] = answer['gender']
                elif x == 'age':
                    new_answer['age'] = answer['age']

            desired_order_list = ['Director', 'Type', 'Characters', 'Genre', 'Location', 'Temporal collocation', 'Saga',
                                  'Duration', 'First viewing', 'id', 'isChosen', 'gender', 'age']
            reordered_answer = {k: new_answer[k] for k in desired_order_list}

            final_resp.append(reordered_answer)

        final_data.append(final_resp)

    return final_data


def levels_unmasker(file: dict):
    '''
    :param file: attribute unmasked file
    :return: just modify the file
    '''
    for respondent in file:
        for answer in respondent:
            for x in answer:
                if x == 'Director':
                    if answer['Director'] == 0:
                        answer['Director'] = 'Christopher Nolan'
                    elif answer['Director'] == 1:
                        answer['Director'] = 'Tim Burton'
                    else:
                        answer['Director'] = 'Steven Spielberg'
                elif x == 'Type': 
                    if answer[x] == 0: 
                      answer[x] = 'Animation film' 
                    else: 
                      answer[x] = 'Live-action'
                elif x == 'Characters':
                    if answer[x] == 0:
                        answer[x] = 'Humans' 
                    elif answer[x] == 1:
                        answer[x] = 'Animals' 
                    else: 
                        answer[x] = 'Robots/androids/humanoids'
                elif x == 'Genre': 
                    if answer[x] == 0: 
                      answer[x] = 'Science-fiction' 
                    elif answer[x] == 1: 
                      answer[x] = 'Thriller' 
                    else: 
                      answer[x] = 'Adventure'
                elif x == 'Location':
                    if answer[x] == 0: 
                        answer[x] = 'United States of America'
                    elif answer[x] == 1:
                        answer[x] = 'Europe'
                    elif answer[x] == 2:
                        answer[x] = 'Japan' 
                    else:
                        answer[x] = 'Mars'
                elif x == 'Temporal collocation': 
                    if answer[x] == 0: 
                      answer[x] = 'End of the 19th century' 
                    elif answer[x] == 1: 
                      answer[x] = '2022' 
                    else: 
                      answer[x] = '2100'
                elif x == 'Saga':
                    if answer[x] == 0:
                        answer[x] = 'Yes'
                    else:
                        answer[x] = 'No'
                elif x == 'Duration':
                    if answer[x] == 0:
                        answer[x] = '1h 40min'
                    elif answer[x] == 1:
                        answer[x] = '2h'
                    else:
                        answer[x] = '2h 20min'
                elif x == 'First viewing':
                    if answer[x] == 0:
                        answer[x] = 'Cinema'
                    else: 
                        answer[x] = 'Platforms'

