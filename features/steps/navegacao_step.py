from behave import given, when, then
from features.pages.navegacao_page import NavegacaoPage
import time

# region Artigo em Alemao
@given(u'que estou na página inicial do LinkedIn')
def step_impl(context):
  context.driver.get("https://www.linkedin.com/")
  context.navegacao_page = NavegacaoPage(context.driver)
  time.sleep(5)


@when(u'clico em artigos na página inicial')
def clicar_artigo(context):
  context.navegacao_page.clicar_artigo()
  time.sleep(5)
    
@when(u'clico no ícone de "Idioma" no rodapé da página')
def clicar_idioma(context):
  context.navegacao_page.fechar_x()
  context.navegacao_page.clicar_modal_idioma()
  time.sleep(5)


@when(u'seleciono "{valor}" na lista de idiomas disponíveis')
def selecionar_alemao(context, valor):
  context.navegacao_page.escolher_linguagem(valor)
  time.sleep(5)
    

@then(u'a página deve ser recarregada em Alemão')
def ficar_pag(context):
  context.navegacao_page.exibir_pagina_alemao()
  time.sleep(20)

    

# endregion

# region FiltrandoVagas
@given(u'que estou na pagina inicial do LinkedIn')
def step_impl(context):
  context.driver.get("https://www.linkedin.com/")
  context.navegacao_page = NavegacaoPage(context.driver)


@when(u'clico na aba "Vagas" na barra de navegação')
def clicar_vagas(context):
  context.navegacao_page.clicar_vagas()
  time.sleep(5)
    

@when(u'digito "Gerente" no campo vaga')
def step_impl(context):
  context.navegacao_page.preencher_campo_vaga('G')
  time.sleep(1)
  context.navegacao_page.preencher_campo_vaga('e')
  time.sleep(1)
  context.navegacao_page.preencher_campo_vaga('r')
  time.sleep(1)
  context.navegacao_page.preencher_campo_vaga('e')
  time.sleep(1)
  context.navegacao_page.preencher_campo_vaga('n')
  time.sleep(3)
  context.navegacao_page.clicar_opcao_vaga()
  time.sleep(2)

    

@when(u'Limpo o campo de Local e digito "Brasil"')
def step_impl(context):  
  context.navegacao_page.apaga_local()
  time.sleep(1)
  context.navegacao_page.preencher_campo_local('B')
  time.sleep(1)
  context.navegacao_page.preencher_campo_local('r')
  time.sleep(1)
  context.navegacao_page.preencher_campo_local('a')
  time.sleep(1)
  context.navegacao_page.preencher_campo_local('s')
  time.sleep(1)
  context.navegacao_page.clicar_opcao_local()
  time.sleep(3)

   

@when(u'eu clico nos filtros "Remoto" e "Fortaleza, CE"')
def step_impl(context):
  context.navegacao_page.escolher_remoto_local()
  time.sleep(2)


@then(u'a página deve mostrar a vaga filtrada')  
def step_impl(context):
  time.sleep(10)


    

# endregion