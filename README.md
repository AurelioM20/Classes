Sistema de Gerenciamento de Produtos em Python
Este projeto é um exemplo didático que demonstra os conceitos fundamentais da Programação Orientada a Objetos (POO) em Python. Ele simula um sistema básico de gerenciamento de produtos com operações de CRUD (Create, Read, Update, Delete), estruturado de forma modular e organizada.

Funcionalidades
Criação de Objetos: Instancia objetos a partir de uma classe Produto.

Operações CRUD:

Adicionar: Adiciona novos produtos a uma lista de gerenciamento.

Listar: Exibe todos os produtos cadastrados com seus respectivos detalhes.

Editar: Atualiza informações (preço e/ou quantidade) de um produto existente.

Excluir: Remove um produto da lista.

Geração Automática de ID: Cada produto recebe um ID único e sequencial automaticamente no momento da criação.

Código Modular: O projeto é dividido em três arquivos, cada um com uma responsabilidade clara, facilitando a manutenção e o reuso do código.

Estrutura do Projeto
O projeto é composto por três arquivos principais:

📄 produto.py

Responsabilidade: Define a classe Produto, que serve como o modelo para os objetos de produto. Contém os atributos (id, nome, preco, quantidade) e os métodos para atualizar seus dados (atualizar_preco, atualizar_estoque).

📄 gerenciador.py

Responsabilidade: Contém a classe GerenciadorDeProdutos, que gerencia a coleção de objetos Produto. Toda a lógica de adicionar, editar, excluir e listar os produtos é implementada neste módulo.

📄 main.py

Responsabilidade: É o ponto de entrada da aplicação. Ele utiliza a classe GerenciadorDeProdutos para executar as operações em sequência e demonstrar o funcionamento completo do sistema.
