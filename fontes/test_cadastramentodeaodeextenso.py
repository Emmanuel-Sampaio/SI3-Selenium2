# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCadastramentodeaodeextenso():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cadastramentodeaodeextenso(self):
    self.driver.find_element(By.NAME, "user.login").click()
    self.driver.find_element(By.NAME, "user.login").send_keys("mm")
    self.driver.find_element(By.NAME, "user.login").send_keys(Keys.DOWN)
    self.driver.find_element(By.NAME, "user.login").send_keys(Keys.TAB)
    self.driver.find_element(By.NAME, "user.senha").send_keys("a")
    self.driver.find_element(By.NAME, "entrar").click()
    self.driver.find_element(By.CSS_SELECTOR, ".docente .texto").click()
    self.driver.find_element(By.CSS_SELECTOR, "#cmAction-47 > .ThemeOfficeMenuItemText").click()
    self.driver.find_element(By.CSS_SELECTOR, ".descricaoOperacao:nth-child(1)").click()
    self.driver.find_element(By.NAME, "formAtividade:j_id_jsp_1355849745_264").click()
    self.driver.find_element(By.ID, "formAtividade:btProposta").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(2) > img").click()
    self.driver.find_element(By.LINK_TEXT, "Evento").click()
    self.driver.find_element(By.ID, "form:titulo").click()
    self.driver.find_element(By.ID, "form:titulo").send_keys("Ciencia de dados no mercado de trabalho")
    self.driver.find_element(By.ID, "form:anoAtividade").click()
    self.driver.find_element(By.ID, "form:anoAtividade").send_keys("2023")
    self.driver.find_element(By.ID, "form:dataInicio").click()
    self.driver.find_element(By.ID, "form:dataInicio").send_keys("24/08/2023")
    self.driver.find_element(By.ID, "form:dataFim").click()
    self.driver.find_element(By.ID, "form:dataFim").send_keys("26/08/2023")
    self.driver.find_element(By.ID, "form:tipoRegiao").click()
    self.driver.find_element(By.CSS_SELECTOR, "#form\\3AtipoRegiao > option:nth-child(3)").click()
    self.driver.find_element(By.ID, "form:areaTematicaPrincipal").click()
    dropdown = self.driver.find_element(By.ID, "form:areaTematicaPrincipal")
    dropdown.find_element(By.XPATH, "//option[. = 'Tecnologia e Produção']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#form\\3A areaTematicaPrincipal > option:nth-child(9)").click()
    self.driver.find_element(By.ID, "form:areaTematicaSecundaria").click()
    dropdown = self.driver.find_element(By.ID, "form:areaTematicaSecundaria")
    dropdown.find_element(By.XPATH, "//option[. = 'Trabalho']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#form\\3A areaTematicaSecundaria > option:nth-child(10)").click()
    self.driver.find_element(By.ID, "form:linhaDeExtensao").click()
    dropdown = self.driver.find_element(By.ID, "form:linhaDeExtensao")
    dropdown.find_element(By.XPATH, "//option[. = 'Tecnologia da informação']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#form\\3AlinhaDeExtensao > option:nth-child(47)").click()
    self.driver.find_element(By.ID, "form:publicoAlvo").click()
    self.driver.find_element(By.ID, "form:publicoAlvo").send_keys("alunos do curso de engenharia de computação")
    self.driver.find_element(By.ID, "form:siteAcao").click()
    self.driver.find_element(By.ID, "form:palavrasChave").click()
    self.driver.find_element(By.ID, "form:palavrasChave").send_keys("dados, engenharia de computação, estatística")
    self.driver.find_element(By.ID, "form:telefoneAcao").click()
    self.driver.find_element(By.ID, "form:telefoneAcao").send_keys("40028922")
    self.driver.find_element(By.ID, "form:emailAcao").click()
    self.driver.find_element(By.ID, "form:emailAcao").send_keys("engcomp@ufc.br")
    self.driver.find_element(By.ID, "form:publicoEstimado").click()
    self.driver.find_element(By.ID, "form:publicoEstimado").send_keys("100")
    self.driver.find_element(By.ID, "form:tipoLocalRealizacao").click()
    dropdown = self.driver.find_element(By.ID, "form:tipoLocalRealizacao")
    dropdown.find_element(By.XPATH, "//option[. = 'Local Principal']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#form\\3AtipoLocalRealizacao > option:nth-child(2)").click()
    self.driver.find_element(By.ID, "form:espacoRealizacaoAdicional").click()
    self.driver.find_element(By.ID, "form:espacoRealizacaoAdicional").send_keys("Departamento de engenharia de teleinformática")
    self.driver.find_element(By.ID, "form:localButton").click()
    self.driver.find_element(By.ID, "form:btAvancar").click()
    self.driver.find_element(By.ID, "form:vinculoProgramaExtensao:1").click()
    self.driver.find_element(By.ID, "form:palavrasChave").click()
    self.driver.find_element(By.ID, "form:palavrasChave").send_keys("dados; engenharia de computação; estatística")
    self.driver.find_element(By.ID, "form:btAvancar").click()
    self.driver.find_element(By.ID, "atividades:btAvancar").click()
    self.driver.switch_to.frame(4)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    self.driver.switch_to.default_content()
    element = self.driver.find_element(By.CSS_SELECTOR, "#mceu_344 .mce-ico")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.switch_to.frame(4)
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>dkdskdlskddkslçkçlskdçlklsdklks<br data-mce-bogus=\"1\"></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "elgen-10").click()
    self.driver.switch_to.frame(3)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>kldksldklsdklçkdlçskdlksadlkdlçask<br data-mce-bogus=\"1\"></p>'}", element)
    self.driver.switch_to.default_content()
    element = self.driver.find_element(By.ID, "elgen-13")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "elgen-14")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "elgen-13").click()
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>dçsdç~sldçlsçdlçdçaldldç~sls<br data-mce-bogus=\"1\"></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "elgen-18").click()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>kdskdlçsakdlklçdkçlkdskadlkslçdsa<br data-mce-bogus=\"1\"></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "elgen-21").click()
    self.driver.find_element(By.ID, "mceu_73-body").click()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>dsklskdlkdslkdsldklçdkçlsaldçksd<br data-mce-bogus=\"1\"></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td").click()
    self.driver.find_element(By.ID, "cargaHoraria").click()
    self.driver.find_element(By.ID, "modalidadeEducacao").click()
    dropdown = self.driver.find_element(By.ID, "modalidadeEducacao")
    dropdown.find_element(By.XPATH, "//option[. = 'Presencial']").click()
    assert self.driver.switch_to.alert.text == "Cursos com carga horária inferior a 20h e eventos com carga horária inferior a 8h não darão direito a certificado emitido pela Prex de acordo com a Portaria nº 01/PREx, de 7 de janeiro de 2016."
    self.driver.find_element(By.ID, "tipoEvento").click()
    dropdown = self.driver.find_element(By.ID, "tipoEvento")
    dropdown.find_element(By.XPATH, "//option[. = 'CONGRESSO']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#tipoEvento > option:nth-child(3)").click()
    self.driver.find_element(By.ID, "j_id_jsp_1384896771_33:1").click()
    self.driver.find_element(By.ID, "cargaHoraria").click()
    self.driver.find_element(By.ID, "cargaHoraria").send_keys("16")
    self.driver.find_element(By.ID, "numeroVagas").click()
    self.driver.find_element(By.ID, "numeroVagas").send_keys("100")
    self.driver.find_element(By.LINK_TEXT, "Gravar e Avançar >>").click()
    self.driver.find_element(By.ID, "frmobjetivos:objetivo").click()
    self.driver.find_element(By.ID, "frmobjetivos:objetivo").send_keys("hfdshhjfhdjhjfdjjfhdsjfhdf")
    self.driver.find_element(By.ID, "frmobjetivos:quantitativos").click()
    self.driver.find_element(By.ID, "frmobjetivos:quantitativos").send_keys("sjskahfkashfhasfhsahkfhsalkf")
    self.driver.find_element(By.ID, "frmobjetivos:qualitativos").click()
    self.driver.find_element(By.ID, "frmobjetivos:qualitativos").send_keys("sjfjfksljklfjskjfklsakfjaslkfs")
    self.driver.find_element(By.ID, "frmobjetivos:atividades").click()
    self.driver.find_element(By.ID, "frmobjetivos:atividades").send_keys("saklfskalfklfçskalçksafllçfklaçkfas")
    self.driver.find_element(By.ID, "frmobjetivos:dataInicio").click()
    self.driver.find_element(By.ID, "frmobjetivos:dataInicio").send_keys("24/08/2023")
    self.driver.find_element(By.ID, "frmobjetivos:dataFim").click()
    self.driver.find_element(By.ID, "frmobjetivos:dataFim").send_keys("26/08/2023")
    self.driver.find_element(By.ID, "frmobjetivos:j_id_jsp_720929453_233").click()
    self.driver.find_element(By.ID, "frmobjetivos:atividades").click()
    self.driver.find_element(By.ID, "frmobjetivos:avancar").click()
    self.driver.find_element(By.ID, "frmobjetivos:addObjetivos").click()
    self.driver.find_element(By.ID, "frmobjetivos:avancar").click()
    self.driver.find_element(By.ID, "equipe:categoriaMembro").click()
    dropdown = self.driver.find_element(By.ID, "equipe:categoriaMembro")
    dropdown.find_element(By.XPATH, "//option[. = 'Docente']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "equipe:nomeDocente").click()
    self.driver.find_element(By.ID, "equipe:nomeDocente").send_keys("charles ")
    self.driver.find_element(By.CSS_SELECTOR, "#\\31 3103 div:nth-child(2)").click()
    self.driver.find_element(By.ID, "equipe:chDedicadaDocente").click()
    self.driver.find_element(By.ID, "equipe:chDedicadaDocente").send_keys("16")
    self.driver.find_element(By.LINK_TEXT, "Adicionar Membro").click()
    self.driver.find_element(By.ID, "equipe:funcaoMembroEquipeDocente").click()
    dropdown = self.driver.find_element(By.ID, "equipe:funcaoMembroEquipeDocente")
    dropdown.find_element(By.XPATH, "//option[. = 'COLABORADOR']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#equipe\\3A funcaoMembroEquipeDocente > option:nth-child(3)").click()
    self.driver.find_element(By.LINK_TEXT, "Adicionar Membro").click()
    dropdown = self.driver.find_element(By.ID, "equipe:categoriaMembro")
    dropdown.find_element(By.XPATH, "//option[. = 'Docente']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "equipe:nomeDocente").click()
    self.driver.find_element(By.ID, "equipe:funcaoMembroEquipeDocente").click()
    self.driver.find_element(By.ID, "equipe:funcaoMembroEquipeDocente").click()
    self.driver.find_element(By.ID, "equipe:nomeDocente").click()
    self.driver.find_element(By.ID, "equipe:nomeDocente").send_keys("jarbas ")
    self.driver.find_element(By.CSS_SELECTOR, "#\\31 3677 div:nth-child(2)").click()
    self.driver.find_element(By.ID, "equipe:funcaoMembroEquipeDocente").click()
    self.driver.find_element(By.ID, "equipe:funcaoMembroEquipeDocente").click()
    self.driver.find_element(By.ID, "equipe:funcaoMembroEquipeDocente").click()
    dropdown = self.driver.find_element(By.ID, "equipe:funcaoMembroEquipeDocente")
    dropdown.find_element(By.XPATH, "//option[. = 'COORDENADOR']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#equipe\\3A funcaoMembroEquipeDocente > option:nth-child(5)").click()
    self.driver.find_element(By.ID, "equipe:nomeDocente").click()
    self.driver.find_element(By.ID, "equipe:nomeDocente").send_keys("michela ")
    self.driver.find_element(By.ID, "equipe:nomeDocente").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Adicionar Membro").click()
    self.driver.find_element(By.ID, "equipe:chDedicadaDocente").click()
    self.driver.find_element(By.ID, "equipe:chDedicadaDocente").send_keys("16")
    self.driver.find_element(By.CSS_SELECTOR, ".formulario:nth-child(5) tr:nth-child(4) > td").click()
    self.driver.find_element(By.LINK_TEXT, "Adicionar Membro").click()
    self.driver.find_element(By.ID, "equipe:btn_irProximoServidores").click()
    self.driver.find_element(By.CSS_SELECTOR, "tfoot:nth-child(1) td").click()
    self.driver.find_element(By.ID, "formLista:avancar").click()
    self.driver.find_element(By.ID, "form:avancar").click()
    self.driver.find_element(By.ID, "formAnexosAtividade:descricao").click()
    self.driver.find_element(By.ID, "formAnexosAtividade:descricao").send_keys("jfdjjdfjddjfkljfdklsj")
    self.driver.find_element(By.ID, "formAnexosAtividade:uFile").click()
    self.driver.find_element(By.ID, "formAnexosAtividade:uFile").send_keys("C:\\fakepath\\Captura de tela de 2023-06-12 12-37-47.png")
    self.driver.find_element(By.ID, "formAnexosAtividade:btAnexarArqui").click()
    self.driver.find_element(By.LINK_TEXT, "Gravar e Avançar >>").click()
    self.driver.find_element(By.ID, "formAnexosAtividade:descricao").click()
    self.driver.find_element(By.ID, "formAnexosAtividade:descricao").send_keys("jkjxkjkjkdkljdlkksjdk")
    self.driver.find_element(By.LINK_TEXT, "Gravar e Avançar >>").click()
    self.driver.find_element(By.ID, "j_id_jsp_320856913_1:confirmaSenha").click()
    self.driver.find_element(By.ID, "j_id_jsp_320856913_1:confirmaSenha").send_keys("a")
    self.driver.find_element(By.ID, "j_id_jsp_320856913_1:submeterPREX").click()
    self.driver.get("https://prex.env.sti.ufc.br/sigaa/verTelaLogin.do")
  
