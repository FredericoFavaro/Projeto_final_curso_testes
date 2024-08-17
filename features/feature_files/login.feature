Feature: Login  logoff no Linkedin e test sem senha
  
  @TestLogin
  Scenario: Login com credencias corretas
    Given que o usuário está na página de login
    When é inserido insere email e senha corretos
    Then clica no botão de login e será redirecionado para a página inicial
  
  @TestErroLogin 
  Scenario: Verifica campo senha vazio
    Given dado que o usuário está na página de login
    When Quando ele insere um email 
    And clica no botão login
    Then a mensagem "Insira uma senha." deverá ser exibida

  @TestLogout
  Scenario: Logout
    Given o usuário está na página de login 
    When Quando ele insere email e senha corretos 
    And clica no botão de login e será redirecionado para a página inicial
    Then depois faz o logout