import random

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2018205041" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Joao Paulo Souza Ferrete" 

def limpaTela(): 
    return
###################################################################################
#(1) Crie uma função que solicite a letra que o jogador deve ser.                 #
# A função retorna dois valores. Se o jogardor desejar ser "X", retorne "X", "O". #
# Caso contrário, retorne "O", "X".                                               #
###################################################################################

def defineLetra():
    letra = input("Insira a letra que deseja jogar (X ou O): ")
    if letra == "X" or letra == "x": return "X", "O"
    elif letra == "O" or letra == "o": return "O", "X"
    else:
        print("Letra Inválida!")
        return defineLetra()


###################################################################################
#(2) Crie uma função que dicida/retorna quem será o primeiro a jogar.             #
# Use o módulo random.                                                            #
###################################################################################
def decideJogada():
    num = random.randint(0, 10000)
    if num%2==0: return True
    else: return False

###################################################################################
#(3) Crie uma função para imprimir o tabuleiro.                                   #
# Função não retorna nada, apenas imprime.                                        #
###################################################################################
def imprimeTab(lista):
    print(f" {lista[7]} | {lista[8]} | {lista[9]} ")
    print("---|---|---")
    print(f" {lista[4]} | {lista[5]} | {lista[6]} ")
    print("---|---|---")
    print(f" {lista[1]} | {lista[2]} | {lista[3]} ")

###################################################################################
#(4) Faça uma função que solicite ao usuário onde ele deseja jogar.               # 
# A função retorna um inteiro entre 1 e 9 (posisão escolhida)                     #
# A função deve garantir que o usuários selecionou uma posição válida             #
###################################################################################
def solicitaJogada(lista):
    ent = int(input("Insira a posição que deseja jogar (1-9): "))
    if 1>ent or 9<ent:
        print("Posição Inválida!")
        return solicitaJogada(lista)

    if lista[ent] == " ": return ent
    else:
        print("Posição Inválida!")
        return solicitaJogada(lista)

###################################################################################
#(5) Faça uma função que retorna True se o "X" ou "O" ganhou e False, caso        #
# contrário. A função deve receber o tabuleiro e o simbolo a ser testado.         #
# Verifique todas as possibilidades e retorne True caso uma delas o simbolo       # 
# ganhou. Por exemplo, se nas posições 7, 8 e 9 do tabuleiro contém "X",          # 
# significa que "X" ganhou e a função deve retornar True.                         #
###################################################################################
def verifGanhador(lista, simbolo):
    if lista[1] == simbolo and lista[2] == simbolo and lista[3] == simbolo: return True
    elif lista[4] == simbolo and lista[5] == simbolo and lista[6] == simbolo: return True
    elif lista[7] == simbolo and lista[8] == simbolo and lista[9] == simbolo: return True
    elif lista[1] == simbolo and lista[5] == simbolo and lista[9] == simbolo: return True
    elif lista[3] == simbolo and lista[5] == simbolo and lista[7] == simbolo: return True
    elif lista[1] == simbolo and lista[4] == simbolo and lista[7] == simbolo: return True
    elif lista[2] == simbolo and lista[5] == simbolo and lista[8] == simbolo: return True
    elif lista[3] == simbolo and lista[6] == simbolo and lista[9] == simbolo: return True
    return False

###################################################################################
#(6) Faça uma função que retorne True se houve empate e False, caso contrário.    #
# Para isso, basta verificar se o tabuleiro está todo preenchido, ou seja, não    #
# contém nenhum espaço em branco.                                                 #
###################################################################################
def verifEmpate(lista):
    if " " in lista: return False
    return True

###################################################################################
#(7.1) Faça uma função que receba o tabuleiro e retorne as posições, entre 1 e 9  #
# que estão livres                                                                #
###################################################################################
def posicaoVaga(lista, result = [], i=1):
    if i==1: result = []
    if i>9: return result
    if lista[i] == " ": result+=[i]
    return posicaoVaga(lista, result, i+1)

###################################################################################
#(7.2) Faça uma função que receba o tabuleiro, escolha (aleatoriamente) e retorne # 
# uma posição livre. Use a função (7.1).
###################################################################################
def posicaoLivre(lista):
    vaga = posicaoVaga(lista)
    a = random.randint(0, len(vaga)-1)
    return vaga[a]

