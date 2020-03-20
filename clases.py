class Paciente():

    def __init__(self,nombre_completo, edad):
        self.nombre_completo= nombre_completo
        self.edad= edad

class Paciente_no_infectado(Paciente):

     def __init__(self,nombre_completo,edad,telefono):
        Paciente.__init__(self,nombre_completo,edad)
        self.telefono= telefono

class Paciente_posible_infectado(Paciente):

    def __init__(self,nombre_completo,edad,direccion,ciudad,estado):
        Paciente.__init__(self,nombre_completo,edad)
        self.direccion= direccion
        self.ciudad=ciudad
        self.estado=estado

class Paciente_infectado(Paciente_posible_infectado):
    def __init__(self,nombre_completo,edad,direccion,ciudad,estado,doctor):
        Paciente_posible_infectado.__init__(self,nombre_completo,edad,direccion,ciudad,estado)
        self.doctor=doctor


class Pais():
    def __init__(self,nombre_pais,infectados,muertos,recuperados):

        self.nombre_pais=nombre_pais
        self.infectados=infectados
        self.muertos=muertos
        self.recuperados=recuperados

        

