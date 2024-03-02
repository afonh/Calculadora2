import math
import threading
import argparse

# Preparing the software to accept arguments

parser = argparse.ArgumentParser(description="Calculadora2 accepts 2 numbers passed as arguments")
parser.add_argument("number_1_arg", nargs="?", default=None, help="Primeiro Número")
parser.add_argument("number_2_arg", nargs="?", default=None, help="Segundo Número")
args = parser.parse_args()

# Make it check if the arguments are passed or not or if just one of them are passed
# If both arguments are passed it will get the numbers automatically
# If just one argument is passed it will ask for the second number
# If no arguments are passed it will ask for both numbers

if args.number_1_arg is None and args.number_2_arg is None:
    number_1 = float(input("primeiro número: "))
    number_2 = float(input("segundo número: "))
elif args.number_1_arg is not None and args.number_2_arg is None:
    number_1 = float(args.number_1_arg)
    number_2 = float(input("segundo número: "))
elif args.number_1_arg is not None and args.number_2_arg is not None:
    number_1 = float(args.number_1_arg)
    number_2 = float(args.number_2_arg)


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
    
# Decided to add multithread support to make the calculations faster
# I could make it in another way using a lot of the old code but i prefered to make this "cleanner"

# Defining threads

thread_add = threading.Thread(target=add_operation, args=(number_1,number_2)) 
thread_minus = threading.Thread(target=minus_operation, args=(number_1,number_2))
thread_multiply = threading.Thread(target=multiply_operation, args=(number_1,number_2))
thread_division = threading.Thread(target=division_operation, args=(number_1,number_2))
thread_potentiation = threading.Thread(target=potentiation_operation, args=(number_1,number_2))
thread_square_root = threading.Thread(target=square_root_operation, args=(number_1,number_2))

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

   
