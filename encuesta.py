#encuesta
class Encuesta:
    preguntas = ["¿Cuál es idea de proyecto?", "¿Cual es tu lenguaje de programación favorito?"]
    respuestas = {}

    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.respuestas = {}

    def agregar_respuesta(self):
        for pregunta in self.preguntas:
            respuesta = input(pregunta + " ")
            self.respuestas[pregunta] = respuesta

    def mostrar_resultados(self):
        print("Resultados de la encuesta:")
        for pregunta, respuesta in self.respuestas.items():
            print(f"{pregunta}: {respuesta}")