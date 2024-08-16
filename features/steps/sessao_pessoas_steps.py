from behave import given, when, then
from features.pages.sessao_pessoas_page import SessaoPessoasPage
import time

# region Testando o acesso ao perfil pesquisado
@given(u'que o usuário está na página inicial')
def step_impl(context):
    context.driver.get("https://br.linkedin.com")
    context.linkedin_page = SessaoPessoasPage(context.driver)
    time.sleep(10)

@when(u'clicar no menu Pessoas')
def step_impl(context):
    context.linkedin_page.clicar_botao_pessoas()
    time.sleep(5)

@when(u'digitar o nome')
def step_impl(context):
    context.linkedin_page.digitar_nome()
    time.sleep(2)

@when(u'digitar o sobrenome e clicar ENTER')
def step_impl(context):
    context.linkedin_page.digitar_sobrenome()
    time.sleep(5)

@when(u'clicar no resultado da busca')
def step_impl(context):
    context.linkedin_page.clicar_perfil()
    time.sleep(5)

@then(u'o modal de login/cadastro para ver o perfil completo aparece')
def step_impl(context):
    elemento_modal = context.linkedin_page.elemento_modal()
    assert elemento_modal
    time.sleep(5)
    
# endregion


# region Testando a pesquisa do menu Learning
@given(u'que o usuário está no início')
def step_impl(context):
    context.driver.get("https://br.linkedin.com")
    context.linkedin_page = SessaoPessoasPage(context.driver)
    time.sleep(10)

@when(u'clicar no menu Learning')
def step_impl(context):
    context.linkedin_page.clicar_botao_learning()
    time.sleep(5)

@when(u'digitar Power Bi e clicar ENTER')
def step_impl(context):
    context.linkedin_page.digitar_pesquisa()
    time.sleep(2)

@when(u'clicar no resultado')
def step_impl(context):
    context.linkedin_page.clicar_curso()
    time.sleep(5)

@when(u'clicar no botão PLAY')
def step_impl(context):
    context.linkedin_page.reproduzir_video()
    time.sleep(5)

@then(u'o vídeo é reproduzido')
def step_impl(context):
    elemento_video = context.linkedin_page.retornar_video()
    assert elemento_video
    time.sleep(40)
    
# endregion