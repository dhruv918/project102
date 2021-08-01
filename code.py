def countNoOfWord():
    filename=input("enter file name")
    noofword=0
    file=open(filename,'r')
    for line in file:
        word = line.split()
        noofword=noofword+len(word)
    print(noofword)

countNoOfWord()    