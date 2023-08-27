import sys
import time 
# Here I got the modules to start my calculator
def calculadora ():
    number_1 = int(input("primeiro número: "))
    number_2 = int(input("segundo número: "))
    # Here i decided the variable as "primeiro número" and "segundo número" and the function for below
    print("Escolhe a operação entre soma diferença multiplicação divisão e potencialização")
    operation = input("Qual operação: ") .lower ()
    operacoes (operation=operation , number_1=number_1 , number_2=number_2)
    # Here put the operacao as a variable for "qual operação" and .lower to cut down the chance of someone messing with the script  and to get the "connector between this function and the function below"

def operacoes (operation , number_1 , number_2):
    if operation == 'soma':
        soma = number_1 + number_2
        mensagem = "A soma de {} + {} = {}" .format(number_1 , number_2, soma)
        print(soma)
        # Here i got the start of the function with the information shared by the last code of the first function and the plus calculator

    elif operation == 'diferença':
        diferença = number_1 - number_2
        mensagem = "A diferença de {} - {} = {}" .format(number_1 , number_2 , diferença)
        print(diferença)
# The minus calculator
    elif operation == 'multiplicação':
        multiplicação = number_1 * number_2
        mensagem ="O produto de {} x {} = {}"  .format(number_1 , number_2 , multiplicação)
# The multiplication calculator

    elif operation == 'divisão':
        divisão = number_1 / number_2
        mensagem = "O quociente de {} / {} = {}" .format(number_1 , number_2 , divisão)
# The division calculator
    elif operation == 'potencialização':
        potencialização = number_1 ** number_2
        mensagem = "{} elevado a {} = {}"    .format(number_1 , number_2 , potencialização)
        # The exponentation calculator
    
    print(mensagem)
    another_operation = input("quer fazer outra operação? ")
    if another_operation == 'sim' or another_operation == "Sim":
        calculadora()
    elif another_operation == 'não' or another_operation == "Não":
        sys.exit()
    else: 
        print("Ou sim ou não")
        time.sleep(30)
        sys.exit()
calculadora()
# Here is the end with print(message) showing the results and the setup to start another calculation
    
    




        
    