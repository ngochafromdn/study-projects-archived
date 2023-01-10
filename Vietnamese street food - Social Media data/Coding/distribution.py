import json
import pandas as pd
import csv
def readFile(filename):
    #read_file_function
    fileResult = open(filename,'r')
    textResult = fileResult.read()
    dctResult = json.loads(textResult)
    return dctResult

def distribution(fileName):
    '''obtain distributions of a list of categories'''
    dct = readFile('liwc_dictionary_final.json')
    dctTranscript = readFile(fileName)
    distribute = {}
    for i in dctTranscript['vtt']:
        if "\n" in i['text']:
            i['text']=i['text'][i['text'].index('\n')+1:]        
    lst_text = []
    for i in dctTranscript['vtt']:
        lst_text.append(i['text'].split())
    transcript_list = [item for sublist in lst_text for item in sublist]
    temp = []
    for item in transcript_list:
        if '[' not in item:
            temp.append(item)
    for key in dct['dict'].keys():
        count = 0
        dctValues = dct['dict'][key]
        for word in temp:
            if word in dctValues:
                count += 1
        distribute[key] = (count/len(temp))

    return distribute


