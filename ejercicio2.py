class Persona:
    def __init__(self, nombre, edad):
        
        
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_informacion(self):
        
        print(self.nombre,self.edad) 

class Alumno(Persona):
    

    def __init__(self, nombre, edad, calificacion):
        
        Persona.__init__(self, nombre, edad)
        self.calificacion = calificacion
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print( self.calificacion)

class Empleado(Persona):
    

    def __init__(self, nombre, edad, sueldo):
        
        Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print( self.sueldo)

alumno1 = Alumno('Glenda', 31, 6)
alumno1.mostrar_informacion()

empleado1 = Empleado('Omar', 45, 1500)
empleado1.mostrar_informacion()
