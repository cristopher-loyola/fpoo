#creamos nuestra clase
class Personaje:
    #Atributos de personaje
    especie="humano"
    nombre="john"
    altura=2.18 #si es un valor flotante no va entre comillas
    
    #Metodos del personaje
    def correr(self,estado):
        if(estado):
            print("el personaje esta corriendo "+self.nombre+" esta corriendo")
        else:
                print("el personaje esta corriendo "+self.nombre+" esta muerto")
    def lanzarGranada(self):
        print(self,nombre+" Pego una granada")
        
    def recargarArma(self, municion):
        cargador=25
        cargador= cargador+ municion
        print("Arma recargada al "+ str(cargador)+"%")
#Creamos el objeto de la clase personaje    
spartan = Personaje()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)
