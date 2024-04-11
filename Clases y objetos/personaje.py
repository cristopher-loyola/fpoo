class personaje:
    # Atributos del perosnaje de halo 
    
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    def get_especie(self):
        return self.__especie
   
    def get_nombre(self):
        return self.__nombre
   
    def get_altura(self):
        return self.__altura
   
    def set_especie(self,especie):
            self.__especie = _especie

    def set_nombre(self,nombre):
            self._nombre = _nombre
        
    def set_altura(self,altura):
        self.__altura = _altura
    
    def __pensar(self):
        print(self.__nombre)
   
   
    # Metodos del personaje de halo
    def correr(self,__estado):
        if(__estado):
            print("el personaje " + self.get_nombre() + " esta corriendo")
        else:
            print("el personaje " + self.get_nombre() + " esta muerto")
            
            #self para llamar los atributos de la clase
            
    def lanzarGranada(self):
        print(self.get_nombre() + " pego una granada")
        
        
  