###################################################################################
#(8) Começa a implementar a função jogadaComputador. De início, você pode apenas  #
# sortear uma posição livre como sendo a jogada do computador. Use a função (7.2) #
# Posteriormente, implemente alguma estratégia mais  "inteligente".               #
###################################################################################
def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador
    """
    simboloJogador = "X" if simboloComputador=="O" else "O"

    vaga = posicaoVaga(tabuleiro)

    if len(vaga) == 9: return random.choice([5, 1, 7, 9])
    elif len(vaga) == 8:
        if 5 in vaga: return 5
        elif 1 in vaga: return 1
        else: return 7
    elif tabuleiro[1] == simboloComputador and tabuleiro[2] == simboloComputador and 3 in vaga: return 3
    elif tabuleiro[1] == simboloComputador and tabuleiro[3] == simboloComputador and 2 in vaga: return 2
    elif tabuleiro[2] == simboloComputador and tabuleiro[3] == simboloComputador and 1 in vaga: return 1
    elif tabuleiro[4] == simboloComputador and tabuleiro[5] == simboloComputador and 6 in vaga: return 6
    elif tabuleiro[4] == simboloComputador and tabuleiro[6] == simboloComputador and 5 in vaga: return 5
    elif tabuleiro[5] == simboloComputador and tabuleiro[6] == simboloComputador and 4 in vaga: return 4
    elif tabuleiro[7] == simboloComputador and tabuleiro[8] == simboloComputador and 9 in vaga: return 9
    elif tabuleiro[7] == simboloComputador and tabuleiro[9] == simboloComputador and 8 in vaga: return 8
    elif tabuleiro[8] == simboloComputador and tabuleiro[9] == simboloComputador and 7 in vaga: return 7
    elif tabuleiro[1] == simboloComputador and tabuleiro[4] == simboloComputador and 7 in vaga: return 7
    elif tabuleiro[1] == simboloComputador and tabuleiro[7] == simboloComputador and 4 in vaga: return 4
    elif tabuleiro[4] == simboloComputador and tabuleiro[7] == simboloComputador and 1 in vaga: return 1
    elif tabuleiro[2] == simboloComputador and tabuleiro[5] == simboloComputador and 8 in vaga: return 8
    elif tabuleiro[2] == simboloComputador and tabuleiro[8] == simboloComputador and 5 in vaga: return 5
    elif tabuleiro[5] == simboloComputador and tabuleiro[8] == simboloComputador and 2 in vaga: return 2
    elif tabuleiro[3] == simboloComputador and tabuleiro[6] == simboloComputador and 9 in vaga: return 9
    elif tabuleiro[3] == simboloComputador and tabuleiro[9] == simboloComputador and 6 in vaga: return 6
    elif tabuleiro[6] == simboloComputador and tabuleiro[9] == simboloComputador and 3 in vaga: return 3
    elif tabuleiro[1] == simboloComputador and tabuleiro[5] == simboloComputador and 9 in vaga: return 9
    elif tabuleiro[1] == simboloComputador and tabuleiro[9] == simboloComputador and 5 in vaga: return 5
    elif tabuleiro[5] == simboloComputador and tabuleiro[9] == simboloComputador and 1 in vaga: return 1
    elif tabuleiro[3] == simboloComputador and tabuleiro[5] == simboloComputador and 7 in vaga: return 7
    elif tabuleiro[3] == simboloComputador and tabuleiro[7] == simboloComputador and 5 in vaga: return 5
    elif tabuleiro[7] == simboloComputador and tabuleiro[5] == simboloComputador and 3 in vaga: return 3


    elif tabuleiro[1] == simboloJogador and tabuleiro[2] == simboloJogador and 3 in vaga: return 3
    elif tabuleiro[1] == simboloJogador and tabuleiro[3] == simboloJogador and 2 in vaga: return 2
    elif tabuleiro[2] == simboloJogador and tabuleiro[3] == simboloJogador and 1 in vaga: return 1
    elif tabuleiro[4] == simboloJogador and tabuleiro[5] == simboloJogador and 6 in vaga: return 6
    elif tabuleiro[4] == simboloJogador and tabuleiro[6] == simboloJogador and 5 in vaga: return 5
    elif tabuleiro[5] == simboloJogador and tabuleiro[6] == simboloJogador and 4 in vaga: return 4
    elif tabuleiro[7] == simboloJogador and tabuleiro[8] == simboloJogador and 9 in vaga: return 9
    elif tabuleiro[7] == simboloJogador and tabuleiro[9] == simboloJogador and 8 in vaga: return 8
    elif tabuleiro[8] == simboloJogador and tabuleiro[9] == simboloJogador and 7 in vaga: return 7
    elif tabuleiro[1] == simboloJogador and tabuleiro[4] == simboloJogador and 7 in vaga: return 7
    elif tabuleiro[1] == simboloJogador and tabuleiro[7] == simboloJogador and 4 in vaga: return 4
    elif tabuleiro[4] == simboloJogador and tabuleiro[7] == simboloJogador and 1 in vaga: return 1
    elif tabuleiro[2] == simboloJogador and tabuleiro[5] == simboloJogador and 8 in vaga: return 8
    elif tabuleiro[2] == simboloJogador and tabuleiro[8] == simboloJogador and 5 in vaga: return 5
    elif tabuleiro[5] == simboloJogador and tabuleiro[8] == simboloJogador and 2 in vaga: return 2
    elif tabuleiro[3] == simboloJogador and tabuleiro[6] == simboloJogador and 9 in vaga: return 9
    elif tabuleiro[3] == simboloJogador and tabuleiro[9] == simboloJogador and 6 in vaga: return 6
    elif tabuleiro[6] == simboloJogador and tabuleiro[9] == simboloJogador and 3 in vaga: return 3
    elif tabuleiro[1] == simboloJogador and tabuleiro[5] == simboloJogador and 9 in vaga: return 9
    elif tabuleiro[1] == simboloJogador and tabuleiro[9] == simboloJogador and 5 in vaga: return 5
    elif tabuleiro[5] == simboloJogador and tabuleiro[9] == simboloJogador and 1 in vaga: return 1
    elif tabuleiro[3] == simboloJogador and tabuleiro[5] == simboloJogador and 7 in vaga: return 7
    elif tabuleiro[3] == simboloJogador and tabuleiro[7] == simboloJogador and 5 in vaga: return 5
    elif tabuleiro[7] == simboloJogador and tabuleiro[5] == simboloJogador and 3 in vaga: return 3
    
    return posicaoLivre(tabuleiro)

###################################################################################
#(9) Faça uma função que será responsável pelas jogadas, intercalando entre o     # 
# jogador e o computador. Essa função, caso queira, pode retornar quem venceu ou  # 
# se o jogo terminou empatado. Note que essas função deve ser recursiva, ou seja, # 
# ela deve ser chamada recursivamente para cada jogada enquanto não houver        # 
# vencedor ou empate.                                                             #
# Sugestão de parâmetros obrigatórios para essa fução:                            #
# - Tabuleiro                                                                     #
# - De quem é a vez da jogada                                                     #
# - Simbolo do jogador                                                            #
# - Simbolo do computador                                                         #
###################################################################################
def jogadas(tabuleiro, vez, simboloJogador, simboloComputador):
    if verifGanhador(tabuleiro, simboloJogador):
        print("Você venceu!")
        imprimeTab(tabuleiro)
        return
    elif verifGanhador(tabuleiro, simboloComputador):
        print("O Computador venceu!")
        imprimeTab(tabuleiro)
        return
    elif verifEmpate(tabuleiro):
        print("EMPATE!")
        imprimeTab(tabuleiro)
        return

    if vez:
        imprimeTab(tabuleiro)
        jogada = solicitaJogada(tabuleiro)
        tabuleiro[jogada] = simboloJogador
        vez = False
    elif not vez:
        jogada = jogadaComputador(tabuleiro, simboloComputador)
        tabuleiro[jogada] = simboloComputador
        vez = True
    jogadas(tabuleiro, vez, simboloJogador, simboloComputador)
    



def main():
    limpaTela()
    #(10) Mensagem de boas-vindas :)
    print("Bem vindo ao Jogo da Velha! :)")
    #(11) Cria o tabuleiro (uma lista de tamanho 10, inicialmente vazia). 
    # Escolha algum simbolo para representar que determinada posição está vazia.
    # Minha sugestão é "" ou " ", mas sinta-se a vontade para escolher o simbolo 
    # que achar melhor.
    tabuleiro = [" "]*10
    tabuleiro[0] = "j"

    #(12) Chame a função (1) e atribua o resultado a duas variáveis. Uma irá representar
    # o simbolo do jogador e a outra o simbolo do computador.
    simboloJogador, simboloComputador = defineLetra()
    #(13) Chame a função (2) e atribua o resultado a um variável que representa quem 
    # começa jogando.
    comeca = decideJogada()
    # Imprima quem irá começar a partida.
    if comeca: print("Você Começa!")
    else: print("O computador começa!")
    #(14) Chame a função (9)
    jogadas(tabuleiro, comeca, simboloJogador, simboloComputador)



if __name__ == "__main__":
    main()

