
class Estudiante:
    def __init__(self, nombre, edad, respuestas):
        self.nombre = nombre
        self.edad = edad
        self.respuestas = respuestas   
class Encuesta:
    def __init__(self):
        self.preguntas = [
            "¿Cuál es tu idea de proyecto?",
            "¿Cuál es tu lenguaje de programación favorito?",
            "¿Tienes algún hobby?"
        ]
        self.respuestas = []  

    def agregar_respuesta(self, estudiante):
        self.respuestas.append(estudiante)

    def mostrar_resultados(self):
        print("RESULTADOS DE LA ENCUESTA")
        for est in self.respuestas:
            print(f"{est.nombre} ({est.edad} años)")
            for i, r in enumerate(est.respuestas):
                print(f"   {self.preguntas[i]} → {r}")

    def resumen(self):
        print("RESUMEN DE RESPUESTAS")
        for i, pregunta in enumerate(self.preguntas):
            conteo = {}
            for est in self.respuestas:
                resp = est.respuestas[i]
                conteo[resp] = conteo.get(resp, 0) + 1
            print(f"{pregunta}")
            for opcion, cantidad in conteo.items():
                print(f"   {opcion}: {cantidad}")
def main():
    encuesta = Encuesta()

    print("ENCUESTA DE IDEAS DE PROYECTO")

    n = int(input("¿Cuántos estudiantes responderán la encuesta?: "))

    for _ in range(n):
        print("Nuevo Estudiante")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        respuestas = []
        for p in encuesta.preguntas:
            r = input(f"{p}: ")
            respuestas.append(r)
        estudiante = Estudiante(nombre, edad, respuestas)
        encuesta.agregar_respuesta(estudiante)
    encuesta.mostrar_resultados()
    encuesta.resumen()


if __name__ == "__main__":
    main()
