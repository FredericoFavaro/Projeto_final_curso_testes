Funcionalidade: Cadastro de usuário

    @VerificacaoSegurancaCadastro
    Cenário: Checar janela de verificação de segurança durante cadastro
        Dado que a página de cadastro esta aberta
        Quando o valor "josedoe@gmail.com" for inserido no campo E-mail
        E o valor "85&$sfss" for inserido no campo Senha
        E o botão Cadastre-se for clicado
        E o valor "Jose" for inserido no campo Nome
        E o valor "Doe" for inserido no campo Sobrenome
        E o botão Continue for clicado
        Então o usuário é encaminhado para a tela verificação de segurança

    @BotaoVisibilidadeSenha
    Cenário: Testar funcionalidade do botão exibir Senha.
        Dado que a página de cadastro esta aberta
        Quando o valor "85&$sfss" for inserido no campo Senha
        E o botão exibir senha for clicado
        Então a senha deve ser exibida
