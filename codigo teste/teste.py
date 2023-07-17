# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestesigaa():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testesigaa(self):
    self.driver.get("https://prex.env.sti.ufc.br/sigaa/logar.do?dispatch=logOff")
    self.driver.set_window_size(1105, 860)
    self.driver.find_element(By.NAME, "user.login").click()
    self.driver.find_element(By.NAME, "user.login").send_keys("emmanuellima")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(6) > tbody > tr:nth-child(1) > td").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td").click()
    self.driver.find_element(By.NAME, "user.senha").click()
    self.driver.find_element(By.NAME, "user.senha").send_keys("24082004")
    self.driver.find_element(By.NAME, "user.senha").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".discente .texto").click()
    self.driver.find_element(By.CSS_SELECTOR, "#cmAction-63 > .ThemeOfficeMenuItemText").click()
    self.driver.find_element(By.ID, "formBuscaAtividade:selectBuscaCodigo1").click()
    self.driver.find_element(By.ID, "formBuscaAtividade:buscaCodigoNew").click()
    self.driver.find_element(By.ID, "formBuscaAtividade:buscaCodigoNew").send_keys("2023.CS.0862")
    self.driver.find_element(By.ID, "formBuscaAtividade:btBuscar").click()
  def teste_text(self):
    elemento = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(4)")
    texto_elemento = elemento.text
    texto_desejado = "concluido"
    assert texto_desejado in texto_elemento, "A ação está concluída"

    
    
test = testesigaaaaa.py()
test.setup_method(None)
test.teste_sigaaaaaa()
test.teardown_method(None)
