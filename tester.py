def tfSeq(size):
 
  if size > 1:
    for head in tfSeq(size-1):
      yield head + [True]
      yield head + [False]
  else:
    yield [True]
    yield [False]

def truthtable(vars, funcs):
    output = ''

    lVars = str(len(vars))
    lFuncs = str(len(funcs))


    l = len(vars) + len(funcs)
    

    
    output += (r'\begin{tabular}{|' + r'c|' * l + '}')
  
    
    labels = vars + [func[0] for func in funcs]
    #output += '&'.join(['$'+label+'$' for label in labels]) + r'\\'
    output += '\n\hline ' + '& '.join(['$'+label+'$ ' for label in labels]) + r' \\'
    output += '\n'

    tfText = {True:'T', False:'F'}

    i = 0
    for tf in tfSeq(len(vars)):
        i+= 1
        values = [tfText[val] for val in tf] 
        
        values += ([tfText[func[1](*tf)] for func in funcs])
        
        output += '\hline '
        output += '&'.join(values) + '\\\\\n'
        

    output += r'\end{tabular}'

    return output


# Example use...
#if __name__ == '__main__':
    '''print(truthtable(['p','q'], [('p \lor q', lambda p,q: (p or q)),('\sim(p \lor q)', lambda p,q: not(p) and not(q))]))'''

    #p = input("enter first var: ")
    #q = input("enter second var: ")
    #r = input("enter third var: ")

    #vars = input("enter vars seperated by ',' for example p,q,r: ").split(",")

    #funcs = input("enter funcs ")

'''
    print(truthtable(['p','q','r'],[('((\sim p \wedge q) \wedge(q \wedge r)) \wedge \sim q', lambda p,q,r: ((not p and q) and (q and r)) and not q)]))
    '''