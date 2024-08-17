import time
from behave import given, when, then
from pages.login_pages import LoginPage
from features.elementos import *
from selenium.webdriver.common.by import By


# region TestLogin
@given(u'que o usuário está na página de login')
def step_impl(context):
    context.page = LoginPage(context.browser)
    context.page.open()

@when(u'é inserido insere email e senha corretos')
def step_impl(context):
    context.page.enter_login(CAMPO_EMAIL, EMAIL)  # o 1º valor,elemento html e o 2º é a informação do usuario    
    context.page.enter_login(CAMPO_SENHA, SENHA)  # o 1º valor,elemento html e o 2º é a informação do usuario
        

@then(u'clica no botão de login e será redirecionado para a página inicial')
def step_impl(context):
    context.page.click_btn(BTN_LOGIN)
    time.sleep(20)  # Espera para carregar a página


# endregion 
# region TestErroLogin
@given(u'dado que o usuário está na página de login')
def step_impl(context):
    context.page = LoginPage(context.browser)
    context.page.open()

@when(u'Quando ele insere um email')
def step_impl(context):
    context.page.enter_login(CAMPO_EMAIL, EMAIL)# o 1º valor, elemento html e o 2º é a informação do usuario

@when(u'clica no botão login')
def step_impl(context):
    context.page.click_btn(BTN_LOGIN)

@then(u'a mensagem "{texto}" deverá ser exibida')
def step_impl(context, texto):
    error_message = context.page.text_capturado() 
    assert texto == error_message, f"Mensagem de erro: \no texto desejado '{texto}'\nfoi diferente do texto obtido '{error_message}'"


# endregion
# region TestLogout
@given(u'o usuário está na página de login')
def step_impl(context):
    context.page = LoginPage(context.browser)
    context.page.open()

@when(u'Quando ele insere email e senha corretos')
def step_impl(context):
    context.page.enter_login(CAMPO_EMAIL, EMAIL)# o 1º valor,elemento html e o 2º é a informação do usuario
    context.page.enter_login(CAMPO_SENHA, SENHA)# o 1º valor,elemento html e o 2º é a informação do usuario

@when(u'clica no botão de login e será redirecionado para a página inicial')
def step_impl(context):
    context.page.click_btn(BTN_LOGIN)

@then(u'depois faz o logout')
def step_impl(context):
    context.page.logout(IMG_MENU)
