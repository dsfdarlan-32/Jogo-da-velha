inicio = 1
while (inicio == 1):

    print("Menu:")
    print("1.Instruções.")
    print("2.Novo jogo.")
    print("3.Sair.\n")
    op = int(input("Digite o numero correspondente. "))

    if( op == 1):
        print("\n")
        print('jogador 1 joga com "X"')
        print('jogador 2 joga com "O"')
        print("jogador 1 sempre começa")
        print("-----------------------------------------------------")
        print("Para escolher a posição, utilize os numeros a seguir:")
        print("-----------------------------------------------------")
        
        matriz2 = [[1,2,3],[4,5,6],[7,8,9]]
        print( matriz2[0][0] , '|' ,  matriz2[0][1] , '|' ,  matriz2[0][2] )
        print('---------')
        print( matriz2[1][0] , '|' ,  matriz2[1][1] , '|' ,  matriz2[1][2] )
        print('---------')
        print( matriz2[2][0] , '|' ,  matriz2[2][1] , '|' ,  matriz2[2][2] )
        print("\n")

    if(op == 2):

        matriz = [[0,0,0],[0,0,0],[0,0,0]]
        matriz2 = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

        print ( matriz2[0][0] , '|' ,  matriz2[0][1] , '|' ,  matriz2[0][2] )
        print ('---------')
        print ( matriz2[1][0] , '|' ,  matriz2[1][1] , '|' ,  matriz2[1][2] )
        print ('---------')
        print ( matriz2[2][0] , '|' ,  matriz2[2][1] , '|' ,  matriz2[2][2] )
        print ('-----------------------------------------------------------------')

        ganhou = 0
        teste = 1
        
        while(teste <= 9 ):

            entrada = int(input("jogador 1 "))
            if entrada == 1:
                matriz[2][0] = 1
                matriz2[2][0] = 'X'

            if entrada == 2:
                matriz[2][1] = 1
                matriz2[2][1] = 'X'
                    
            if entrada == 3:
                matriz[2][2] = 1
                matriz2[2][2] = 'X'
                    
            if entrada == 4:
                
                matriz[1][0] = 1
                matriz2[1][0] = 'X'
                    
            if entrada == 5:
                matriz[1][1] = 1
                matriz2[1][1]= 'X'
                    
            if entrada == 6:
                matriz[1][2] = 1
                matriz2[1][2] = 'X'
                    
            if entrada == 7:
                matriz[0][0] = 1
                matriz2[0][0] = 'X'
                    
            if entrada == 8:
                matriz[0][1]=1
                matriz2[0][1]= 'X'
                    
            if entrada == 9:
                matriz[0][2] = 1 
                matriz2[0][2] = 'X'


            print ( matriz2[0][0] , '|' ,  matriz2[0][1] , '|' ,  matriz2[0][2] )
            print ('---------')
            print ( matriz2[1][0] , '|' ,  matriz2[1][1] , '|' ,  matriz2[1][2] )
            print ('---------')
            print ( matriz2[2][0] , '|' ,  matriz2[2][1] , '|' ,  matriz2[2][2] )
            print ('-----------------------------------------------------------------')
            

            for i in (0,1,2):

                soma = 0
                soma2 = 0
                 
                for f in (0,1,2):
                    soma += matriz[i][f]
                    soma2 += matriz[f][i]


                if(soma == 3 or soma2 == 3):
                    print("Jogador 1 ganhou\n")
                    ganhou = 1

                s = matriz[0][0] +  matriz[1][1] + matriz[2][2]
                s2 = matriz[2][0] +  matriz[1][1] + matriz[0][2]

                if(s == 3 or s2 == 3):
                    print("Jogador 1 ganhou\n")
                    ganhou = 1


            if ganhou == 1:
                break 

            if(teste == 9):
                print("Houve um empate\n")
                break
                
            teste +=1
            
            
            entrada = int(input("jogador 2 "))
            if entrada == 1:
                matriz[2][0] = -1
                matriz2[2][0] = "O"

            if entrada == 2:
                matriz[2][1] = -1
                matriz2[2][1] = "O"
                    
            if entrada == 3:
                matriz[2][2] = -1
                matriz2[2][2] = "O"
                    
            if entrada == 4:
                matriz[1][0] = -1
                matriz2[1][0] = "O"
                    
            if entrada == 5:
                matriz[1][1] = -1
                matriz2[1][1] = "O"
                    
            if entrada == 6:
                matriz[1][2] = -1
                matriz2[1][2] = "O"
                    
            if entrada == 7:
                matriz[0][0] = -1
                matriz2[0][0] = "O"
                    
            if entrada == 8:
                matriz[0][1] = -1
                matriz2[0][1] = "O"
                    
            if entrada == 9:
                matriz[0][2] = -1
                matriz2[0][2] = "O"


            print ( matriz2[0][0] , '|' ,  matriz2[0][1] , '|' ,  matriz2[0][2] )
            print ('---------')
            print ( matriz2[1][0] , '|' ,  matriz2[1][1] , '|' ,  matriz2[1][2] )
            print ('---------')
            print ( matriz2[2][0] , '|' ,  matriz2[2][1] , '|' ,  matriz2[2][2] )
            print ('-----------------------------------------------------------------')
            

            for i in (0,1,2):

                soma = 0
                soma2 = 0
                
                for f in (0,1,2):

                    soma += matriz[i][f]
                    soma2 += matriz[f][i]


                if(soma == -3 or soma2 == -3):
                    print("Jogador 2 ganhou\n")            
                    ganhou = 1

                s = matriz[0][0] +  matriz[1][1] + matriz[2][2]
                s2 = matriz[0][2] +  matriz[1][1] + matriz[2][0]

                if(s == -3 or s2 == -3):
                    print("Jogador 2 ganhou\n")
                    ganhou = 1


            if ganhou == 1:
                break 

            teste +=1

    if(op == 3):
        inicio = 0

        
        test