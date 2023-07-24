# https://cwi.com.br/blog/ferramentas-para-ambientes-virtuais-no-python/
# https://www.selenium.dev/pt-br/documentation/webdriver/interactions/alerts/
# pyenv install 3.11.4
# pyenv virtualenv 3.11.4 selenium_si3
# pyenv activate selenium_si3
# pip3 install selenium
# pip3 install pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

# CONSTANTES
BROWSER_DE_TESTE = "Firefox"
SITE_TESTE = "https://prex.env.sti.ufc.br/sigaa/logar.do"
SITE_TESTE = "https://si3.ufc.br/sigaa/verTelaLogin.do"
USUARIO = "antoniokassio"
SENHA = ""

class CreateDriver():
    def __init__(self, browser):
        if browser == BROWSER_DE_TESTE :
            self.driver = webdriver.Firefox()
        else :
            self.driver = webdriver.Chrome()
    def getDriver(self):
        return self.driver
    def close(self) :
        self.driver.close()

class LogarSigaa():
    def __init__(self,driver) :
        self.realizarLoginSigaa(driver)
        if ( not( self.verificarMultiplosVinculos( ) ) ):
            pass
        
        listaTodosModulosAtivos = driver.find_elements(By.CSS_SELECTOR, ".on")
        # self.listaTodosModulosAtivos = listaTodosModulosAtivos
        self.moduloExtensaoAtivo = self.verificarSeModuloExtensaoEstaAtivo(listaTodosModulosAtivos)

    def realizarLoginSigaa(self,driver):
        # Entrar no site
        driver.get(SITE_TESTE)

        # mapeamento dos elementos que vamos manipular no teste
        inputTextUsuario = driver.find_element(By.NAME, "user.login")
        inputTextSenha   = driver.find_element(By.NAME, "user.senha")
        btnEntrar        = driver.find_element(By.NAME, "entrar")

        # clicar e preencher o campo do usuario
        inputTextUsuario.click()
        inputTextUsuario.send_keys(USUARIO)
        # clicar e preencher o campo de senha
        inputTextSenha.click()
        inputTextSenha.send_keys(SENHA)
        # clicar no botao de logar
        btnEntrar.click()
        # print(retorno)

    def verificarMultiplosVinculos(self) :
        return False
    
    def verificarSeModuloExtensaoEstaAtivo(self, listaModulos):
        moduloExtensaoAtivo = False
        for modulo in listaModulos :
            if ( modulo.get_attribute("value") == 'extensao') :
                moduloExtensaoAtivo = True
        return moduloExtensaoAtivo;

        
class PlanoTeste(unittest.TestCase):
    def setUp(self):
        if "Firefox" == BROWSER_DE_TESTE :
            self.driver = webdriver.Firefox()
        else :
            self.driver = webdriver.Chrome()        
        self.logarSigaa = LogarSigaa(self.driver)

    def test_verifica_se_usuario_eh_servidor_prex(self):
        moduloExtensaoAtivo = self.logarSigaa.moduloExtensaoAtivo
        self.assertTrue( moduloExtensaoAtivo, "Verifica se módulo de extensão encontra-se habilitado")
        
    def tearDown(self):
        pass
        # self.driver.close()

# if __name__ == "__main__":
#     unittest.main()

## ########################################################### ##
##      RODAR INDIVIDUALMENTE AS CLASSES DEFINIDAS ACIMA 
## ########################################################### ##
# driver = CreateDriver(BROWSER_DE_TESTE).getDriver()
# logarSigaa = LogarSigaa(driver)
# driver.close()


