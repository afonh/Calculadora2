import sys
import time
import math

# Get the operation and the numbers needed

def calculadora ():
    number_1 = int(input("primeiro número: "))
    number_2 = int(input("segundo número: "))
    print("Escolhe a operação entre soma, diferença, multiplicação, divisão, potencialização e raíz quadrada")
    operation = input("Qual operação: ") .lower ()
    operacoes (operation=operation , number_1=number_1 , number_2=number_2)

# Get the operations and deal with the numbers

def operacoes (operation , number_1 , number_2):
    if operation == 'soma':
        soma = number_1 + number_2
        mensagem = "A soma de {} + {} = {}" .format(number_1 , number_2, soma)
        print(soma)

    elif operation == 'diferença':
        diferença = number_1 - number_2
        mensagem = "A diferença de {} - {} = {}" .format(number_1 , number_2 , diferença)
        print(diferença)
    elif operation == 'multiplicação':
        multiplicação = number_1 * number_2
        mensagem ="O produto de {} x {} = {}"  .format(number_1 , number_2 , multiplicação)


    elif operation == 'divisão':
        divisão = number_1 / number_2
        mensagem = "O quociente de {} / {} = {}" .format(number_1 , number_2 , divisão)
    elif operation == 'potencialização':
        potencialização = number_1 ** number_2
        mensagem = "{} elevado a {} = {}"    .format(number_1 , number_2 , potencialização)
        # The exponentation calculator

    elif operation == 'raíz quadrada':
        square_root = math.sqrt(number_1)
        messagem = "A raíz quadrada de {} é {}".format(number_1, square_root)
    
    print(mensagem)

    # Ask user if he wants to do another calculation

    another_operation = input("quer fazer outra operação? ")
    if another_operation.lower() == 'sim':
        calculadora()
    elif another_operation.lower() == 'não':
        sys.exit()

    # Just here to deal with exceptions
    else: 
        print("Ou sim ou não")
        time.sleep(30)
        sys.exit()


calculadora()

    
    




        
    