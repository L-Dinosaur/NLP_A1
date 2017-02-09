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
    pass

def feat8(string):
    pass

def feat9(string):
    pass

def feat10(string):
    pass

def feat11(string):
    pass

def feat12(string):
    pass

def feat13(string):
    pass

def feat14(string):
    pass

def feat15(string):
    pass

def feat16(string):
    pass

def feat17(string):
    pass

def feat18(string):
    pass

def feat19(string):
    pass

def feat20(string):
    pass