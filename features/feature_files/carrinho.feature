Funcionalidade: Adicionar e Remover Carrinho

  @Adicionaraocarrinho
  Cenário: Verificar e clicar no botão "Ir para o carrinho"
    Dado que estou na página do produto
    Quando verifico se o texto do botão é "Adicionar ao carrinho"
    E clicar no botão e adiciono o produto
    Então o item é inserido no carrinho

    
  # @RemovendodoCarrinho
  # Cenário: Removendo um curso do carrinho
  #   Dado O usuário está na página do carrinho
  #   Quando verifico se o conteudo de texto do botão é "Remover"
  #   Então clico no botão e removo o item