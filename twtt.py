def twtt1(string):
    '''
    This function removes the html tags
    :param string: pre-processed string
    :return string: html-tag-removed string
    '''

    string = re.sub('<[\\w+="/ .]+>', '', string)
    return string

def twtt2(string):
    '''
    This function changes the html characters to ascii ones
    :param string: pre-processed string
    :return string: html-character swapped string
    '''
    string = re.sub('&amp;', '&', string)
    string = re.sub('&quot', '"', string)
    string = re.sub('&gt;', '>', string)
    string = re.sub('&lt;', '<', string)
    return string

def twtt3(string):
    '''
    This function removes urls
    :param string: pre-processed string
    :return:
    '''
    string = re.sub('((https?:\\/\\/)|(www.))[A-z./?=]+', '', string)
    return string

def twtt4(string):
    '''
    This function removes hashtag character and at characters
    :param string:
    :return:
    '''
    string = re.sub('[@|#]', '', string)
    return string

def twtt5(string):
    '''
    This function puts distinct sentences on different lines
    :param string:
    :return:
    '''

    string = re.sub('\\. ', '.\n', string)
    string = re.sub('\\! ', '!\n', string)
    string = re.sub('\\? ', '?\n', string)
    return string



def twtt7(string):
    '''
    This function separates each token by space
    :param string:
    :return:
    '''
    string = re.sub('(\\. )|(\\.$)', ' . ', string)     # EOS periods
    string = re.sub('\\.\\.\\.+', ' ... ', string)     # Elipsis

    string = re.sub(',', ' ,', string)                  # commas

    string = re.sub('(\\! )|(\\!$)', ' ! ', string)     # EOS exclamation
    string = re.sub('\\!\\!\\!+', ' !!! ', string)       # Triple exclamation

    string = re.sub('(\\? )|(\\?$)', ' ? ', string)     # EOS question mark
    string = re.sub('\\?\\?\\?+', ' ??? ', string)       # Swaggy P ???

    string = re.sub('; ', ' ;', string)                 # semicolon

    string = re.sub('\'', ' \'', string)                # single quote

    string = re.sub(': ', ' : ', string)                # colon

    string = re.sub(' +', ' ', string)                  # merge extra spaces into one


    return string


def twtt8(string):
    tokens = string.split()
    tagger = nb.NLPlib()
    tags = tagger.tag(tokens)
    i = 0
    res = ""
    for token in tokens:
        res = res + token + "/"
        res = res + tags[i] + " "
        i += 1
    return res




def twtt9(string, mood):
    res = '<A=' + str(mood) + '>'
    if(len(string) == 0):
        return res
    if(res[-1] != "\n"):
        res += "\n" + string
    return res

def twtt(string, mood):

    string = twtt9(twtt5(twtt8(twtt7(twtt4(twtt3(twtt2(twtt1(string))))))), mood)
    return string

import re
import csv
import random
import NLPlib as nb
import sys
import time

time1 = time.time()
try:
    f = open(sys.argv[1], 'rt')
    rd = csv.reader(f)
    i = 0
    strlis = []
    x1 = (int(sys.argv[2]) % 80) * 10000
    x2 = x1 + 800000
    time2 = time.time()
    for row in rd:
        i += 1
        if(((i >= x1) and (i <= (x1 + 9999))) or ((i >= x2) and (i <= (x2 + 9999)))):
            strlis.append(row[5])

        if(i >= 1330000):
            break
    time3 = time.time()
finally:
    f.close()

d = open(sys.argv[3], 'w')
time4 = time.time()
for i in range(1000):
    strlis[i] = twtt(strlis[i],4*random.randrange(0,2,1))
    d.write(strlis[i])
time5 = time.time()
print('extracting tweets: ' + str(time3 - time2) + "s, on average: " + str(float(time3 - time2)/20000) + "s\n")
print('processing tweets: ' + str(time5 - time4) + "s, on average: " + str(float(time5 - time4)/1000) + "s\n")



