from gerenciador import GerenciadorDeProdutos

def main():
    gerenciador = GerenciadorDeProdutos()

    print("### PASSO 1: Adicionando novos produtos ###\n")
    gerenciador.adicionar_produto("Notebook Gamer", 7500.00, 10)
    gerenciador.adicionar_produto("Mouse Sem Fio", 150.50, 50)
    gerenciador.adicionar_produto("Teclado Mecânico", 450.00, 30)
    print("\n" + "="*50 + "\n")

    print("### PASSO 2: Listando os produtos atuais ###\n")
    lista_de_objetos = gerenciador.listar_produtos()
    print(f"\nA variável 'lista_de_objetos' contém {len(lista_de_objetos)} objetos Produto.")
    print("\n" + "="*50 + "\n")

    print("### PASSO 3: Editando um produto existente (ID 2) ###")
    gerenciador.editar_produto(produto_id=2, novo_preco=139.99, nova_quantidade=45)
    print("\nListando novamente para ver a alteração:")
    gerenciador.listar_produtos()
    print("\n" + "="*50 + "\n")

    print("### PASSO 4: Excluindo um produto (ID 1) ###\n")
    gerenciador.excluir_produto(produto_id=1)
    print("\n" + "="*50 + "\n")

    print("### PASSO 5: Retornando a lista final de produtos ###\n")
    lista_final = gerenciador.listar_produtos()
    print(f"\nA lista final agora contém {len(lista_final)} objetos Produto.")

if __name__ == "__main__":
    main()