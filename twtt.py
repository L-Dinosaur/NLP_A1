def twtt1(string):
    string = re.sub('<[\\w+="/ .]+>', '', string)
    return string

def twtt2(string):
    string = re.sub('&amp;', '&', string)
    string = re.sub('&quot', '"', string)
    string = re.sub('&gt;', '>', string)
    string = re.sub('&lt;', '<', string)
    return string

def twtt3(string):
    string = re.sub('((https?:\\/\\/)|(www.))[A-z./?=]+', '', string)
    return string

def twtt4(string):
    string = re.sub('[@|#]', '', string)
    return string

def twtt5(string):
    string = re.sub(' +', ' ', string)
    string = re.sub('\\. ', '.\n', string)
    #string = re.sub('\\! ', '!\n')
    return string



def twtt7(string):
    #string = re.sub('\\. ', ' .', string)
    string = re.sub(',', ' ,', string)
    string = re.sub('\\! ', ' !', string)
    string = re.sub('\\? ', ' ?', string)
    string = re.sub('; ', ' ;', string)
    string = re.sub('\'', ' \'', string)
    return string
'''
def twtt8(string):
    tokens = string.split()
    tagger = NLPlib.NLPlib()
    tags = tagger.tag(tokens)
    i = 0
    res = ""
    for token in tokens:
        res += token
        res += tags[i]
        i += 1
    return res
'''



def twtt9(string, mood):
    res = '<A=' + str(mood) + '>\n' + string
    return res

def twtt(string, mood):
    string = twtt9(twtt7(twtt5(twtt4(twtt3(twtt2(twtt1(string)))))), mood)
    return string

import re
import csv
import random
try:
    f = open("testdata.manual.2009.06.14.csv", 'rt')
    rd = csv.reader(f)
    i = 0
    strlis = []
    for row in rd:
        strlis.append(row[5])
        i += 1
        if(i >= 100):
            break
finally:
    f.close()

#str1 = twtt(str1, 0)
for i in range(100):
    strlis[i] = twtt(strlis[i],4*random.randrange(0,2,1))
    print(strlis[i])





