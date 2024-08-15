from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class CarrinhoPage(BasePage):
  BOTAO_ADD = (By.CSS_SELECTOR, '[data-testid="add-to-cart-button"]')
  BOTAO_RMV = (By.CSS_SELECTOR, 'button.ud-btn.ud-btn-xsmall.ud-btn-ghost.ud-text-sm span.ud-btn-label')


  def clicar_botao_add(self):
    self.find_element(*self.BOTAO_ADD).click()

  def recuperar_texto_botao_add(self):
    return self.find_element(*self.BOTAO_ADD).text
  
  