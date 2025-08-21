class Produto:
    _id_counter = 1  

    def __init__(self, nome: str, preco: float, quantidade: int):
        self.id = Produto._id_counter
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        Produto._id_counter += 1

    def __str__(self):
        return f"ID: {self.id} | Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.quantidade} unidades"

    def atualizar_preco(self, novo_preco: float):
        if novo_preco > 0:
            self.preco = novo_preco
            print(f"✅ Preço do produto '{self.nome}' atualizado para R${novo_preco:.2f}.")
        else:
            print("❌ Erro: O preço deve ser um valor positivo.")

    def atualizar_estoque(self, nova_quantidade: int):
        if nova_quantidade >= 0:
            self.quantidade = nova_quantidade
            print(f"✅ Estoque do produto '{self.nome}' atualizado para {nova_quantidade} unidades.")
        else:
            print("❌ Erro: A quantidade em estoque não pode ser negativa.")