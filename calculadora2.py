import sys
import time 
# Here I got the modules to start my calculator
def calculadora ():
    variavel_1 = int(input("primeiro número: "))
    variavel_2 = int(input("segundo número: "))
    # Here i decided the variable as "primeiro número" and "segundo número" and the function for below
    print("Escolhe a operação entre soma diferença multiplicação divisão e potencialização")
    operacao = input("Qual operação: ") .lower ()
    operacoes (operacao = operacao , variavel_1=variavel_1 , variavel_2=variavel_2)
    # Here put the operacao as a variable for "qual operação" and .lower to cut down the chance of someone messing with the script  and to get the "connector between this function and the function below"

def operacoes (operacao , variavel_1 , variavel_2):
    if operacao == 'soma':
        soma = variavel_1 + variavel_2
        mensagem = "A soma de {} + {} = {}" .format(variavel_1 , variavel_2, soma)
        print(soma)
        # Here i got the start of the function with the information shared by the last code of the first function and the plus calculator

    elif operacao == 'diferença':
        diferença = variavel_1 - variavel_2
        mensagem = "A diferença de {} - {} = {}" .format(variavel_1 , variavel_2 , diferença)
        print(diferença)
# The minus calculator
    elif operacao == 'multiplicação':
        multiplicação = variavel_1 * variavel_2
        mensagem ="O produto de {} x {} = {}"  .format(variavel_1 , variavel_2 , multiplicação)
# The multiplication calculator

    elif operacao == 'divisão':
        divisão = variavel_1 / variavel_2
        mensagem = "O quociente de {} / {} = {}" .format(variavel_1 , variavel_2 , divisão)
# The division calculator
    elif operacao == 'potencialização':
        potencialização = variavel_1 ** variavel_2
        mensagem = "{} elevado a {} = {}"    .format(variavel_1 , variavel_2 , potencialização)
        # The exponentation calculator
    
    print(mensagem)
    variavel_do_input = input("quer fazer outra operação? ")
    if variavel_do_input == 'sim' or variavel_do_input == "Sim":
        calculadora()
    elif variavel_do_input == 'não' or variavel_do_input == "Não":
        sys.exit()
    else: 
        print("Ou sim ou não")
        time.sleep(30)
        sys.exit()
calculadora()
# Here is the end with print(message) showing the results and the setup to start another calculation
    
    




        
    