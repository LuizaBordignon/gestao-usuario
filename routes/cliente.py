from flask import Blueprint, render_template

"""
Rota de Clientes

- /clientes/ (GET) - Listar os clientes
- /clientes/(POST) -inserir o cliente no servidor
- /clientes/new (GET) -renderizar o formulario para criar um cliente
- /clientes/<id>(GET) - obter os dados de um cliente
- /clientes/<id>/edit (GET) - renderizar um formulario para editar um cliente
- /clientes/<id>/update (PUT) - atualizar os dados do cliente
- /clientes/<id>/delete (DELETE) - deleta o registro do usuario

"""

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_cliente():
    #listar clientes
    return render_template('lista_clientes.html')

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    #inserir os dados dos clientes
    pass

@cliente_route.route('/new')
def form_cliente():
    #formulario para cadastrar os clientes
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    #detalhes sobre o cliente
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    #formulario para editar o cliente
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods =['PUT'])
def atualizar_cliente(cliente_id):
    #atualizar informaçoes sobre o cliente
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods =['DELETE'])
def deletar_cliente(cliente_id):
    #deletar o cliente
    pass