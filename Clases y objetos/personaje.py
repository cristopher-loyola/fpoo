class personaje:
    # Atributos del perosnaje de halo 
    
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
    # Metodos del personaje de halo
    def correr(self,estado):
        if(estado):
            print("el personaje " + self.nombre + " esta corriendo")
        else:
            print("el personaje " + self.nombre + " esta muerto")
            
            #self para llamar los atributos de la clase
            
    def lanzarGranada(self):
        print(self.nombre + " pego una granada")
        
        
  