from turtle import Turtle                                                          #Importa biblioteca turtle

t = Turtle()                                                                       #Inicia turtle
t.speed(3)                                                                         #Define a velocidade da turtle

def obter_distancia():
    resposta = int(input('Quantos pixels percorrer? '))  
    return resposta

def rotacionar_graus():
    graus = int(input('Rotacionar quantos graus? '))
    return graus

while True:                                                                        #Inicia um loop
    direcao_frente = input('Deseja ir pra frente ou pra trás? ')                   #Variavel com input pra guardar a resposta
    if direcao_frente == 'frente':                                                 #Condição se a resposta for 'frente'
        pixels_frente = obter_distancia()                                          #Variavel com input pra guardar a reposta
        t.forward(pixels_frente)                                                   #Move a turtle pra frente de acordo com a resposta acima

    elif direcao_frente == 'tras':                                                 #Segunda condição da primeira pergunta
        pixels_tras = obter_distancia()                                            #Variavel com input pra guardar a respota
        t.backward(pixels_tras)                                                    #Move a turtle pra tras de acordo com a respota acima

    rotacionar = input('Deseja rotacionar pra esquerda ou direita? ')              #Variavel com input pra guardar a resposta
    if rotacionar == 'direita':                                                    #Condição se a resposta for 'direita'
        pixel_direita = rotacionar_graus()                                         #Variavel com input pra guardar a reposta
        t.right(pixel_direita)                                                     #Rotaciona pra direita de acordo com a resposta acima

    elif rotacionar == 'esquerda':                                                 #Segunda condição da segunda pergunta
        pixels_esqueda = rotacionar_graus()                                        #Variavel com input pra guardar a respota
        t.left(pixels_esqueda)                                                     #Rotaciona pra esquerda de acordo com a respota acima

    contiunar = input('Deseja continuar andando? ')                                #Variavel com input pra guarda ultima pergunta
    if contiunar == 'nao':                                                         #Condição se deve continuar
        break                            