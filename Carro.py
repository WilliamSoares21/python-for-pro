class Carro:
    runs = True

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} carro foi ligado")

            
        else:
            print(f"{self.name} carro tá quebrado")




