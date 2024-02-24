class armas:
     
     def seleccionarArma(self,nombre):
         seleccion=int(input("Selecciona el arma: \n 1=Rifle de asalto\n 2=Espada de energia\n 3=Rifle M392"))

         if(seleccion==1):
            print("rifle de asalto asignado a "+nombre)
            print("Municiones 7.62 * 52mm, sin Mira")
            
         if(seleccion ==2):
            print("espada de energia asignada a "+nombre)
            print("Arma creada por los shangheili")
        
         if(seleccion ==3):
            print("Rifle M392 asignada a "+nombre)
            print("Municiones 7.62 * 52 mm, con mira ")
     
     def recargarArma(self,munucion):
        cargador = 25
        cargador= cargador +munucion
        print("arma recargada al "+ str(cargador) + "%")
        