class Celular:
    def __init__(self,so): #Sempre é chamado pelo python quando um objeto da classe é instanciado
        self.sistema_operacional = so
        print(f"celular criado com o sistema operacional {so}")

    def ligar(self):
        print("celular ligando")