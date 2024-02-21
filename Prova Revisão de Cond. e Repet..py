#EMAIL E SENNHA CADASTRADOS 
email_cad = 'joao123@gmail.com'
senha_cad = 'joaozinho123456'


#LOOP DE REPETIÇÃO
while True:
    email_usuario = str(input('Digite o seu email cadastrado: '))
    senha_usuario = str(input('Digite a sua senha cadastrada: '))

    if email_cad == email_usuario and senha_cad == senha_usuario:
        print('cadastro valido')
        break
    else:
        print('Email ou senha errados tente novamente')
        
    