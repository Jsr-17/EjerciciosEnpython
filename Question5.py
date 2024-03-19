class Conversor(object):
    
    def __init__(self):
        self.string=""
    
    def getString(self):
      self.string=input("Introduzca una cadena de texto") 
    def  printString(self):
        print(self.string.upper())

texto=Conversor()
texto.getString()
texto.printString()