class personaje:
    # Atributos del perosnaje de halo 
    
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    # Metodos del personaje de halo
    def correr(self,estado):
        if(estado):
            print("el personaje " + self.nombre + " esta corriendo")
        else:
            print("el personaje " + self.nombre + " esta muerto")
            
            #self para llamar los atributos de la clase
            
    def lanzarGranada(self):
        print(self.nombre + "pego una granada")
        
        
  