from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver import FirefoxOptions
#from seleniumwire import webdriver as seleniumwire_webdriver


# CONSTANTES
BROWSER_DE_TESTE = "Firefox"
SITE_TESTE = "https://prex.env.sti.ufc.br/sigaa/"
#SITE_TESTE = "https://si3.ufc.br/sigaa/verTelaLogin.do"
USUARIO = "antoniokassio"
# SENHA = ""
SENHA = "1q2w3e4r"
TEMPO_ESPERA_POR_TELA = 2 # SEGUNDOS
PROXY = f'http://{USUARIO}:{SENHA}@proxy.ufc.br:8080'

class Conexao():
    def __init__(self):
        if "Firefox" == BROWSER_DE_TESTE :
            self.driver = webdriver.Firefox()
            # fireFoxOptions = FirefoxOptions()
            # fireFoxOptions.headless = True

            # seleniumwire_options = {
            #     'proxy': {
            #         'http': PROXY
            #         , 'https': PROXY
            #         #, 'no_proxy': 'localhost,127.0.0.1,dev_server:8080'
            #     }
            # }

            # self.driver = webdriver.Firefox(
            #                 options=fireFoxOptions,
            #                 seleniumwire_options=seleniumwire_options)
        else :
            self.driver = webdriver.Chrome()


    def getDriver(self):
        # tela de teste em fullscreen        
        return self.driver
    
    def setFullscreen(self):
        self.driver.fullscreen_window()

    # fecha a aba corrente
    def close(self) :
        self.driver.close()
    
    # fecha o browser
    def quit(self) :
        self.driver.quit()