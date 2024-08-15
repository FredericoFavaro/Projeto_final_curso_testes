from behave import given, when, then
from features.pages.cadastro_page import CadastroPage
import time

# region cadastro de usuário
@given(u'que a página de cadastro seja acessada')
def step_impl(context):
    context.driver.get("https://www.udemy.com/join/signup-popup/?locale=pt_BR&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fjoin%2Flogin-popup%2F%3Flocale%3Den_US%26response_type%3Dhtml%26next%3Dhttps%253A%252F%252Fwww.udemy.com%252F")
    context.cadastro_page = CadastroPage(context.driver)

@when(u'o valor "{valor}" for inserido no campo Nome completo')
def inserir_texto_campo_nome(context, valor):
    context.cadastro_page.preencher_campo_nome(valor)
    time.sleep(1)

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

@then(u'o usuário é encaminhado para a tela de configuração do usuário')
def tela_usuario(context):
    meu_aprendizado = context.cadastro_page.obter_texto_meu_aprendizado()
    assert  meu_aprendizado == "Meu Aprendizado"
    time.sleep(1)
# endregion

# region Email inválido
@then(u'a mensagem "{msg}" deve ser exibida')
def testar_email(context, msg):
    texto_msg = context.cadastro_page.msg_email_invalido()
    assert texto_msg == msg, f"Mensagem de erro:\nO texto '{texto_msg}'\n foi diferente do esperado '{msg}'"

# endregion

# region Usuário já existe
@then(u'o aviso "{msg}" deve ser exibida')
def email_existe(context, msg):
    texto_msg = context.cadastro_page.msg_email_erro()
    assert texto_msg == msg, f"Mensagem de erro:\nO alerta '{texto_msg}'\n foi diferente do esperado '{msg}'"

# endregion

# region Senha visível
@when(u'o botão exibir senha for clicado')
def cadastrar(context):
    context.cadastro_page.clicar_botao_exibir_senha()
    time.sleep(1)

@then(u'a senha deve ser exibida')
def teste(context):
    senha_visivel = context.cadastro_page.obter_tipo_botao_senha()
    assert senha_visivel == "text", f"Mensagem de erro:\nO alerta '{senha_visivel}'\n foi diferente do esperado text"
    time.sleep(1)