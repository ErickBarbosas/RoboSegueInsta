from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



links=[]
valor=[]

#perfis= str(input('Digite os Links do Perfil (Separados Por ;):\n'))

# links=perfis.split()



i = 0
#while True:
    
driver = webdriver.Chrome(executable_path="C:\Projetos\RoboSeguiInsta\webdriver\chromedriver.exe")
driver.get('https://www.instagram.com/amante_dos_baixos/')
sleep(3)

#Clicando no botao de login   
driver.find_element_by_css_selector("button[type='button']").click()
#Digitando Login e senha 
driver.find_element_by_css_selector("input[name='username']").send_keys('hermanos_acessorios')
driver.find_element_by_css_selector("input[name='password']").send_keys('Quiksilver2@')
#Clicando no botao logar
driver.find_element_by_css_selector("button[type='submit']").click()
sleep(5)
#Clicando para nao salvar informacoes no navegador
driver.find_element_by_xpath("//button[text()='Agora não']").click()
#Clicando no botao de seguidores no perfil
driver.find_element_by_xpath("//a[text()=' seguidores']").click()

#Clicando em Seguir

try:
    while True:
        sleep(3)
        valor= driver.find_element_by_xpath("//button[text()='Seguir']").click()
       

except:
    print("erro")

