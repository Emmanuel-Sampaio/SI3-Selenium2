from selenium import webdriver
driver = webdriver.Firefox()
#Open apress webpage
driver.get('https://apress.com')
#Get Window Position
window_pos= driver.get_window_position()
print(window_pos)