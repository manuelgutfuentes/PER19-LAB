class Producto():
    def __init__(self, nombre, precio):
        self.precio = precio
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
        
class Medicamento(Producto):
    def __init__(self, nombre, precio, porcentaje):
        self.nombre = nombre
        self.precio = precio
        self.porcentaje = porcentaje
    def get_porcentaje(self):
        return self.porcentaje

class Laboratorio():
    def __init__(self, nombre, inventario):
        self.nombre = nombre
        self.inventario = inventario
    def get_nombre(self):
        return self.nombre
    def get_inventario(self):
        return self.inventario
    
    
prod1 = Producto("Gasas", 0.55)
prod2 = Producto("Agujas", 0.35)
medi1 = Medicamento("Ibuprofeno", 1.25, 3)
medi2 = Medicamento("Aspirina", 2.20, 15)
invent = [prod1, prod2, medi1, medi2]
Lab = Laboratorio("Labs SA", invent)