from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time

class SessaoPessoasPage(BasePage):
    BOTAO_PESSOAS = (By.CSS_SELECTOR, "a[data-tracking-control-name='guest_homepage-basic_guest_nav_menu_people']")
    INPUT_NOME = (By.CSS_SELECTOR, "input[aria-label='Nome']")
    INPUT_SOBRENOME = (By.CSS_SELECTOR, "input[aria-label='Sobrenome']")
    CLICAR_PERFIL = (By.CSS_SELECTOR, "a[href='https://br.linkedin.com/in/ezequiel-leandro-jr?trk=people-guest_people_search-card']")
    MODAL = (By.CSS_SELECTOR, "div.modal__overlay")
    
    BOTAO_LEARNING = (By.CSS_SELECTOR, "a[data-tracking-control-name='guest_homepage-basic_guest_nav_menu_learning']")
    INPUT_LEARNING = (By.CSS_SELECTOR, 'input[aria-label="Pesquise competências, tópicos ou software"]')
    CLICAR_CURSO = (By.CSS_SELECTOR, 'a.base-card__full-link')
    VIDEO = (By.CSS_SELECTOR, 'span.top-card__preview-cta')
    ELEMENTO_VIDEO = (By.ID, 'vjs_video_3_html5_api')
    
    
    
    
    
    def clicar_botao_pessoas(self):
        botao_pessoas = self.find_element(*self.BOTAO_PESSOAS)
        botao_pessoas.click()
    
    def digitar_nome(self):
        input_nome = self.find_element(*self.INPUT_NOME)
        input_nome.send_keys("Ezequiel")
    
    def digitar_sobrenome(self):
        input_sobrenome = self.find_element(*self.INPUT_SOBRENOME)
        input_sobrenome.send_keys("Leandro Jr")
        input_sobrenome.send_keys(Keys.ENTER)
    
    def clicar_perfil(self):
        link_perfil = self.find_element(*self.CLICAR_PERFIL)
        link_perfil.click()
    
    def elemento_modal(self):
        modal = self.find_element(*self.MODAL)
        return modal
    
    #####################################################################
    
    def clicar_botao_learning(self):
        botao_learning = self.find_element(*self.BOTAO_LEARNING)
        botao_learning.click()
    
    def digitar_pesquisa(self):
        input_learning = self.find_element(*self.INPUT_LEARNING)
        input_learning.send_keys("Power BI")
        input_learning.send_keys(Keys.ENTER)
    
    def clicar_curso(self):
        link_curso = self.find_element(*self.CLICAR_CURSO)
        link_curso.click()
    
    def reproduzir_video(self):
        video = self.find_element(*self.VIDEO)
        video.click()
    
    def retornar_video(self):
        elemento_video = self.find_element(*self.ELEMENTO_VIDEO)
        return elemento_video
        
    
    #def recuperar_texto_cadastro(self):
        #botao_cadastro = self.get_element_text(self.find_element(*self.BOTAO_CADASTRO))
        #return botao_cadastro
    
    
    #def escrever_texto_campo_pesquisa(self):
     #   formulario = self.find_element(*self.FORMULARIO)
      #  campo_pesquisa = formulario.find_element(By.CSS_SELECTOR, "input.ud-text-input.ud-text-input-small.ud-text-sm.ud-search-form-autocomplete-input.js-header-search-field")
       # campo_pesquisa.send_keys('gherkin')
        #campo_pesquisa.send_keys(Keys.ENTER)
