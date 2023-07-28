import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSigaa():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_sigaa(self):
        self.driver.get("https://prex.env.sti.ufc.br/sigaa/logar.do?dispatch=logOff")
        self.driver.set_window_size(1105, 860)
        self.driver.find_element(By.NAME, "user.login").click()
        self.driver.find_element(By.NAME, "user.login").send_keys("emmanuellima")
        self.driver.find_element(By.NAME, "user.senha").send_keys("24082004")
        self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(6)").click()
        self.driver.find_element(By.NAME, "entrar").click()
        self.driver.find_element(By.CSS_SELECTOR, ".discente .texto").click()
        self.driver.find_element(By.CSS_SELECTOR, "#cmAction-62 > .ThemeOfficeMenuItemText").click()

# Instancia a classe de teste e chama o método de teste
test = TestSigaa()
test.setup_method(None)
test.test_sigaa()
test.teardown_method(None)
