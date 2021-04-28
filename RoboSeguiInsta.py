from selenium import webdriver
import os
from time import sleep

links=[]
valor=[]

os.system('cls') or None #Limpa Tela
print('**************************************')
print('*****  Robo Ganhe Seguidores :) ******')
print('**************************************')
print('               MENU                   ')
print('\nSelecione uma opção')
print('1- Seguir Seguidores de um Perfil')
print('2- Deixar De Seguir')

opcao = str(input('R: '))

if opcao =='1':
  
    os.system('cls') or None #Limpa Tela 

    #Digite o link da pagina que deseja seguir os seguidores
    perfis= str(input('Digite os Links do Perfil (Separados Por ;):\n'))
    #Quantidades de perfil que deseja seguir
    seguir=int(input('Digite Quantos Perfil Você que Seguir\n'))
   
    #login do Instagram
    login=str(input('Digite seu Login: '))
    #Senha Do perfil
    senha=str(input('Digite a Senha do Perfil: '))
    links=perfis.split()

    for i in range(len(links)):
           
            os.system('cls') or None #Limpa Tela
            print('Iniciando Processo...')
            #WebDriver
            driver = webdriver.Chrome(executable_path="C:\Projetos\RoboSeguiInsta\webdriver\chromedriver.exe")
            #Abrindo navegados e entrando no link
            driver.get(links[i])
            sleep(3)

            #Clicando no botao de login
            driver.find_element_by_css_selector("button[type='button']").click()
            sleep(1)
            #Digitando Login e senha
            driver.find_element_by_css_selector("input[name='username']").send_keys(login)
            driver.find_element_by_css_selector("input[name='password']").send_keys(senha)
            #Clicando no botao logar
            driver.find_element_by_css_selector("button[type='submit']").click()
            sleep(5)
            #Clicando para nao salvar informacoes no navegador
            driver.find_element_by_xpath("//button[text()='Agora não']").click()
            #Clicando no botao de seguidores no perfil
            driver.find_element_by_xpath("//a[text()=' seguidores']").click()

            try:
                contador = 0
                for i in range(seguir):
                    sleep(3)
                    driver.find_element_by_xpath("//button[text()='Seguir']").click()

                    contador +=1
                    if contador ==5:
                        contador=0
                        sleep(60)

            except:
                print("Erro:")

elif opcao == '2':

    

    #Digite o link da pagina que deseja seguir os seguidores
    os.system('cls') or None #Limpa Tela 
    perfis= str(input('Digite os Links do Perfil (Separados Por ;):\n'))
   
    #Quantidades de perfil que deseja seguir
    os.system('cls') or None #Limpa Tela 
    seguir=int(input('Digite Quantos Perfil Você Deseja Deixar de Seguir: \n'))
   
    #login do Instagram
    login=str(input('Digite seu Login: '))
    #Senha Do perfil
    senha=str(input('Digite a Senha do Perfil: '))

    links=perfis.split()

    for i in range(len(links)):

        os.system('cls') or None #Limpa Tela 
        print('Iniciando Processo...')

        driver = webdriver.Chrome(executable_path="C:\Projetos\RoboSeguiInsta\webdriver\chromedriver.exe")
        driver.get(links[i])
        sleep(3)

        #Clicando no botao de login
        driver.find_element_by_css_selector("button[type='button']").click()

        sleep(1)
        #Digitando Login e senha
        driver.find_element_by_css_selector("input[name='username']").send_keys(login)
        driver.find_element_by_css_selector("input[name='password']").send_keys(senha)

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
