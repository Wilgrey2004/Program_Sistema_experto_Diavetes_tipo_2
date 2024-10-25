class Agente_De_Diavetes_Tipo_2: 
        preguntas = [
                "¿Tiene antecedentes familiares de diabetes? (Sí / No)",
                "¿Presenta síntomas de sed excesiva (polidipsia)? (Sí / No)",
                "¿Ha experimentado aumento de hambre (polifagia)? (Sí / No)",
                "¿Siente fatiga o cansancio inusual de manera frecuente? (Sí / No)",
                "¿Ha notado una pérdida de peso inesperada recientemente? (Sí / No)",
                "¿Tiene visión borrosa frecuentemente? (Sí / No)",
                "¿Le cuesta que las heridas sanen rápidamente? (Sí / No)",
                "¿Experimenta hormigueo o entumecimiento en manos o pies? (Sí / No)",
                "¿Tiene hipertensión o presión arterial elevada? (Sí / No)",
                "¿Lleva un estilo de vida sedentario (ejercicio menos de tres veces por semana)? (Sí / No)"
                ]
        respuestas= [False,False,False,False,False,False,False,False,False,False]
        
        def __init__(self) -> None:
                pass
        
        def Contar(self):
            contador = 0
            for i in range(len(self.respuestas)):
                if(self.respuestas[i]):
                    contador =+1

        def Preguntar(self):
            for i in range(len(self.preguntas)):
                print(f" Pregunta Numero {i+1}){self.preguntas[i]} ")
                req = input("Respuesta aqui (Si o No) =>")
                for e in range(len(self.respuestas)):
                    if req == "Si" or req == "si" or req == "s" or req == "S" :
                        self.respuestas[e] == True
                    elif req == "No" or req == "no" or req == "n" or req == "N" :
                        continue
                        
            return self.Contar()
            
            pass
                