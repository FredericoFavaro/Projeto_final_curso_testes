Funcionalidade: Menu superior

        @TesteMenuPessoas
        Cenário: Testando a pesquisa do menu Pessoas
            Dado que o usuário está na página inicial
             Quando clicar no menu Pessoas
              E digitar o nome
              E digitar o sobrenome e clicar ENTER
              E clicar no resultado da busca
             Então o modal de login/cadastro para ver o perfil completo aparece
        
        @TesteMenuLearning
        Cenário: Testando a pesquisa do menu Learning
            Dado que o usuário está no início
             Quando clicar no menu Learning
              E digitar Power Bi e clicar ENTER
              E clicar no resultado
              E clicar no botão PLAY
             Então o vídeo é reproduzido
    