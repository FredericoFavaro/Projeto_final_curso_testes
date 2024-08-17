from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class CadastroPage(BasePage):
    BOTAO_CLICK_ME = (By.CSS_SELECTOR, '#buttonSimple')
    CAMPO_EMAIL = (By.CSS_SELECTOR, '#email-or-phone')
    CAMPO_SENHA = (By.CSS_SELECTOR, '#password')
    CAMPO_NOME = (By.CSS_SELECTOR, '#first-name')
    CAMPO_SOBRENOME = (By.CSS_SELECTOR, '#last-name')
    BOTAO_CADASTRAR = (By.CSS_SELECTOR, "#join-form-submit")
    TEXTO_SEGURANCA = (By.XPATH, '//h2[text()="Verificação de segurança"]')
    BOTAO_SENHA_VISIVEL = (By.CSS_SELECTOR, '.join-form__show-password-btn')

    

    def preencher_campo_email(self, valor):
        campo_nome = self.find_element(*self.CAMPO_EMAIL)
        campo_nome.send_keys(valor)

    def preencher_campo_senha(self, valor):
        campo_nome = self.find_element(*self.CAMPO_SENHA)
        campo_nome.send_keys(valor)
    
    def preencher_campo_nome(self, valor):
        campo_nome = self.find_element(*self.CAMPO_NOME)
        campo_nome.send_keys(valor)
    
    def preencher_campo_sobrenome(self, valor):
        campo_nome = self.find_element(*self.CAMPO_SOBRENOME)
        campo_nome.send_keys(valor)

    def clicar_botao_cadastrese(self):
        self.find_element(*self.BOTAO_CADASTRAR).click()
    
    def checar_texto_seguranca(self):
        return self.find_element(*self.TEXTO_SEGURANCA).text
    
    def clicar_botao_exibir_senha(self):
        self.find_element(*self.BOTAO_SENHA_VISIVEL).click()

    def checar_visibilidade_senha(self):
        campo_senha = self.find_element(*self.CAMPO_SENHA)
        return campo_senha.get_attribute("type")