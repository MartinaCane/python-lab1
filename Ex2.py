var=0

while var==0:
    print("Enter a word:")
    phrase = input()
    int(len(phrase))
    limit=2
    print("The lenght of the word is ", len(phrase))
    if int(len(phrase)) >= limit:
        print(phrase[0],phrase[1], phrase[len(phrase)-2],phrase[len(phrase)-1])
        var=1
    else:
        print("The word should have more than three characters")