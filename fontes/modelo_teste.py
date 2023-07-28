# https://cwi.com.br/blog/ferramentas-para-ambientes-virtuais-no-python/
# https://www.selenium.dev/pt-br/documentation/webdriver/interactions/alerts/


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver import FirefoxOptions
#from seleniumwire import webdriver as seleniumwire_webdriver

from conexao import Conexao
from login_sigaa_selenium import LoginSigaaSelenium

import unittest
import time 

# CONSTANTES
BROWSER_DE_TESTE = "Firefox"
SITE_TESTE = "https://prex.env.sti.ufc.br/sigaa/"
#SITE_TESTE = "https://si3.ufc.br/sigaa/verTelaLogin.do"
USUARIO = "antoniokassio"
# SENHA = ""
SENHA = "1q2w3e4r"
TEMPO_ESPERA_POR_TELA = 2 # SEGUNDOS
PROXY = f'http://{USUARIO}:{SENHA}@proxy.ufc.br:8080'

        
class PlanoTeste(unittest.TestCase):
    def setUp(self):
        self.driver = Conexao().getDriver()

        self.logarSigaa = LoginSigaaSelenium(self.driver)

    def test_verifica_se_usuario_eh_servidor_prex(self):
        self.logarSigaa.realizaVerificacoes(self.driver)
        moduloExtensaoAtivo = self.logarSigaa.moduloExtensaoAtivo
        self.assertTrue( moduloExtensaoAtivo, "Verifica se módulo de extensão encontra-se habilitado")
        
    def tearDown(self):
        pass
        # self.driver.close()

## ########################################################### ##
##      RODAR TESTES
## ########################################################### ##
# if __name__ == "__main__":
#     unittest.main()

## ########################################################### ##
##      RODAR INDIVIDUALMENTE AS CLASSES
## ########################################################### ##
driver = Conexao().getDriver()
logarSigaa = LoginSigaaSelenium(driver)
logarSigaa.realizaVerificacoes(driver)
print(f'Modulo de extensão ativo? : {logarSigaa.moduloExtensaoAtivo}')
# driver.close()
## ########################################################### ##
##      RODAR INDIVIDUALMENTE AS CLASSES
## ########################################################### ##

