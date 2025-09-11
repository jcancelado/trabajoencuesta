
class Encuesta:
    preguntas = ["¿Cuál es idea de proyecto?", "¿Cual es tu lenguaje de programación favorito?", "¿Tienes algun hobby?"]
    respuestas = []

    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.respuestas = []

    def agregar_respuesta(self, estudiante):
        respuesta_individual = {"estudiante": estudiante}
        for pregunta in self.preguntas:
            respuesta = input(pregunta + " ")
            respuesta_individual[pregunta] = respuesta
        self.respuestas.append(respuesta_individual)

    def mostrar_resultados(self):
        print("Resultados de la encuesta:")
        for i, respuesta in enumerate(self.respuestas, 1):
            estudiante = respuesta["estudiante"]
            print(f"Participante {i}: {estudiante}")
            for pregunta in self.preguntas:
                print(f"{pregunta}: {respuesta[pregunta]}")

    def resumen(self):
        resumen_dict = {pregunta: {} for pregunta in self.preguntas}
        for respuesta in self.respuestas:
            for pregunta in self.preguntas:
                opcion = respuesta[pregunta]
                resumen_dict[pregunta][opcion] = resumen_dict[pregunta].get(opcion, 0) + 1
        return resumen_dict

class Estudiante:
    def __init__(self, nombre, edad, idea_respuesta):
        self.nombre = nombre
        self.edad = edad
        self.idea = idea_respuesta
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Idea de Proyecto: {self.idea}"

if __name__ == "__main__":
        encuesta = Encuesta(Encuesta.preguntas)
        n = int(input("¿Cuántos participantes responderán la encuesta? "))
        for _ in range(n):
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            idea = input("Idea de proyecto del estudiante: ")
            estudiante = Estudiante(nombre, edad, idea)
            # Prepara las respuestas, usando la idea ya capturada
            respuesta_individual = {"estudiante": estudiante}
            respuesta_individual["¿Cuál es idea de proyecto?"] = idea
            for pregunta in encuesta.preguntas:
                if pregunta != "¿Cuál es idea de proyecto?":
                    respuesta = input(pregunta + " ")
                    respuesta_individual[pregunta] = respuesta
            encuesta.respuestas.append(respuesta_individual)
        encuesta.mostrar_resultados()
        print("Resumen de la encuesta (conteo de respuestas):")
        for pregunta, opciones in encuesta.resumen().items():
            print(f"{pregunta}:")
            for opcion, cantidad in opciones.items():
                print(f"  {opcion}: {cantidad}")
