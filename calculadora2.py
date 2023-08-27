import sys
import time
import math
import threading

# Get the numbers needed

number_1 = int(input("primeiro número: "))
number_2 = int(input("segundo número: "))


# Get the numbers and define how the operations are handled

def add_operation(number_1, number_2):
    add = number_1 + number_2
    print("A soma de {} + {} = {}" .format(number_1 , number_2, add))

def minus_operation(number_1, number_2):
    minus = number_1 - number_2
    print("A diferença de {} - {} = {}".format(number_1 , number_2 , minus))

def multiply_operation(number_1, number_2):
    multiply = number_1 * number_2
    print("O produto de {} x {} = {}".format(number_1 , number_2 , multiply))

def division_operation(number_1, number_2):
    division = number_1 / number_2
    print("O quociente de {} / {} = {}".format(number_1 , number_2 , division))

def potentiation_operation(number_1, number_2):
    potentiation = number_1 ** number_2
    print("{} elevado a {} = {}".format(number_1 , number_2 , potentiation))

def square_root_operation(number_1, number_2):
    square_root_1 = math.sqrt(number_1)
    square_root_2 = math.sqrt(number_2)
    print("A raíz quadrada de {} é {} e de {} é {}".format(number_1, square_root_1, number_2, square_root_2))
    
# Defining threads

thread_add = threading.Thread(target=add_operation)
thread_minus = threading.Thread(target=minus_operation)
thread_multiply = threading.Thread(target=multiply_operation)
thread_division = threading.Thread(target=division_operation)
thread_potentiation = threading.Thread(target=potentiation_operation)
thread_square_root = threading.Thread(target=square_root_operation)

# Running threads

thread_add.start()
thread_minus.start()
thread_multiply.start()
thread_division.start()
thread_potentiation.start()
thread_square_root.start()

# Waiting for the threads to finish

thread_add.join()
thread_minus.join()
thread_multiply.join()
thread_division.join()
thread_potentiation.join()
thread_square_root.join()


    # Ask user if he wants to do another calculations

def another_operation():
    another_operation = input("quer fazer outra operação? ")
    if another_operation.lower() == 'sim':
        pass
    elif another_operation.lower() == 'não':
        sys.exit()
    else: 
        print("Ou sim ou não")
        time.sleep(30)
        sys.exit()




    
    




        
    