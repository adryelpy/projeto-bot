from banco_SQLlite import MeuBanco
import pywhatkit as pwk
opcao = input('Deseja entrar no programa? [s]/[n]').lower().strip()

while opcao == 's':
    bancoIns = MeuBanco()
    bancoIns.criar_tabelas()
    
    print('BEM VINDO AO SISTEMA DE GESTÃO')
    print('======MENU=====')



    print('(1) CADASTRAR UM CLIENTE')
    print('(2) FILTRAR DADOS DO CLIENTE')


  # se escolher 1,inserir os dados do clente no banco de dados
    try:
       escolha = input('')
       escolha_int = int(escolha)

       if escolha_int == 1:
         nome = input('Nome do cliente:\n')
         cpf = input('CPF:\n')
         data_nascimento = input('Data de nasciemnto:\n')
         valor_divida = input(f'Valor da divida:\n')
         telefone = input('Telefone pra contato:\n')
         status_client = input('status [adinplemte] / [inadimplente]')
         bancoIns.criar_usuarios(nome,cpf,data_nascimento,valor_divida,telefone,status_client)
         print()
         print(f'USUARIO ({nome}) CADASTRADO COM SUCESSO!! ')
       #se escolher 2 
       elif escolha_int == 2:
          
          escolha1 = int(input('Consultar (1)inadimplemte / (2)adimplente\n'))
          if escolha1 == 1:
             status_client = 'inadimplente'
          elif escolha1 == 2: 
             status_client = 'adimplente'
          else:
             print('valor invalido!')
             continue
          
          # Consulta todos os clientes com o status q foi escolhido a cima e enviar uma mensagem com o pywhatkit se tiver duvidas abra o arquivo README[R1]👇
          tupla_elemt = bancoIns.consulta_status(status_client)
          lista_tel_inadimplente = []
          CODIGO_PAIS = '+55'

          for i in tupla_elemt:
             for numero in i:
                numero_formatado = CODIGO_PAIS + numero
                lista_tel_inadimplente.append(numero_formatado)
             print(lista_tel_inadimplente)


          escolha2 = input(f'Deseja enviar uma mensagem para os usuarios {status_client} ? [S] / [N]')
          badeira = None

          if escolha2.lower() == 's':
             mensagem = 'Ola estamos entrando em contado para analise de dividas para inadimplentes da nossa filial (Santader)'
             for i in range(len(lista_tel_inadimplente)):
                pwk.sendwhatmsg(lista_tel_inadimplente[i], mensagem, 23,23)
                badeira = True

          print(badeira)
         #continuar teste de bandeira aqui...
             
          ...
    except ValueError as e:
        print(f'ERRO {e}')
        print(f'O usuario digitou {escolha} digite um numero valido!')
        continue
        

    opcao = input('Deseja continuar no programa? [s]/[n]').lower().strip()
else:
    print('Saindo do programa...')
    quit()


'''
 A ideia principal é que, depois que o usuário escolher a opção 2,

 1. a gente pegue os números de telefone que a gente filtrou e, CONTINUAR DAQUI

 para cada um deles, use o PyWhatKit para mandar uma mensagem. Vou te dar um passo a passo. 
 Primeiro, a gente precisa garantir que o número do telefone está no formato internacional, 
 com código do país. Depois, a gente vai definir o horário de envio (por exemplo, colocar o horário atual mais um minutinho, 
 já que o PyWhatKit precisa desse tempo) e então chamar a função.
'''



    
    


    



    






