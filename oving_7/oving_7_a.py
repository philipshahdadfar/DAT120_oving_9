

wordlist = dict()

linje_nummer = 0





with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as file:
    
    for linje in file:
        strippet_linje = linje.strip()
        words = strippet_linje.split()
        linje_nummer += 1
        
        #print(strippet_linje)
        
        
        
        
        
        
        for word in words:
            
            
                
            if word in wordlist:
                continue
            else:
                wordlist[word] = linje_nummer
                
                
            
                
    for word in wordlist:
        
            

        
        print(f"Ordet {word} forekommer første gang på linje {wordlist[word]}")
        

