from produto import Produto

class GerenciadorDeProdutos:
    def __init__(self):
        self._produtos = []  

    def adicionar_produto(self, nome: str, preco: float, quantidade: int):
        novo_produto = Produto(nome, preco, quantidade)
        self._produtos.append(novo_produto)
        print(f"📦 Produto '{nome}' adicionado com sucesso.")
        return novo_produto

    def _buscar_produto_por_id(self, produto_id: int):
        for produto in self._produtos:
            if produto.id == produto_id:
                return produto
        return None

    def editar_produto(self, produto_id: int, novo_preco: float = None, nova_quantidade: int = None):
        produto_a_editar = self._buscar_produto_por_id(produto_id)
        if produto_a_editar:
            print(f"\n✏️ Editando produto: {produto_a_editar.nome} (ID: {produto_id})")
            if novo_preco is not None:
                produto_a_editar.atualizar_preco(novo_preco)
            if nova_quantidade is not None:
                produto_a_editar.atualizar_estoque(nova_quantidade)
        else:
            print(f"❌ Erro: Produto com ID {produto_id} não encontrado.")

    def excluir_produto(self, produto_id: int):
        produto_a_excluir = self._buscar_produto_por_id(produto_id)
        if produto_a_excluir:
            self._produtos.remove(produto_a_excluir)
            print(f"🗑️ Produto '{produto_a_excluir.nome}' (ID: {produto_id}) foi excluído.")
        else:
            print(f"❌ Erro: Produto com ID {produto_id} não encontrado.")

    def listar_produtos(self):
        print("--- Lista de Produtos Cadastrados ---")
        if not self._produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self._produtos:
                print(produto)
        return self._produtos