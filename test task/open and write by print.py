with open('frank.txt', 'w') as outfile:
    s='I am dead'
    print(s)
    print(s,file=outfile)
    myfile=None
    print(s, file=myfile)
    print(s, file=None)
