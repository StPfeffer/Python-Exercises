class Sku():
    def __init__(self) -> None:
        pass


    def Codigo(self) -> int:
        return -1 # deve retornar o código de barras

    
    def Imagens(self) -> str:
        return "image.png"


class Produto(Sku):
    def __init__(self, descricao: str, marca: str, departamento: str, estoque: int) -> None:
        self.descricao = descricao
        self.marca = marca
        self.departamento = departamento
        self.estoque = estoque

    
    def __str__(self) -> str:
        return f"{self.descricao}, {self.marca}, {self.departamento}, {self.estoque}"


    def Descricao(self) -> str:
        return self.descricao


    def Marca(self) -> str:
        return self.marca


    def Departamento(self) -> str:
        return self.departamento

    
    def Estoque(self) -> int:
        return self.estoque


if __name__ == '__main__':
    sku = Produto("televisão 55 polegadas", "samsung", "eletrônicos", 6)

    print(sku)