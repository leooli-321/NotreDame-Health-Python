# Debora Costa - RM554196
# Leonardo de Oliveira - RM554024
# Sara Sousa - RM552656


# Funções de validação de CPF e senha
def validar_cpf(cpf):
    return len(cpf) == 11

def validar_senha(senha):
    return len(senha) >= 8

# Função para criar o perfil do usuário
def criar_perfil_usuario():
    # Captura de informações pessoais do usuário
    nome = input("\nNome: ")
    cpf = input("CPF (insira os onze dígitos do CPF): ")

    while True:
        if validar_cpf(cpf): # Verifica se o CPF inserido é válido
            break # Encerra o loop se o CPF for válido
        else: # Solicita ao usuário inserir o CPF novamente em caso de inválido
            print("CPF inválido. Por favor, insira um CPF válido.")
            cpf = input("CPF: ")

# Captura de informações pessoais do usuário
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    email = input("E-mail: ")
    senha = input("Senha (a senha deve conter oito ou mais caracteres): ")

    while True:
        if validar_senha(senha): # Verifica se a senha inserida é válid
            break # Encerra o loop se a senha for válida
        else: # Solicita ao usuário inserir a senha novamente em caso de inválida
            print("Senha inválida. Por favor, insira uma senha válida (pelo menos 8 caracteres).")
            senha = input("Senha: ")

# Captura de informações pessoais do usuário
    alergias = input("Alergias: ")
    tipo_convenio = input("Tipo do Convênio: ")
    telefone = int(input("Telefone: "))

# Lista que armazena as informações de endereço do usuário e retorna a partir das posições de cada campo
    endereco = [
        input("Logradouro: "), #Posição 0
        int(input("CEP: ")), #Posição 1
        input("Bairro: "), #Posição 2
        int(input("Número: ")) #Posição 3
    ]

# Exibe o perfil do usuário criado com sucesso
    print("\nPERFIL DO USUÁRIO CRIADO COM SUCESSO!")
    print(f"\nNome: {nome}\nCPF: {cpf}\nIdade: {idade}\nSexo: {sexo}\nE-mail: {email}\nAlergias: {alergias}")
    print(f"Tipo do Convênio: {tipo_convenio}\nTelefone: {telefone}\n\nINFORMAÇÕES DE ENDEREÇO\n")
    print(f"Logradouro: {endereco[0]}\nCEP: {endereco[1]}\nBairro: {endereco[2]}\nNúmero: {endereco[3]}")

#Após criar o perfil, verifica se o usuário é um paciente oncológico para redirecionar para o histórico de saúde correto
    paciente_oncologico = input("\nVocê é um paciente oncológico? (S/N): ")
    if paciente_oncologico.lower() == "s":
        acessar_historico_saude_personalizado()
    else:
        acessar_historico_saude()
