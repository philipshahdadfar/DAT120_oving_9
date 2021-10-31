

class Flervalgssporsmaal:
    
    def __init__(self, sporsmaal, riktig_svar, valg):
        self.__sporsmaal = sporsmaal
        self.__valg = valg
        self.__riktig_svar = riktig_svar
    
    @property
    def sporsmaal(self):
        return self.__sporsmaal
    @property
    def valg(self):
        return self.__valg
    @property
    def riktig_svar(self):
        return self.__riktig_svar
  

    
    
    def sjekk_svar(self, svaret):
        if svaret == self.riktig_svar:
            return True
        else:
            return False
        
    def __str__(self):
        tekst = "Spørsmål:  " 
        tekst += self.sporsmaal + "\n"
        
        for valg_nr, svar in enumerate(self.valg):
            tekst += f"{valg_nr}: {svar} \n"
            
        return tekst
    
    def korrekt_svar_tekst(self):
        tekst = "Korrekt svar!"
        
        return tekst
        
        
        


    
    
    

        

        
    
   




def lag_sporsmaal():
    sporsmaalene = []
    
    file = open("sporsmaalsfil.txt", "r", encoding="UTF8")

    for line in file:
    
        stripped_line = line.strip()
    
        stripped_line = stripped_line.replace("[","")
        stripped_line = stripped_line.replace("]","")
            
        split_line = stripped_line.split(":")
            
        #print(split_line)
                
        
        question = split_line[0]
        
        answer = int(split_line[1])
        
        options = split_line[2]
    
        opt1 = options.split(",")
    
    
        sporsmaalene.append(Flervalgssporsmaal(question, answer, opt1))
    
    
    
    return sporsmaalene





if __name__ == "__main__":
    sporsmaalene = lag_sporsmaal()
    riktig_svar = 0
    for sporsmaal in sporsmaalene:
        print(sporsmaal)
        svar = input("Skriv inn svaret ditt: ")
        svar = int(svar)
        if sporsmaal.sjekk_svar(svar):
            print("Riktig!\n")
            riktig_svar += 1
        else:
            print("Feil!")
    print(f"{riktig_svar} riktige av {len(sporsmaalene)}.")


    
        
   
        



  

        
    
       
        
    
        
        
        
        
        
        
       
                    
      
    
    