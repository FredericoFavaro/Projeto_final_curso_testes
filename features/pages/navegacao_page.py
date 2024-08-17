from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


class NavegacaoPage(BasePage):
  LINK_ARTIGO = (By.XPATH, "/html/body/nav/ul/li[1]/a")
  X_AVISO = (By.XPATH, "/html/body/div[2]/div/div/section/button")
  MODAL_IDIOMA = (By.XPATH,"/html/body/main/section[1]/div/div[1]/div[1]/button" )
  SELECT_LANG = (By.ID, "select-language-dropdown")
  BOTAO_SAVE = (By.ID, "article-translation-save-cta-btn")
  LINK_VAGAS = (By.XPATH, "/html/body/nav/ul/li[4]/a" )
  ESPACO_VAGA = (By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input")
  OPCAO_VAGA = (By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[1]/div/ul/li[6]")
  ESPACO_LOCAL = (By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[2]/input")
  OPCAO_LOCAL = (By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[2]/div/ul/li[1]")
  APAGAR_LOCAL = (By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[2]/button")
  BOTAO_PESQUISA = (By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/button")
  BOTAO_REMOTO = (By.XPATH, "/html/body/div[1]/section[1]/div/div/div/form/ul/li[6]/div/div/button")
  CHECK_REMOTO = (By.XPATH, "/html/body/div[1]/section[1]/div/div/div/form/ul/li[6]/div/div/div/div/div/div[2]/input")
  BOTAO_CONFIRMAR_REMOTO = (By.XPATH, "/html/body/div[1]/section[1]/div/div/div/form/ul/li[6]/div/div/div/button")
  BOTAO_LOCAL = (By.XPATH, "/html/body/div[1]/section[1]/div/div/div/form[1]/ul/li[6]/div/div/button")
  CHECK_LOCAL = (By.XPATH, "/html/body/div[1]/section[1]/div/div/div/form[1]/ul/li[6]/div/div/div/div/div/div[4]/input")
  BOTAO_CONFIRMAR_LOCAL = (By.XPATH, "/html/body/div[1]/section[1]/div/div/div/form[1]/ul/li[6]/div/div/div/button")

  def clicar_artigo(self):
    self.find_element(*self.LINK_ARTIGO).click()

  def fechar_x(self):
    self.find_element(*self.X_AVISO).click()

  def clicar_modal_idioma(self):
    self.find_element(*self.MODAL_IDIOMA).click()

  def escolher_linguagem(self, valor):
    opcao = Select(self.find_element(*self.SELECT_LANG))
    opcao.select_by_value(valor)

  def exibir_pagina_alemao(self):
    self.find_element(*self.BOTAO_SAVE).click()

  def clicar_vagas(self):
    self.find_element(*self.LINK_VAGAS).click()

  def preencher_campo_vaga(self, valor):
    campo_vaga = self.find_element(*self.ESPACO_VAGA)
    campo_vaga.send_keys(valor)
    
    

  def clicar_opcao_vaga(self):
    self.find_element(*self.OPCAO_VAGA).click()

  def apaga_local(self):
    self.find_element(*self.APAGAR_LOCAL).click()
    time.sleep(1)
  

  def preencher_campo_local(self, valor):    
    campo_vaga = self.find_element(*self.ESPACO_LOCAL)
    campo_vaga.send_keys(valor)
    time.sleep(2)
    

  def clicar_opcao_local(self):
    self.find_element(*self.OPCAO_LOCAL).click()
    time.sleep(2)


  def escolher_remoto_local(self):
    self.find_element(*self.BOTAO_REMOTO).click()
    time.sleep(1)
    self.find_element(*self.CHECK_REMOTO).click()
    time.sleep(1)
    self.find_element(*self.BOTAO_CONFIRMAR_REMOTO).click()
    time.sleep(3)
    self.find_element(*self.BOTAO_LOCAL).click()
    time.sleep(1)
    self.find_element(*self.CHECK_REMOTO).click()
    time.sleep(2)
    self.find_element(*self.BOTAO_CONFIRMAR_LOCAL).click()
    time.sleep(10)





  