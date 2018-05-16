from pythonds.basic.stack import Stack
def paranbalancer(symbolstring):
    index = 0
    s = Stack()
    balancedstring = True
    while index < len(symbolstring):
        symbol=symbolstring[index]
        if (symbol == '('):
            s.push(symbol)
        else:
            if (s.isEmpty()==True):
                balancedstring = False
            else:
                s.pop()
        index += 1

    if(s.isEmpty()==True and balancedstring==True):
        print('Expression is balanced')
    else:
        print ("Expression is unbalanced")

def multiparanbalancer(symbolstring):
    index = 0
    s = Stack()
    balancedstring = True
    while index < len(symbolstring):
        symbol=symbolstring[index]
        if (symbol in '([{'):
            s.push(symbol)
        else:
            if (s.isEmpty()==True):
                balancedstring = False
            else:
                top = s.pop()
                if (matches(top,symbol)==False):
                    balancedstring=False
        index += 1
    if(s.isEmpty()==True and balancedstring==True):
        print('Expression is balanced')
    else:
        print ("Expression is unbalanced")

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open)==closers.index(close)


multiparanbalancer('((()))')
