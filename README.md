Debora Costa - RM554196

Leonardo de Oliveira - RM554024

Sara Sousa - RM552656


# NotreDame-Health-Python
Simulação de funcionalidades da aplicação "NotreDame Health" usando Python

## Descrição do Projeto:

O projeto "NotreDame Health" é um sistema de gerenciamento de informações de saúde de usuários. Ele permite a criação de um perfil do usuário, onde são capturadas informações pessoais, incluindo nome, CPF, idade, sexo, e-mail, alergias, tipo de convênio, telefone e endereço. Além disso, o sistema oferece funcionalidades para acessar o histórico de saúde do usuário (tanto padrão quanto personalizado para pacientes oncológicos), informações sobre exames realizados, acompanhamento psicológico e lembretes de medicamentos.

## Funcionalidades Implementadas:
- **Criação de Perfil de Usuário:** Captura de informações pessoais básicas.
- **Acesso ao Histórico de Saúde:** Visualização do histórico padrão ou personalizado, incluindo detalhes sobre batimentos cardíacos, níveis de glicose, peso, atividades diárias, entre outros.
- **Acesso a Informações sobre Exames:** Registro e exibição de detalhes de exames, como data, tipo e resultado.
- **Acesso ao Acompanhamento Psicológico:** Registro e exibição de notas, recomendações, tema da sessão, entre outros.
- **Acesso aos Lembretes de Medicamentos:** Permite adicionar, visualizar e armazenar informações sobre medicamentos, como nome, dosagem, horário e data de início.

## Fluxo de Funcionamento:
1. Inicialmente, a aplicação direciona o usuário para a criação de um perfil, onde são requisitadas informações pessoais.
2. Após criar o perfil, o sistema permite ao usuário acessar diferentes funcionalidades, como histórico de saúde, exames, acompanhamento psicológico e lembretes de medicamentos.
3. O menu de funcionalidades é exibido, permitindo que o usuário escolha a ação desejada.
4. Após acessar uma funcionalidade, é perguntado se deseja acessar outra ou sair do sistema.

## Requisitos:
- **Python:** O código foi escrito em Python, portanto é necessário ter o interpretador Python instalado no ambiente de execução para executar o programa.
- **Entrada de Dados:** O programa utiliza entrada de dados pelo console (usando a função input) para capturar informações do usuário.
- **Validação de CPF e Senha:** As funções `validar_cpf` e `validar_senha` garantem a validação do CPF (11 dígitos) e da senha (com pelo menos 8 caracteres), respectivamente.
