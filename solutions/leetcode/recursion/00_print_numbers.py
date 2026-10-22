# Tail recursion
def printNumbers(Lrange, Urange):
    if Lrange > Urange:
        return
    print(Lrange)
    printNumbers(Lrange+1, Urange)

# head recursion
def printNumber(Lrange, Urange):
    if Lrange > Urange:
        return
    printNumbers(Lrange+1, Urange)
    print(Lrange)
    
    
printNumbers(1,5) # OUTPUT: 1 2 3 4 5 
printNumber(1,5) # OUTPUT: 5 4 3 2 1 