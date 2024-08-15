Funcionalidade: Cadastro de usuário

    ### Udemy bloqueou depois de algumas tentativas
    #@CadastroUsuario
    #Cenário: Cadastrar novo usuário com sucesso
    #    Dado que a página de cadastro seja acessada
    #    Quando o valor "José Doe" for inserido no campo Nome completo
    #    E o valor "josedoe@gmail.com" for inserido no campo E-mail
    #    E o valor "85&$sfss" for inserido no campo Senha
    #    E o botão Cadastre-se for clicado
    #    Então o usuário é encaminhado para a tela de configuração do usuário

    ### Udemy bloqueou depois de algumas tentativas    
    #@UsuarioExistente
    #Cenário: Cadastrar um usuário que já existe.
    #    Dado que a página de cadastro seja acessada
    #    Quando o valor "José Doe" for inserido no campo Nome completo
    #    E o valor "josedoe@gmail.com" for inserido no campo E-mail
    #    E o valor "85&$sfss" for inserido no campo Senha
    #    E o botão Cadastre-se for clicado
    #    Então o aviso "O e-mail que você inseriu já está em uso. Tente fazer login." deve ser exibida

    @EmailInvalido
    Cenário: Cadastrar usuário com e-mail fora de padrão
        Dado que a página de cadastro seja acessada
        Quando o valor "José Doe" for inserido no campo Nome completo
        E o valor "josedoe@yahoo" for inserido no campo E-mail
        E o valor "85&$sfss" for inserido no campo Senha
        E o botão Cadastre-se for clicado
        Então a mensagem "Este não é um endereço de e-mail válido." deve ser exibida

    @BotaoSenhaVisivel
    Cenário: Testar funcionalidade do botão exibir Senha.
        Dado que a página de cadastro seja acessada
        Quando o valor "85&$sfss" for inserido no campo Senha
        E o botão exibir senha for clicado
        Então a senha deve ser exibida