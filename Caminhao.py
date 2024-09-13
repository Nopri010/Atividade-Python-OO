from Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cavalos):
        super().__init__(marca, modelo, placa, ano)
        self.__cavalos = cavalos
    
    # Sobrescreve o método __str__() da classe Veiculo
    def __str__(self):
        cam = super().__str__()  # Corrigir a chamada do método da superclasse
        return f'''{cam}
 - cavalos: {self.__cavalos}''' 