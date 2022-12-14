import funcoes

validar= funcoes.Validar_cpf()

while True:
    opcao = str(input(' 1. Gerar um CPF\n 2. Validar um CPF\nO que deseja fazer? '))

    if opcao == '1':
        novo_cpf = validar.gerar_cpf()
        print(validar.formatar_string_novo_cpf(novo_cpf))

    elif opcao== '2':
        cpf_usuario = str(input('Digite seu cpf: '))
        
        validador_cpf = validar.validar_cpf(cpf_usuario)
        
        if validador_cpf:
            print('CPF Válido')
        else:
            print('CPF Inválido')

    else:
        print('Opção inválida')

