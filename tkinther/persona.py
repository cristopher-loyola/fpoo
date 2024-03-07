class persona:

    # Constructor
    def __init__(self):
        self._listaBD = []

    # Métodos del CRUD
    def insertar(self, id, nom, edad):
        self._listaBD.append({"Id": id, "Nombre": nom, "Edad": edad})

    def consultarTodos(self):
        print(self._listaBD)

    def buscarUsuario(self, id):
        encontrado = False
        for usuario in self._listaBD:
            if usuario['Id'] == id:
                print(usuario)
                encontrado = True
                break
        if not encontrado:
            print("Usuario no encontrado")

    def eliminar(self, id):
        for usuario in self._listaBD:
            if usuario['Id'] == id:
                self._listaBD.remove(usuario)
                print(":: Usuario Eliminado ::")
                self.consultarTodos()
                return
        print("Usuario no encontrado")

    def editar(self, id, nom, edad):
        for usuario in self._listaBD:
            if usuario['Id'] == id:
                usuario['Nombre'] = nom
                usuario['Edad'] = edad
                print(":: Usuario Editado ::")
                self.consultarTodos()
                return
        print("Usuario no encontrado")

