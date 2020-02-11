# Example use...
import tester
if __name__ == '__main__':

    '''
    print(tester.truthtable(
        ['p','q'], 
        [
            ('p \lor q', lambda p,q: (p or q)),
            ('\sim(p \lor q)', lambda p,q: not(p) and not(q)
            )
        ]))
    '''

    f = open("output.txt", "w")

    #CHANGE THIS STUFF HERE

    #these are your variables
    var = ['p','q','r']
    func = [
            # inside '' is the latex header
            # following it is the lambda evaluation for the latex header. Don't fuck this up
            # you can reference previous entries using IIFE lambdas or just type it in again
            ('\sim p', lambda p,q,r: not p),
            ('\sim q', lambda p,q,r: not q),
            ('(\sim p \wedge q', lambda p,q,r: (not p and q)),
            ('(q \wedge r)', lambda p,q,r: q and r),
            ('((\sim p \wedge q) \wedge (q \wedge r))', lambda p,q,r: func[2][1](p,q,r) and func[3][1](p,q,r)),
            ('((\sim p \wedge q) \wedge(q \wedge r)) \wedge \sim q', lambda p,q,r: ((not p and q) and (q and r)) and not q)


    ]



    f.write(tester.truthtable(
        var,
        func
        ))
    print("done")
    f.close()
    