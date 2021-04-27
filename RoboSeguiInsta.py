from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

links=[]
valor=[]

print('**************************************')
print('*****  Robo Ganhe Seguidores :) ******')
print('**************************************')
print('               MENU                   ')
print('\nSelecione uma opção')
print('1- Seguir Seguidores de um Perfil')
print('2- Deixar De Seguir')

opcao = str(input('R: '))

if opcao =='1':

    perfis= str(input('Digite os Links do Perfil (Separados Por ;):\n'))
    seguir=int(input('Digite Quantos Perfil Você que Seguir\n'))

    links=perfis.split()

    for i in range(len(links)):
            driver = webdriver.Chrome(executable_path="C:\Projetos\RoboSeguiInsta\webdriver\chromedriver.exe")
            driver.get(links[i])
        
            #Clicando no botao de login   
            driver.find_element_by_css_selector("button[type='button']").click()
            #Digitando Login e senha 
            driver.find_element_by_css_selector("input[name='username']").send_keys('')
            driver.find_element_by_css_selector("input[name='password']").send_keys('')
            #Clicando no botao logar
            driver.find_element_by_css_selector("button[type='submit']").click()
            sleep(5)
            #Clicando para nao salvar informacoes no navegador
            driver.find_element_by_xpath("//button[text()='Agora não']").click()

            #Clicando no botao de seguidores no perfil
            driver.find_element_by_xpath("//a[text()=' seguidores']").click()

            try:
               for j in seguir:
                    for i in range(5):
                        sleep(3)
                        #Clicando em Seguir
                        valor= driver.find_element_by_xpath("//button[text()='Seguir']").click()
                    sleep(60)

            except:
                print("erro")

elif opcao == '2':

    perfis= str(input('Digite os Links do Perfil (Separados Por ;):\n'))
    seguir=int(input('Digite Quantos Perfil Deseja Deixar de Seguir\n'))
    links=perfis.split()

    for i in range(len(links)):
        driver = webdriver.Chrome(executable_path="C:\Projetos\RoboSeguiInsta\webdriver\chromedriver.exe")
        driver.get(links[i])
        
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
        driver.find_element_by_xpath("//a[text()=' seguindo']").click()

        #Deixando de segui Usuario
        for j in range(seguir):
            sleep(3)
            driver.find_element_by_xpath("//button[text()='Seguindo']").click()
            sleep(2)
            driver.find_element_by_xpath("//button[text()='Deixar de seguir']").click()
                
elif opcao != '1' or opcao != '2':
    print('Valor Invalido')
