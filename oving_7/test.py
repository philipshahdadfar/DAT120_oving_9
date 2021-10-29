def index2(f,word_f):

    infile = open("oving_1_rein_tekst.txt", 'r')
    dct = {}
    # deleted line
    for line in infile:
        newLine = line.replace('\n', ' ')
        if newLine == ' ':
            continue
        # deleted line
        newLine2 = newLine.strip(".")
        split_line = newLine2.split()
        for word in word_f:
            count = 0 # you might want to start at 1 instead, if you're going for 'word number'
            # important note: you need to have 'word2', not 'word' here, and on the next line
            for word2 in split_line: # changed to looping through data
                if word2 == word:                    
                    if word2 in dct:
                        temp = dct[word]
                        temp.append(count)
                        dct[word] = temp
                    else:
                        temp = []
                        temp.append(count)
                        dct[word] = temp
                count += 1
    for word in word_f:
        print('{:12} {},'.format(word,dct[word]))
    infile.close()    