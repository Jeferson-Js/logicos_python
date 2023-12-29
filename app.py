# In this array is responsible to register the users
usuarios = []

# Function responsible for register the users
def cadastrar_usuarios():
    cadastro_nome = input('Digite seu nome: ')
    cadastro_senha = input('Digite sua senha: ')
    usuarios.append({'nome': cadastro_nome, 'senha': cadastro_senha})
    print('Cadastro realizado com sucesso.')

# Function responsible for logging
def fazer_login():
    nome_usuario = input('Digite seu nome: ')
    senha_usuario = input('Digite sua senha: ')

    for usuario in usuarios:
        if usuario['nome'] == nome_usuario and usuario['senha'] == senha_usuario:
            print('Login realizado com sucesso')
            return
    print('Usuário ou senha invalidos tente novamente')

cadastrar_usuarios()
fazer_login()