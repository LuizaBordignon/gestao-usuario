from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

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
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    #inserir os dados dos clientes
    data = request.json
    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )
    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    #formulario para cadastrar os clientes
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    #detalhes sobre o cliente
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    #formulario para editar o cliente
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods =['PUT'])
def atualizar_cliente(cliente_id):
    #atualizar informaçoes sobre o cliente
    cliente_editado = Cliente.get_by_id(cliente_id)
    data = request.json
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()

    #editar o usuario
    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods =['DELETE'])
def deletar_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}