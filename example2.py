from example import Example


class Example2(Example):
    def __init__(self):
        print("Example2 instance is created!!")

    def calcular_frete(self, cep, valor):
        print(f"o valor do frete para o cep {cep} eh: ", (valor/100))
