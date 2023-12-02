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

# Função para acessar o histórico de saúde personalizado
def acessar_historico_saude_personalizado():
    # Captura de informações do histórico de saúde padrão
    batimentos_cardiacos = int(input("\nBatimentos Cardíacos: "))
    niveis_glicose = float(input("Níveis de Glicose: "))
    peso = float(input("Peso: "))
    atividades_diarias = int(input("Duração de Atividades Físicas Diárias: "))
    duracao_sono = int(input("Duração do Sono: "))

    # Captura de informações específicas para pacientes oncológicos
    print(f"\nINFORMAÇÕES ADICIONAIS DO HISTÓRICO PERSONALIZADO\n")
    tipo_cancer = input("Tipo de câncer: ")
    estagio_cancer = input("Estágio do câncer: ")
    tipo_tratamento = input("Tipo de tratamento: ")
    resposta_tratamento = input("Resposta ao tratamento: ")

    pressao_arterial = [
        int(input("Pressão Sistólica: ")),
        int(input("Pressão Diastólica: "))
    ]
# Exibe o histórico de saúde personalizado
    print("\nHISTÓRICO DE SAÚDE PERSONALIZADO\n")
    print(f"Batimentos Cardíacos: {batimentos_cardiacos}\nNíveis de Glicose: {niveis_glicose}\nPeso: {peso}\nDuração de Atividades Físicas Diárias: {atividades_diarias}\nDuração do Sono: {duracao_sono}\nTipo de câncer: {tipo_cancer}"
          f"\nEstágio do câncer: {estagio_cancer}\nTipo de tratamento: {tipo_tratamento}\nResposta ao tratamento: {resposta_tratamento}")
    print(f"Pressão Sistólica: {pressao_arterial[0]}\nPressão Diastólica: {pressao_arterial[1]}")

# Função para acessar o histórico de saúde padrão
def acessar_historico_saude():
    # Captura de informações do histórico de saúde padrão
    batimentos_cardiacos = int(input("\nBatimentos Cardíacos: "))
    niveis_glicose = int(input("Níveis de Glicose: "))
    peso = float(input("Peso: "))
    atividades_diarias = int(input("Duração de Atividades Físicas Diárias: "))
    duracao_sono = int(input("Duração do Sono: "))

    pressao_arterial = [
        int(input("Pressão Sistólica: ")),
        int(input("Pressão Diastólica: "))
    ]
# Exibe o histórico de saúde padrão
    print("\nHISTÓRICO DE SAÚDE\n")
    print(f"Batimentos Cardíacos: {batimentos_cardiacos}\nNíveis de Glicose: {niveis_glicose}\nPeso: {peso}")
    print(f"Duração de Atividades Físicas Diárias: {atividades_diarias}\nDuração do Sono: {duracao_sono}")
    print(f"Pressão Sistólica: {pressao_arterial[0]}\nPressão Diastólica: {pressao_arterial[1]}")

# Função para acessar informações sobre exames
def acessar_exames():
    # Captura de informações sobre exames
    data_exame = input("\nData do Exame: ")
    tipo_exame = input("Tipo de Exame: ")
    resultado_exame = input("Resultado do Exame: ")

# Exibe informações sobre o exame
    print("\nEXAMES\n")
    print(f"Data do Exame: {data_exame}\nTipo de Exame: {tipo_exame}\nResultado do Exame: {resultado_exame}")

# Função para acessar informações sobre acompanhamento psicológico
def acessar_acompanhamento_psicologico():
    # Captura de informações sobre acompanhamento psicológico
    numero_sessoes = int(input("\nNúmero de Sessões: "))
    notas = input("Notas (descrição) sobre a sessão: ")
    recomendacoes = input("Recomendações: ")
    tema_sessao = input("Tema da Sessão: ")
    avaliacao = input("Avaliação da Sessão (de 0 a 10 e o porquê): ")
    proximo_encontro = input("Próximo Encontro (expectativa, data etc): ")

# Exibe informações sobre o acompanhamento psicológico
    print("\nACOMPANHAMENTO PSICOLÓGICO\n")
    print(f"Número de Sessões: {numero_sessoes}\nNotas: {notas}\nRecomendações: {recomendacoes}")
    print(f"Tema da Sessão: {tema_sessao}\nAvaliação: {avaliacao}\nPróximo Encontro: {proximo_encontro}")
