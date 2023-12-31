# SI3-Selenium2

# Material de referencia para estudo
* [Video de configuração do pyenv, selenium](https://youtu.be/XUeu4ZzQNUI)

# Para ativar o ambiente deve-se
1. Usar um sistema operacional baseado em unix
2. Instalar o Firefox e o Chrome
3. Ser credenciado no projeto e fazer clone do projeto [SI3-Selenium2](https://github.com/Emmanuel-Sampaio/SI3-Selenium2/tree/main/codigo%20teste)
4. Instalar o pyenv: orientações abaixo
5. Criar um ambiente virtual no diretório do SI3-Selenium2
6. Instalar bibliotecas e fazer download dos drives do Firefox e Chrome


# Baixar o projeto em seu computador
- Comando clone: 
```
git clone git@github.com:Emmanuel-Sampaio/SI3-Selenium2.git SI3-Selenium''
```

# Programas para instalar
## pyenv
- Referência: https://cwi.com.br/blog/ferramentas-para-ambientes-virtuais-no-python/
### *Atualizar as bibliotecas do SO*
```
sudo apt-get update -y && sudo apt-get install -y
```
### *Instalando bibliotecas de dependências*
```
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev libpq-dev python3-pip
```
### *Rodando o instalador do pyenv*
```
sudo curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```
### *Ativando no terminal*
- Adicionar o código abaixo no final do arquivo ~/.bashrc: Ex: vim ~/.bashrc ou gedit ~/.bashrc
```
export PYENV_ROOT="$HOME/.pyenv" && \
export PATH="$PYENV_ROOT/bin:$PATH" && \
eval "$(pyenv init -)" && \
eval "$(pyenv virtualenv-init -)"
```

# Criar um ambiente virtual
- Baixando a versão mais recente e estável do python
```
pyenv install 3.11.4
```
- Criando um ambiente virtual com nome de selenium_si3 com a versão do python baixada
```
pyenv virtualenv 3.11.4 selenium_si3
```
- Ativando o ambiente do selenium_si3, toda vez antes de iniciar os trabalhos temos que ativar esse ambiente
```
 pyenv activate selenium_si3
```
- Atualizando a biblioteca do pip3
```
python3.11 -m pip install --upgrade pip
```

- Instalando a biblioteca do Selenium ( TODO: Quando o projeto estiver mais madulo, fechar as versões das bibliotecas)
```
pip3 install selenium
pip3 install webdriver-manager
pip3 install selenium-wire
```
- Criando o arquivo que lista as bibliotecas do pip3 e suas versões
```
pip3 freeze > requirements.txt
```

- Caso precise, comando para atualizar a biblioteca do selenium
```
pip3 install --upgrade selenium
```

# Lista das bibliotecas para rodar o selenium
## Primeiramente focaremos no Fiferox e Chrome
- [Link para baixar o WebDriver do Firefox](https://github.com/mozilla/geckodriver/releases)
- [Link para baixar o WebDriver do Chrome](https://sites.google.com/chromium.org/driver/?pli=1)
- [Link para baixar o WebDriver do Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- [Link para baixar o WebDriver do Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
