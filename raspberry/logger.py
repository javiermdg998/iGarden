from datetime import datetime
class Fichero():
    def __init__(self, p, today):
        self.path = p 
        f = open(self.path, "a")
        f.write(today)
        f.close()
    def escribir(self, txt):
        f = open(self.path, "a")
        f.write(txt)
        f.close()
