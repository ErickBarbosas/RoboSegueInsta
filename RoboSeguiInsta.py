
from selenium import webdriver
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import os
from time import sleep


def main():
    #Variaveis
    driver = selenium
    seguir = 0
    contador = 0
    login = ""
    senha = ""
    links= ""
    
 
########################################## ---- FUNCOES ---- #############################################

    def LogarUsuario():
        global driver
        try:
            #login do Instagram
            login=str(input('Digite seu Login: '))
            #Senha Do perfil
            senha=str(input('Digite a Senha do Perfil: '))

            #Abrindo navegados e entrando no link
            os.system('cls') or None
            print('Iniciando Processo...')        
            driver = webdriver.Chrome(executable_path="C:\Projetos\RoboSeguiInsta\webdriver\chromedriver.exe")
            driver.maximize_window() #Maximizar Page
            driver.get(links) #Abrir Link
            
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
            sleep(3) 
        except WebDriverException as Erro:
            driver.quit()
            os.system('cls') or None
            print('Ocorreu Um Erro no Processo:\n\n{}'.format(Erro))

 

    def SeguirSeguidores():    
        global driver
        global contador
        action = webdriver.ActionChains(driver)
        count = 0
        try:
            #Clicando no botao de seguidores no perfil
            driver.find_element_by_xpath("//a[text()=' seguidores']").click()
            sleep(5)
            
            #Seguindo
        
            j = 0
            for i in range(seguir):
                sleep(5)
                driver.find_element_by_xpath("//button[text()='Seguir']").click()

                action.send_keys(Keys.TAB).perform()
                action.send_keys(Keys.TAB).perform()
                action.send_keys(Keys.TAB).perform()
                                
                
                count +=1
                j +=1
                if j ==5:
                    j=0
                    sleep(70)    
        except WebDriverException as Erro:
            driver.quit()
            os.system('cls') or None
            print("Ocorreu Um Erro: \n\n{}".format(Erro))
        
        contador=count
        
   
    def DeixardeSegui():
        try: 
            global driver
            global contador
            count = 0

            #Clicando no botao de seguidores no perfil
            driver.find_element_by_xpath("//a[text()=' seguindo']").click()
            sleep(3)

            for j in range(seguir):
                sleep(5)
                driver.find_element_by_xpath("//button[text()='Seguindo']").click()
                sleep(2)
                driver.find_element_by_xpath("//button[text()='Deixar de seguir']").click()
               
                count+=1
                
        except WebDriverException as Erro:
            driver.quit()
            os.system('cls') or None
            print('Ocorreu Um Erro no Processo:\n\n{}'.format(Erro))

        contador=count
   

    def FimProcesso():
        global contador
        global driver

        driver.quit() #Fechar Page 
        print('****************************************************')    
        print('*                   Fim do Processo                *')
        print('****************************************************')
        print('****************      Meta: {} Perfis **************'.format(seguir))
        print('**************** Alcançado: {} Perfis **************'.format(contador))
        print('****************************************************')
        print('****************************************************\n')
            
        resposta =input('\nVocê Deseja Voltar Para o Menu Inicial?\n\n1-Sim\n2-Não\n\n')
        if resposta == '1':
            main()

        
#########################################--Fim Funções--#################################################
    
    #MENU
    os.system('cls') or None #Limpa Tela
    print('**************************************')
    print('*****  Robo Ganhe Seguidores :) ******')
    print('**************************************\n')
    print('*************  MENU  *****************')
    print('\nSelecione uma opção\n')
    print('1- Seguir Seguidores de um Perfil')
    print('2- Deixar De Seguir\n')

    opcao = str(input('R: '))

    if opcao =='1': #Seguir Seguidores
        
        os.system('cls') or None #Limpa Tela 
        #Digite o link da pagina que deseja seguir os seguidores
        links= str(input('Digite os Links do Perfil (Separados Por ;):\n'))
        #Quantidades de perfil que deseja seguir
        os.system('cls') or None #Limpa Tela 
        seguir=int(input('Digite Quantos Perfil Você que Seguir\n'))

        LogarUsuario()
        SeguirSeguidores()
        FimProcesso()
        
    elif opcao == '2': #Deixar de seguir

        #Digite o link da pagina que deseja seguir os seguidores
        os.system('cls') or None 
        links= str(input('Digite os Links do Perfil (Separados Por ;):\n'))
    
        #Quantidades de perfil que deseja seguir
        os.system('cls') or None 
        seguir=int(input('Digite Quantos Perfil Você Deseja Deixar de Seguir: \n'))

        LogarUsuario()
        DeixardeSegui()
        FimProcesso()

    elif opcao != '1' or opcao != '2':
            print('Valor Invalido')


if __name__ == '__main__':
    main()
