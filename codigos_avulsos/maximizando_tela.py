from selenium import webdriver
driver = webdriver.Firefox()
#Open apress webpage
driver.get('https://apress.com')
#Maximise Window
driver.maximize_window()
print("Browser is maximised")