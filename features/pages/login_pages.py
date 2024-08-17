import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.elementos import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = URL_LINKDIN
    
    def __init__(self, browser: webdriver):
        self.browser = browser

    def open(self):
        # Abre a página de login
        self.browser.get(self.URL)

    def limpar_campos(self, limpo):
        self.browser.find_element(By.ID, limpo).clear()

    def enter_login(self, campo_page_html, dados_do_usuario ): # o primeiro valor é o elemento html e o segndo é a informação do usuario
        self.limpar_campos(campo_page_html)       
        username_field = self.browser.find_element(By.ID, campo_page_html)
        username_field.send_keys(dados_do_usuario) # recebe o email do arquivo em elementos
        time.sleep(5)

    def text_capturado(self):
        message_text = WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, TXT_CAPTURADO))    )
        return message_text.text                
        
    def click_btn(self, btn):
        # Localiza o botão de login pelo ID usando By e clica nele
        login_btn = self.browser.find_element(By.XPATH, btn)
        login_btn.click()
        time.sleep(20)

    def logout(self, btn):
        self.click_btn(btn)
        time.sleep(5)
        btn_sair = self.browser.get(URL_LOGOUT)    
        time.sleep(5)

