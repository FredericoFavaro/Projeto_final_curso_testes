from behave import given, when, then
from features.pages.cadastro_page import CadastroPage
import time

# region Teste Cadastro 
@given(u'que a página de cadastro esta aberta')
def step_impl(context):
    context.driver.get("https://www.linkedin.com/signup?_l=pt&trk=guest_homepage-basic_nav-header-join")
    context.cadastro_page = CadastroPage(context.driver)

@when(u'o valor "{email}" for inserido no campo E-mail')
def inserir_texto_campo_email(context, email):
    context.cadastro_page.preencher_campo_email(email)
    time.sleep(1)

@when(u'o valor "{senha}" for inserido no campo Senha')
def inserir_texto_campo_senha(context, senha):
    context.cadastro_page.preencher_campo_senha(senha)
    time.sleep(1)

@when(u'o botão Cadastre-se for clicado')
def cadastrar(context):
    context.cadastro_page.clicar_botao_cadastrese()
    time.sleep(1)

@when(u'o valor "{nome}" for inserido no campo Nome')
def inserir_texto_campo_email(context, nome):
    context.cadastro_page.preencher_campo_nome(nome)
    time.sleep(1)

@when(u'o valor "{sobrenome}" for inserido no campo Sobrenome')
def inserir_texto_campo_sobrenome(context, sobrenome):
    context.cadastro_page.preencher_campo_sobrenome(sobrenome)
    time.sleep(1)

@when(u'o botão Continue for clicado')
def cadastrar(context):
    context.cadastro_page.clicar_botao_cadastrese()
    time.sleep(5)

@then(u'o usuário é encaminhado para a tela verificação de segurança')
def tela_verificacao(context):
    texto_seguranca = context.cadastro_page.checar_texto_seguranca()
    assert texto_seguranca == "Verificação de segurança", f"Mensagem de erro:\nO texto '{texto_seguranca}' foi diferente do esperado 'Verificação de segurança'"
    time.sleep(1)

# endregion

# region botão senha visível

@when(u'o botão exibir senha for clicado')
def cadastrar(context):
    context.cadastro_page.clicar_botao_exibir_senha()
    time.sleep(1)

@then(u'a senha deve ser exibida')
def teste(context):
    senha_visivel = context.cadastro_page.checar_visibilidade_senha()
    assert senha_visivel == "text", f"Mensagem de erro:\nO alerta '{senha_visivel}'\n foi diferente do esperado text"
    time.sleep(1)

# end region