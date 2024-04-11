from fpdf import FPDF
from controlador import *
objcontro12= controlador ()

class GeneradorPDF(FPDF):
    
    def header(self):
        self.set_font("Times", "BU", 14)
        self.cell(0,10,"Reporte de Usuarios",0,1,"C")
        
        
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I",8)
        self.cell(0,10, "Pagina %s"%self.page_no(),0,0,"C")
        
    def chapter_body(self):
        self.set_font("Arial", "I",10)
        self.set_fill_color(135,206,235)
        listaUsuarios= objcontro12.mostrarTodosUsuarios()
        self.multi_cell(100,10,"ID:  "+"Usuario: "+"Correo:  ",1,'C',1)
        
        for i in listaUsuarios:
            self.multi_cell(100.10,str(i[0])+str(i[1])+str(i[2]),1,'C')