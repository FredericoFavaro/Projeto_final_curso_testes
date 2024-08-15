from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class CadastroPage(BasePage):
    CAMPO_NOME = (By.CSS_SELECTOR, '#form-group--1')
    CAMPO_EMAIL = (By.CSS_SELECTOR, '#form-group--3')
    CAMPO_SENHA = (By.CSS_SELECTOR, '#form-group--5')
    BOTAO_CADASTRESE = (By.CSS_SELECTOR, 'button.ud-btn.ud-btn-large.ud-btn-brand.helpers--auth-submit-button--W3Tqk')
    CHECK_CADASTRO = (By.CSS_SELECTOR, 'span.ud-text-sm.desktop-header-module--dropdown-button-text--Sq73l')
    BOTAO_LOGIN = (By.CSS_SELECTOR, 'a[data-purpose="header-login"].ud-btn.ud-btn-medium.ud-btn-secondary')
    TEXTO_TITULO = (By.XPATH, '//title')
    MSG_EMAIL_INVALIDO = (By.CSS_SELECTOR, '#form-group-note--4')
    MSG_EMAIL_ERRO = (By.CSS_SELECTOR, 'div[data-purpose="safely-set-inner-html:auth:error"]')
    BOTAO_SENHA_VISIVEL = (By.CSS_SELECTOR, 'button.password-form-group--icon--tZsyr')
    CHECAR_SENHA_VISIVEL = (By.CSS_SELECTOR, '#form-group--5 > type')


    def preencher_campo_nome(self, valor):
        campo_nome = self.find_element(*self.CAMPO_NOME)
        campo_nome.send_keys(valor)

    def preencher_campo_email(self, valor):
        campo_nome = self.find_element(*self.CAMPO_EMAIL)
        campo_nome.send_keys(valor)

    def preencher_campo_senha(self, valor):
        campo_nome = self.find_element(*self.CAMPO_SENHA)
        campo_nome.send_keys(valor)

    def clicar_botao_cadastrese(self):
        self.find_element(*self.BOTAO_CADASTRESE).click()
    
    def obter_texto_meu_aprendizado(self):
        return self.find_element(*self.CHECK_CADASTRO).text
    
    def botao_login_nao_existe(self):
        return not self.find_element(*self.BOTAO_LOGIN).is_displayed()
    
    def pegar_titulo(self):
        return self.find_element(*self.TEXTO_TITULO)

    def msg_email_invalido(self):
        return self.find_element(*self.MSG_EMAIL_INVALIDO).text

    def msg_email_erro(self):
        return self.find_element(*self.MSG_EMAIL_ERRO).text
    
    def clicar_botao_exibir_senha(self):
        self.find_element(*self.BOTAO_SENHA_VISIVEL).click()

    def obter_tipo_botao_senha(self):
        campo_senha = self.find_element(*self.CAMPO_SENHA)
        return campo_senha.get_attribute("type")