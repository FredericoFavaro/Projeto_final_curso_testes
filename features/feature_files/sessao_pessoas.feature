Funcionalidade: Menu superior

        @TesteItemPessoas
        Cenário: Pesquisa e tentativa de acesso do perfil de um usuário
            Dado que o usuário está na página inicial
             Quando clicar no item Pessoas
              E digitar o nome
              E digitar o sobrenome mais ENTER
              E clicar no resultado da busca
             Então o modal de login/cadastro para ver o perfil completo aparece
        
        @TesteItemLearning
        Cenário: Pesquisa e acesso a um curso online
            Dado que o usuário está no início
             Quando clicar no item Learning
              E digitar Power Bi mais ENTER
              E clicar no resultado
              E clicar no botão PLAY
             Então o vídeo é reproduzido
    