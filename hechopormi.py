class Encuesta:
    def __init__(self):
        self.preguntas = [
            "¿Qué tema prefieres para el proyecto?",
            "¿Sabes trabajar en equipo?",
            "¿Conoces alguna librería de Python?"
        ]
        self.respuestas = [] 
    def agregar_respuesta(self):
        respuestas_estudiante = []
        for pregunta in self.preguntas:
            respuesta = input(pregunta, ": ")
            respuestas_estudiante.append(respuesta)
            self.respuestas.append(respuesta_estudiante)
    def mostrar_resultados(self):
        for i, respuestas_estudiante in enumerate(self.respuestas, start=1) :
            print(f"Estudiante{1}:")
            for pregunta, respuesta in zip(self.preguntas, self.respuesta_estudiante):
                print(f"{pregunta}->{respuesta}")
            print(resultado)    
class Estudiante:
    def __init__(self, nombre, edad, respuesta_proyecto):
        self.nombre = nombre
        self.edad = edad
        self.respuesta_proyecto = respuesta_proyecto
# Creamos una encuesta de ejemplo

mi_encuesta = Encuesta(preguntas)
print(mi_encuesta.preguntas)  # solo para verificar
