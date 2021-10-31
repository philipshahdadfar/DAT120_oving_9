with open("sporsmaalsfil.txt", "r", encoding="UTF8") as file:

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
        
        def sporsmaal_fra_fil():
            
            
            for line in file:
                
                stripped_line = line.strip()
            
                split_line = stripped_line.split(":")
            
                #print(split_line)
                
                question = split_line[0]
        
                answer = split_line[1]
        
                options = split_line[2]
                
        
        
            
            
            
    
    
    def lag_sporsmaal():
        sporsmaalene = []
        sporsmaalene.append(Flervalgssporsmaal("Hvor ligger UiS?", 1, 
                                      ["Bergen", "Stavanger", "Oslo", "Kristiansand"]))
        sporsmaalene.append(Flervalgssporsmaal("Hva er 2+2?", 3,
                                      ["1", "2", "3", "4"]))
        
        return sporsmaalene




    


            
    
        
    
        
        
      
        
    
        
        
        
        
        
        
       
                    
                
                
                
              
                
 
                
                
            
            
            
    
        

        
        
        
        
        
        
    











    
    
    
    
    
    