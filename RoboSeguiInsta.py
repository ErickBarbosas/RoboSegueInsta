from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
from time import sleep

def main():

    links=[]
    valor=[]

    os.system('cls') or None #Limpa Tela
    print('**************************************')
    print('*****  Robo Ganhe Seguidores :) ******')
    print('**************************************\n')
    print('*************  MENU  *****************')
    print('\nSelecione uma opção\n')
    print('1- Seguir Seguidores de um Perfil')
    print('2- Deixar De Seguir\n')

    opcao = str(input('R: '))

    if opcao =='1':
        
        contador = 0
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
                j = 0
                for i in range(seguir):
                    sleep(3)
                    driver.find_element_by_xpath("//button[text()='Seguir']").click()

                    contador+=1
                    j +=1
                if j ==5:
                    j=0
                    sleep(70)

            except WebDriverException as Erro:
                os.system('cls') or None
                print("Ocorreu Um Erro: \n\n{}".format(Erro))
        
        driver.close()
        os.system('cls') or None  
        print('****************************************************')    
        print('*           Fim do Processo (Seguir Perfis)        *')
        print('****************************************************')
        print('****************      Meta: {} Perfis **************'.format(seguir))
        print('**************** Alcançado: {} Perfis **************'.format(contador))
        print('****************************************************')
        print('****************************************************\n')
        
        resposta =input('\nVocê Deseja Voltar Para o Menu Inicial?\n\n1-Sim\n2-Não\n\n')
        if resposta == '1':
            main()

    elif opcao == '2':
        contador=0
        try:  
            
            #Digite o link da pagina que deseja seguir os seguidores
            os.system('cls') or None #Limpa Tela 
            perfis= str(input('Digite os Links do Perfil (Separados Por ;):\n'))
        
            #Quantidades de perfil que deseja seguir
            os.system('cls') or None #Limpa Tela 
            seguir=int(input('Digite Quantos Perfil Você Deseja Deixar de Seguir: \n'))
        
            #login do Instagram
            os.system('cls') or None #Limpa Tela 
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
                    sleep(5)
                    driver.find_element_by_xpath("//button[text()='Seguindo']").click()
                    sleep(10)
                    driver.find_element_by_xpath("//button[text()='Deixar de seguir']").click()
                    contador+=1
                
               
        except WebDriverException as Erro:
            os.system('cls') or None
            print('Ocorreu Um Erro no Processo:\n\n{}'.format(Erro))

        driver.close()
        os.system('cls') or None    
        print('****************************************************')  
        print('*      Fim do Processo (Deixar de Segui Perfis)    *')
        print('****************************************************')
        print('****************      Meta: {} Perfis **************'.format(seguir))
        print('**************** Alcançado: {} Perfis **************'.format(contador))
        print('****************************************************')
        print('****************************************************\n\n')
        
        resposta =input('\nVocê Deseja Voltar Para o Menu Inicial?\n\n1-Sim\n2-Não\n\n')
        if resposta == '1':
            main()


    elif opcao != '1' or opcao != '2':
            print('Valor Invalido')


if __name__ == '__main__':
    main()
