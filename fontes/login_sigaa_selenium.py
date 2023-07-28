
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import parametros # parametros de configuração
import time 

class LoginSigaaSelenium():
    def __init__(self,driver) :        
        self.moduloExtensaoAtivo = False
        # Login no SIGAA
        self.realizarLoginSigaa(driver)
        
        # Recupera informações da tela de Módulos
        if ( not( self.verificaTelaDeMultiplosVinculos( driver ) ) ):
            pass
      
    def realizaVerificacoes(self, driver) :
        time.sleep(parametros.TEMPO_ESPERA_POR_TELA) 
        # Verifica se o módulo de extensão encontra-se ativo
        self.moduloExtensaoAtivo = self.verificaSeModuloExtensaoEstaAtivo(driver)

    def realizarLoginSigaa(self,driver):
        # Entrar no site
        driver.get(parametros.SITE_TESTE)

        # mapeamento dos elementos que vamos manipular no teste
        inputTextUsuario = driver.find_element(By.NAME, "user.login")
        inputTextSenha   = driver.find_element(By.NAME, "user.senha")
        btnEntrar        = driver.find_element(By.NAME, "entrar")

        # clicar e preencher o campo do usuario
        inputTextUsuario.click()
        inputTextUsuario.send_keys(parametros.USUARIO)
        # clicar e preencher o campo de senha
        inputTextSenha.click()
        inputTextSenha.send_keys(parametros.SENHA)
        # clicar no botao de logar
        btnEntrar.click()

    def verificaTelaDeMultiplosVinculos(self, driver) :
        return False
    
    def verificaSeModuloExtensaoEstaAtivo(self,driver):
        # lista de todos os módulos ativos
        listaTodosModulosAtivos = driver.find_elements(By.CSS_SELECTOR, ".on")

        moduloExtensaoAtivo = False
        for modulo in listaTodosModulosAtivos :
            if ( 'Extensão' in modulo.text) :
                moduloExtensaoAtivo = True
        return moduloExtensaoAtivo;