from banco_SQLlite import MeuBanco
import pywhatkit as pwk
import barcode
from barcode.writer import ImageWriter
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
          
          # Consulta todos os clientes com o status q foi escolhido a cima e enviar uma mensagem com o pywhatkit. se tiver duvidas abra o arquivo README[R1]👇
          tupla_elemt = bancoIns.consulta_status(status_client)
          lista_tel_inadimplente = []
          CODIGO_PAIS = '+55'

          for i in tupla_elemt:
             for numero in i:
                numero_formatado = CODIGO_PAIS + numero
                lista_tel_inadimplente.append(numero_formatado)
          print(lista_tel_inadimplente)


          escolha2 = input(f'Deseja enviar uma mensagem para os usuarios {status_client} ? [S] / [N]')
          
          if escolha2.lower() == 's':
             # este codigo esta explicado no README[R2]
             print('---------SERÁ GERADO UM BOLETO COM O VALOR DA DIVIDA DO INADIMPLENTE---------')
             print('')
             codigo_barras = input('Copie e cole a baixo a linha digitavel para gera um boleto:\n')                   
             #Exemplo de linha digitavel para boleto: 12345 67890 12345 67890 123456789
             codigo = barcode.get('code128', codigo_barras, writer=ImageWriter())                  
             codigo.save('boleto')

             mensagem = 'Ola estamos entrando em contado para analise de dividas para inadimplentes da nossa filial (Santader)'
             for i in range(len(lista_tel_inadimplente)):
                pwk.sendwhats_image(                #ATENÇÃO! AQUI PODE GERAR UM ERRO 'q ira precisar instalar um arquivo' ABRA O README[R3]
                   lista_tel_inadimplente[i],
                   'boleto.png',
                   mensagem,
                   15,
                   tab_close=True
                )



                #instalamos o (pip install pyboleto) para gera boletos e enviar para os inadimplentes
    except ValueError as e:
        print(f'ERRO {e}')
        print(f'O usuario digitou {escolha} digite um numero valido!')
        continue
        
    opcao = input('Deseja continuar no programa? [s]/[n]').lower().strip()
else:
    print('Saindo do programa...')
    quit()





    
    


    



    






