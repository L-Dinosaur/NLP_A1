def feat1(string):
    '''
    This function counts how many first person pronouns there are in the tweet
    :param string:
    :return:
    '''
    string = re.sub("/[A-Z]+", "", string).split()
    res = 0
    for substr in string:
        if(re.match("(^me$)|(^I$)|(^my$)|(^My$)|(^We$)|(^Our$)|(^mine$)|(^we$)|(^us$)|(^our$)|(^ours$)", substr) != None):
            res += 1
    return res



def feat2(string):
    '''
    This function counts how many second person pronouns there are in the tweet
    :param string:
    :return:
    '''

    string = re.sub("/[A-Z]+", "", string).split()
    res = 0
    for substr in string:
        if(re.match("(^you$)|(^You$)|(^your$)|(^Your$)|(^yours$)|(^u$)|(^U$)|(^ur$)|(^Ur$)|(^urs$)", substr) != None):
            res += 1
    return res


def feat3(string):
    '''
    This function counts the number of third person pronouns there are in the tweet
    :param string:
    :return:
    '''

    string = re.sub("/[A-Z]+", "", string).split()
    res = 0
    for substr in string:
        if (re.match("(^he$)|(^He$)|(^him$)|(^his$)|(^His$)|(^she$)|(^She$)|(^her$)|(^Her$)|(^hers$)|(^it$)", substr) != None):
            res += 1
        elif(re.match("(^It$)|(^its$)|(^they$)|(^They$)|(^them$)|(^their$)|(^Their$)|(^theirs$)", substr) != None):
            res += 1
    return res


def feat4(string):
    '''
    This function finds out how many coordination conjunction there are in the tweet
    :param string:
    :return:
    '''

    return string.count("CC")

def feat5(string):
    '''
    This function finds out how many past tense verbs there are in the tweet
    :param string:
    :return:
    '''

    return string.count("VBD")

def feat6(string):
    '''
    This function finds out how many future tense verbs there are in the tweet
    :param string:
    :return:
    '''
    res = 0

    agt_list = re.findall("are/VBP going/VBG to/TO [A-z]+/VB")
    res += len(agt_list)
    string = re.sub("/[A-Z]+", "", string).split()

    for substr in string:
        if(re.match("(^'ll$)|(^will$)|(^Will$)|(^gonna$)", substr) != None):
            res += 1
    return res

def feat7(string):
    '''
    This function counts how many commas there are
    :param string:
    :return:
    '''
    return string.count("/,")

def feat8(string):
    '''
    This function counts the number of colons
    :param string:
    :return:
    '''
    return string.count(":") - string.count("/:") + string.count(";")


def feat9(string):
    '''
    This function counts the number of dashes
    :param string:
    :return:
    '''
    return string.count("-")

def feat10(string):
    '''
    This function returns the number of parentheses
    :param string:
    :return:
    '''
    return string.count("/(") + string.count("/)")

def feat11(string):
    '''
    This function returns the number of elipsis
    :param string:
    :return:
    '''

    return string.count("/:") - string.count(":/") - string.count(";/")

def feat12(string):
    '''
    This function returns the number of common nouns
    :param string:
    :return:
    '''
    return string.count("/NN ") + string.count("/NNS ")

def feat13(string):
    '''
    This function returns the number of proper nouns
    :param string:
    :return:
    '''
    return string.count("/NNP")

def feat14(string):
    '''
    This function returns the number of adverbs
    :param string:
    :return:
    '''
    return string.count("/RB")

def feat15(string):
    '''
    This function returns the number of wh words
    :param string:
    :return:
    '''
    return string.count("/W")

def feat16(string):
    '''
    This function returns the number of slangs in acronyms
    :param string:
    :return:
    '''
    res = 0
    slanglist = ['smh', 'fwb', 'lmfao', 'lmao', 'lms', 'tbh', 'rofl', 'wtf', 'bff', 'wyd', 'lylc',
              'brb', 'atm', 'imao', 'sml', 'btw', 'bw', 'imho', 'fyi', 'ppl', 'sob', 'ttyl',
              'imo', 'ltr', 'thx, kk, omg, ttys, afn, bbs, cya, ez, f2f, gtr', 'ic', 'jk', 'k',
              'ly', 'ya', 'nm', 'np', 'plz', 'ru', 'so', 'tc', 'tmi', 'ym', 'ur', 'u', 'sol']
    for slang in slanglist:
        res += string.count(slang)
    return res

def feat17(string):
    '''
    This function returns the number of all capital words
    :param string:
    :return:
    '''
    res = 0
    string = re.sub("/[A-Z]+", "", string).split()
    for substr in string:
        if(re.match("^[A-Z]{2,}$", substr) != None):
            res += 1
    return res

def feat18(string):
    '''
    This function returns the average length of sentences
    :param string:
    :return:
    '''

    return float(len(string.split())) / (len(string.split("\n")) - 1)


def feat19(string):
    '''
    This function counts the average length of tokens
    :param string:
    :return:
    '''
    string = re.sub("/[A-Z]+", "", string)
    string = re.sub(" [.,:;\'\"?!%()[\]{}]\/[\#$.,():\"\']", "", string).split()
    tot_length = 0
    num_token = len(string)
    for substr in string:
        tot_length += len(substr)
    return tot_length / num_token



def feat20(string):
    '''
    This function counts the number of sentences in a tweet
    :param string:
    :return:
    '''
    return len(string.split("\n") - 1)

import re