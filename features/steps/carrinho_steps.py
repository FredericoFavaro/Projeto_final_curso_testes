from behave import given, when, then
from features.pages.carrinho_page import CarrinhoPage
import time

# region add item

@given(u'que estou na página do produto')
def step_impl(context):
  context.driver.get("https://www.udemy.com/course/power-bi-completo-do-basico-ao-avancado/?couponCode=LETSLEARNNOWPP")
  context.carrinho_page = CarrinhoPage(context.driver)
  time.sleep(10)

@when(u'verifico se o texto do botão é "{texto_correto}"')
def verificar_texto(context, texto_correto):
  texto_obtido = context.carrinho_page.recuperar_texto_botao_add()
  assert texto_obtido == "Adicionar ao carrinho", f"O texto obtido '{texto_obtido}' foi diferente do texto esperado '{texto_correto}'"

@when(u'clicar no botão e adiciono o produto')
def clicar_botao(context):
  context.carrinho_page.clicar_botao_add()
  time.sleep(5)



# endregion