class contador_palabra():
    contador = 0
    palabras = ""

    def contador_palabras(self, palabra):
        self.palabras = palabra.split()
        self.contador = len(self.palabras)
        return  self.contador

contar_palabra = contador_palabra()
contar_palabra.palabras = input( "Dame  una frase: ")
contar_palabra.frase = contar_palabra.contador_palabras(contar_palabra.palabras)
print(contar_palabra.frase)